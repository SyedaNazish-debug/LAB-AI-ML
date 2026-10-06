
import re
text = """NLP IS AMAZING!!!
I can't wait to learn it."""
print("Original:")
print(text)

text = text.lower()

text = text.replace("can't", "cannot")

text =re.sub(r"[^a-z0-9\s]", ' ', text)

text = re.sub(r'\s+','', text).strip()
print("inafter Preprocessing:")
print(text)
