from langchain_community.llms import GPT4All

# Instantiate the model. Callbacks support token-wise streaming
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

# Generate text
response = model.invoke("Once upon a time, ")