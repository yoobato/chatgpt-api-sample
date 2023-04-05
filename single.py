import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']

# TODO: role: system 은 뭘까?
completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'user',
            'content': 'Hello!'
        }
    ]
)
# print(completion.choices[0].message)

print(completion)
# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "message": {
#         "content": "Hello there! How can I assist you today?",
#         "role": "assistant"
#       }
#     }
#   ],
#   "created": 1680692225,
#   "id": "chatcmpl-71v734x0zjHhEa7zVkD26bnqsCQdA",
#   "model": "gpt-3.5-turbo-0301",
#   "object": "chat.completion",
#   "usage": {
#     "completion_tokens": 10,
#     "prompt_tokens": 10,
#     "total_tokens": 20
#   }
# }
