import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from prompt.instructions import SYSTEM_INSTRUCTIONS

USER_NAME = "user"
ASSISTANT_NAME = "assistant"

# 環境変数の読み込みとクライアントの初期化
load_dotenv()
client = OpenAI()

def main() -> None:
    st.title("Hello, World!")

if __name__ == "__main__":
    main()
