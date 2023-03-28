import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

print('Testing OpenAI API for completion...')

completion = openai.Completion.create(
    model="text-davinci-003", # text-davinci-003, gpt-3.5-turbo, gpt-4
    prompt="Say this is a test",
    max_tokens=7,
    temperature=0)

print(completion.choices[0].text)

print('---------------------------------')

print('Testing OpenAI API for chat completion...')

chat_completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(chat_completion.choices[0].message)



