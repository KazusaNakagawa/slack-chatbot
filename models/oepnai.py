import os
import openai

from dotenv import load_dotenv

load_dotenv()

# API トークンを設定する
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# OpenAI: Prompt params
ENGINE = 'text-davinci-003'

openai.api_key = OPENAI_API_KEY

class OpenAI:

  def __init__(self, engine=ENGINE):
     self.engine = engine

  def response_text(self, prompt):
      response = openai.Completion.create(
          engine=self.engine,
          prompt=prompt,
          max_tokens=1024,
          n=1,
          stop=None,
          temperature=0.7
      )
      return response.choices[0].text.strip()
