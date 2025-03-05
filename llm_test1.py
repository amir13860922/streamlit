import ollama as llm

model_llm = llm.ollama(modelNa = "deepseek")

response = model_llm.run()

print(response)