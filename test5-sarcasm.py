import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_completion = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "user", 
     "content": "Conversation: Link: Things are going to get better, just hold on. Rhett: I hope the same. Link: Hey, I just got a message from Stevie that there has been a theft at your house! Rhett: Oh god, that is exactly what I needed today. -- Q. What did Rhett exactly need today?"
    }
  ]
)

print(chat_completion.choices[0].message)