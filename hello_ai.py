from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "What is Generative AI in exactly 2 sentences?"}]
)
print(response.choices[0].message.content)


# Generative AI refers to a type of artificial intelligence 
# that uses complex algorithms and neural networks to generate 
# new, original content, such as images, videos, music, or text,
# based on a given set of inputs or prompts. This technology 
# has the potential to revolutionize various industries, 
# including art, entertainment, and marketing, by enabling 
# machines to create high-quality, realistic, and often 
# innovative content that is similar to, or even 
# indistinguishable from, human-created work.