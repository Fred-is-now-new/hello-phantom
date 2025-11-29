from gpt4all import GPT4All
from webscrape.events import EventScrape
import datetime

class eventGPT:
    def getEvents(prompt):

        model = GPT4All('Meta-Llama-3-8B-Instruct.Q4_0.gguf', allow_download=False)
        #model = GPT4All('orca-mini-3b-gguf2-q4_0.gguf', allow_download=False)

        eventresponse = EventScrape.scrapeEventsWithDiagnostics()
        print(f"\neventresponse:\n{eventresponse}")

        today = datetime.datetime.now()
        #print("\nDatetime info: " + str(today))

        system_prompt = '### System:\nYou are an AI  assistant model, meant to answer the questions of users with information given to you by a real-time source. Keep your responses brief, and only supply the information asked for. The date today is ' + today.strftime("%A") + ", " + today.strftime("%B") + " " + today.strftime("%d")  + '. Your source tells you that the events this month are ' + eventresponse + '.\n\n'
        prompt_template = '### User:\n{0}\n\n### Response:\n'



        output = ""

        with model.chat_session(system_prompt=system_prompt, prompt_template=prompt_template):
            for token in model.generate(prompt, streaming=True):
                #print(token)
                print(token, end='', flush=True)
                output += (token + '')

        print('\n\nSaved output: ' + output)
        print('\nSpoken output: ' + output.split('###')[0] + '\n')

        return [prompt, output.split('###')[0]]

    
    if __name__ == "__main__":
        print(getEvents(input("q: ")))