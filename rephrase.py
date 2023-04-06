import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_completion = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "user", 
     "content": "Rephrase the following paragraph: Researchers at Nokia Bell Labs have been behind or involved in nearly every critical technological milestone for the last nine decades. They built the first lasers and transistors, discovered the origins of the universe, and connected the world using communications satellites. They also invented implementable technologies like the solar battery and the first hearing aids and made great theoretical leaps forward with the likes of Information Theory. Every decade of existence has brought new ideas, new breakthroughs, and new contributions to humanity. At Bell Labs, researchers break down the essential ideas, people and concepts that shaped Bell Labs over time."
    }
  ]
)

print(chat_completion.choices[0].message)