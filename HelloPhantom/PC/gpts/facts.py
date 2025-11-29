from gpt4all import GPT4All

class factsGPT:
    def getFacts(prompt):

        model = GPT4All('Meta-Llama-3-8B-Instruct.Q4_0.gguf', allow_download=False)
        #model = GPT4All('orca-mini-3b-gguf2-q4_0.gguf', allow_download=False)

        #weatherresponse = [WeatherScrape.scrapeWeather("today"), WeatherScrape.scrapeWeather("tomorrow")]
        #print(f"\nweatherresponse:\ntoday: {weatherresponse[0]}\ntomorrow: {weatherresponse[1]}\n")


        system_prompt = '### System:\nYou are an AI  assistant model, meant to answer the questions of users with information given to with your own knowledge. Keep your responses brief and to one line, and only supply the information asked for.\n\n'
        prompt_template = '### User:\n{0}\n\n### Response:\n'



        output = ""

        with model.chat_session(system_prompt=system_prompt, prompt_template=prompt_template):
            for token in model.generate(prompt, streaming=True):
                #print(token)
                print(token, end='', flush=True)
                output += (token + '')

        print('\n\nSaved output: ' + output)
        print('\nSpoken output: ' + output.split('###')[0] + '\n')

        return [prompt, output.split('###')[0].split('\n')[0]]

    
    if __name__ == "__main__":
        print(getFacts(input("q: ")))