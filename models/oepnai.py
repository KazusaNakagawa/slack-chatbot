import os
import openai
from dotenv import load_dotenv

load_dotenv()

class OpenAI:
    def __init__(self, model='gpt-4o-mini'):
        """OpenAI API を使用するためのクラス
         Args:
           model (str): 使用する言語モデルエンジン. デフォルトは gpt-4o-mini
        """
        self.model = model
        openai.api_key = os.getenv('OPENAI_API_KEY')

    def response_text(self, prompt: str, temperature=0.3) -> str:
        """OpenAI API にリクエストを送信し、返信を取得する
          Args:
            prompt (str): プロンプト
            temperature (float): 返信のランダム性を制御する. 値が大きいほどランダム性が高くなる

          Returns: 返信 (str)
        """
        completion = openai.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=temperature,
        )

        return completion.choices[0].message.content.strip()
