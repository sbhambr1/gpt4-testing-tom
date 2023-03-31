import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_completion = openai.Completion.create(
  model="text-davinci-003",
  messages=[
    {"role": "user", 
     "content": "I order idli here and I'm thinking which game I can play with those. Please help me to choose one: 1)base ball, 2)cricket? What does the customer feel about the idli he ordered?"
    }
  ]
)

print(chat_completion.choices[0].message)