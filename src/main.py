import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from prompt.instructions import SYSTEM_INSTRUCTIONS

# 環境変数の読み込みとクライアントの初期化
load_dotenv()
client = OpenAI()

def main() -> None:
    st.title("AI Workflow Demo")
    st.write("調べたいトピックを入力してください。")

    # ユーザー入力
    query = st.text_input("トピックを入力")

    # 情報収集ボタン
    if st.button("情報収集開始"):
        if query:
            st.write(f"情報収集中: {query}")
            # 情報収集と要約のロジック
            try:
                # Web情報収集のダミーデータ
                collected_data = "ここに収集した情報が入ります。"

                # OpenAI APIを使用して要約
                response = client.chat.completions.create(
                    messages=[{
                        "role": "user",
                        "content": f"{SYSTEM_INSTRUCTIONS}\n\n{collected_data}",
                    }],
                    model="gpt-4o-mini",
                )
                summary = response.choices[0].message.content

                # 結果の表示
                st.write("要約:")
                st.write(summary)
                st.write("参照リンク:")
                st.write("- [Example Link](https://example.com)")
            except Exception as e:
                st.write("エラーが発生しました:", e)
        else:
            st.write("トピックを入力してください。")

if __name__ == "__main__":
    main()
