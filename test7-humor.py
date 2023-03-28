import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_completion = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "user", 
     "content": "Conversation: Clara: Hey Steve, how are you doing today? Steve: Hey Clara, I just finished writing my project report and I am so relieved now. Clara: That’s great! Do you have any plans to go out for celebrating tonight? Steve: I used to think I was indecisive, but now I’m not really sure. -- Q. What is Clara’s reaction going to be? "
    }
  ]
)

print(chat_completion.choices[0].message)