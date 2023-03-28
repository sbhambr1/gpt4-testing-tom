import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_completion = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "user", 
     "content": "Conversation: Sergeant Mark: I believe there are huge loopholes in your strategy for the east front. I would advise against that. Sergeant John: You are not seeing what I am seeing here. We have to utilize this opportunity! Sergeant Mark (angrily): This is going to be a failure! Major Steve: Easy sergeants! You can’t fight here. This is a war room! Sergeant John: Hahaha, that was a good one Major. -- Q. What is Major Steve’s sentiment here? "
    }
  ]
)

print(chat_completion.choices[0].message)