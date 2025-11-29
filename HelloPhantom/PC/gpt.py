from gpt4all import GPT4All
from gpts.weather import weatherGPT
from gpts.events import eventGPT
from gpts.facts import factsGPT


class PhantomGPT:
    def PhantomSpeak(prompt):

        #prompt = input("Q: ")


        model = GPT4All('Meta-Llama-3-8B-Instruct.Q4_0.gguf', allow_download=False)
        #model = GPT4All('orca-mini-3b-gguf2-q4_0.gguf', allow_download=False)

       


        system_prompt = '### System:\nYou are tasked with classifying the intent of an input question into three categories: weather, events, advice, and facts. You must classify the input into one of these categories. Keep your responses brief.\n\n'
        prompt_template = '### User:\n{0}\n\n### Response: \n'



        intent_output = ""
        intent = ""
        tries = 0

        while (not (intent == "weather" or intent == "events" or intent == "facts")) and (tries < 3):

            with model.chat_session(system_prompt=system_prompt):
                for token in model.generate(prompt, streaming=True):
                    #print(token)
                    print(token, end='', flush=True)
                    intent_output += (token + '')

            print('\n\nSaved intent output: ' + intent_output)
            
            if not intent_output.find('"') == -1:
                intent = intent_output.split('"')[1].lower()
            print('\n\nFound intent: ' + intent)

            intent_output = ""

            if not (intent == "weather" or intent == "events" or intent == "facts"):
                tries += 1

        if intent == "weather":
            output = weatherGPT.getWeather(prompt)
        elif intent == "events":
            output = eventGPT.getEvents(prompt)
        elif intent == "facts" or intent == "advice":
            output = factsGPT.getFacts(prompt)
        else:
            output = "I'm sorry, I can't answer that."
            

        return [prompt, output]

    
    if __name__ == "__main__":
        print(PhantomSpeak(input("Q: ")))