# deploy chatGPT using its API

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
_prompt = "tell me a joke about Winnie-the-Pooh"

#gpt-3.5-turbo
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=_prompt,
  temperature=0,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=None
)
generated_text = response.choices[0]['text'].strip()
print(generated_text)

print('End')
