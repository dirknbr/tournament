
from vertexai.preview.generative_models import GenerativeModel
import json
import re

gemini_pro_model = GenerativeModel("gemini-1.5-flash") 

pattern = r"\b\d{4}\b"

class Bot:
  def __init__(self, playerid):
    self.name = ''
    self.playerid = playerid

  def play(self, game_state=None):
    if len(game_state[0]) == 0:
      return '0123'
    else:
      state_as_json = json.dumps(game_state[self.playerid])
      prompt = "You have to guess a 4 digit pin (0-9) and your log of guesses and bulls and cows is " +  state_as_json + ". Explain your answer but the last word needs to be the next guess."
      # print(prompt)
      model_response = gemini_pro_model.generate_content(prompt)
      text = model_response.candidates[0].content.parts[0].text
      matches = re.findall(pattern, text)
      guess = matches[-1]
      # print(guess)
      return guess
