import os
import openai

from dotenv import load_dotenv

load_dotenv()


class OpenAI:

  def __init__(self, engine='text-davinci-003'):
      """OpenAI API を使用するためのクラス
       Args:
         engine (str): 使用する言語モデルエンジン. デフォルトは text-davinci-003
      """
      self.engine = engine
      # API トークンを設定する
      openai.api_key = os.getenv('OPENAI_API_KEY')

  def response_text(self, prompt: str, temperature=0.3) -> str:
      """OpenAI API にリクエストを送信し、返信を取得する
        Args:
          prompt (str): プロンプト
          temperature (float): 返信のランダム性を制御する. 値が大きいほどランダム性が高くなる

        Returns: 返信 (str)
      """
      response = openai.Completion.create(
          engine=self.engine,
          prompt=prompt,
          max_tokens=1024,
          n=1,
          stop=None,
          temperature=temperature,
      )
      return response.choices[0].text.strip()
