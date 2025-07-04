from openai import OpenAI

from helpers.tool_box import read_config

def api_call(message=None):
    client = OpenAI(
      api_key= read_config()["API_KEY"]["API_KEY"],
        )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        temperature=0.7,
        seed=42,
        max_tokens=1000,
        messages=message
    )

    return completion.choices[0].message.content

def api_call_json(message=None):
    client = OpenAI(
        api_key=read_config()["API_KEY"]["API_KEY"],
    )

    completion = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        temperature=0.7,
        seed=42,
        max_tokens=10000,
        messages=message,
        response_format={"type": "json_object"}
    )

    return completion.choices[0].message.content