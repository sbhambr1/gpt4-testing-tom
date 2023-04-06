import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_completion = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "user", 
     "content": "Suppose g is a continuous smooth function such that for every x > 0, there is one and only one y > 0 such that g(x) + g(y) ≤ 2xy. Can you prove that g(x) != x^2?"
    }
  ]
)

print(chat_completion.choices[0].message)