import nltk
from nltk.tokenize import sent_tokenize,word_tokenize

text="""Natural language processing is an important area of AI.
it helps machines / computer understand human language.
NLP is used in many chatbots, translation and text classification."""

sentence= sent_tokenize(text)

print("sentence in enumerate(sentence):")
for i, sent in enumerate(sentence):
    print(f"{i}: {sent}")
    
print("\n word Tokenization:")
for i, word in enumerate(word_tokenize(text)):
    print(f"{i}: {word}")