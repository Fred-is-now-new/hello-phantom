from gpt4all import GPT4All
from weatherscrape_test import WeatherScrape
from events_test import EventScrape
model = GPT4All('Meta-Llama-3-8B-Instruct.Q4_0.gguf', allow_download=False)
#model = GPT4All('orca-mini-3b-gguf2-q4_0.gguf', allow_download=False)

weatherresponse = [WeatherScrape.scrapeWeather("today"), WeatherScrape.scrapeWeather("tomorrow")]
print(f"weatherresponse:\ntoday: {weatherresponse[0]}\ntomorrow: {weatherresponse[1]}")

eventresponse = EventScrape.scrapeEventsWithDiagnostics()

system_prompt = '### System:\nYou are tasked with classifying the intent of an input question into three categories: weather, events, and facts.\n\n'
prompt_template = '### User:\n{0}\n\n### Classification: \n'

output = ""

with model.chat_session(system_prompt=system_prompt, prompt_template=prompt_template):
    for token in model.generate(input("Q: "), streaming=True):
        #print(token)
        print(token, end='', flush=True)
        output += (token + '')

print('Saved output: ' + output)
print('Spoken output: ' + output.split('###')[0])