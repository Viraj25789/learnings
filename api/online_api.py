from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
     model="gemini-flash-latest",
     messages=[
         {
             "role":"user", "content":"hey give me 2+2 "
         }
     ]
 )

print(response.choices[0].message.content)


# models = client.models.list()

# for model in models.data:
#     print(model.id)