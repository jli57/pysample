import re

# replace keywords
def replace_text(txt, new_word = "GreenPark", words = ["coach", "superbowl", "playoff"]):
  for word in words:
    pattern = re.compile(word, re.IGNORECASE)
    new_txt = pattern.sub(new_word, txt)
  return new_txt
