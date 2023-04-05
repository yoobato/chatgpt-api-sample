import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']

print('### Enter q to exit')

messages = []
while True:
    user_content = input('User : ')
    if user_content == 'q':
        break

    messages.append({
        'role': 'user',
        'content': user_content
    })

    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )

    assistant_content = completion.choices[0].message['content'].strip()
    messages.append({
        'role': 'assistant',
        'content': assistant_content
    })
    print(f'ChatGPT : {assistant_content}')
