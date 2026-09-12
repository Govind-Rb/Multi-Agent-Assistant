import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def get_model():
    model = ChatOpenAI(
        model="gpt-5.4-mini"
    )

    return model