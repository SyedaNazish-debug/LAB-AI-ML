import re
text="""I'm learning NLP!!! NLP is VERY useful in A I don't want unnecessary characters a = 5%
It's an interesting subject."""
print("Original Text:")
print(text)

text = text.lower()

contractions = {
    "i'm": "i am",
    "don't": "do not",
    "can't": "cannot",
    "it's":"it is",
    "isn't": "is not",
    "won't": "will not",
    "didn't": "did not"
}
for contraction, expanded in contractions.items():
     text = text.replace(contraction, expanded)

text = re.sub(r"[^a-z0-9\s]", "", text)
#4. Remove extra spaces
text = re.sub(r'\s+',"", text).strip()
print("\nNormalized Text:")
print(text)