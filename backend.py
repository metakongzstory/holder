from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import openai

openai.api_key = "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"

def chat(messages):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    resp_dict = response.to_dict_recursive()
    assistant_turn = resp_dict['choices'][0]['message']
    return assistant_turn # {"role": "assistant", "content": "blahblahblah"}

messages = [{"role": "user", "content": "당신은 누구십니까"}]

print(chat(messages=messages))
