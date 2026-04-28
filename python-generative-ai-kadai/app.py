import os
import requests
from dotenv import load_dotenv

# --- 初期設定 ---
load_dotenv()
API_KEY = os.getenv("API_KEY")

# 最も標準的な最新エンドポイント
# こちらも試す価値があります
ENDPOINT_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"
print("=== AIお悩み相談チャット（'終了'と入力すると終わります） ===")

# 会話履歴（最初のメッセージでカウンセラー設定を流し込む）
messages = [
    {"role": "user", "content": "あなたは親身な心理カウンセラーです。優しく丁寧な日本語で回答してください。"},
    {"role": "model", "content": "承知いたしました。私は心理カウンセラーとして、あなたの心に寄り添い、お話を伺います。"}
]

while True:
    user_input = input("あなた: ")
    if user_input == "終了":
        print("終了します。お大事に。")
        break
    if not user_input.strip(): continue

    messages.append({"role": "user", "content": user_input})

    try:
        # リクエストURLを作成
        request_url = f"{ENDPOINT_URL}?key={API_KEY}"
        
        # データ構造を整理
        data = {
            "contents": [{"role": m["role"], "parts": [{"text": m["content"]}]} for m in messages]
        }

        headers = {"Content-Type": "application/json"}
        response = requests.post(request_url, headers=headers, json=data)
        
        if response.status_code != 200:
            print(f"【サーバーからの回答】: {response.text}")
            response.raise_for_status()

        result = response.json()
        ai_response = result["candidates"][0]["content"]["parts"][0]["text"]
        
        print(f"AIカウンセラー: {ai_response}")
        
        # AIの回答を履歴に追加
        messages.append({"role": "model", "content": ai_response})

    except Exception as e:
        print(f"【エラー発生】: {e}")