import nltk 
from nltk.tokenize import sent_tokenize

text="""Python is a popular programming language.
It is widely used in NLP.
NLTK provide many useful tools for nlp.
sentence segmentation is an important pre-processing step."""

print("Sentence segmentation:")
print("original text:",text)
sentence= sent_tokenize(text)

print("\n Segmented sentence :")

for i , sentence in enumerate(sentence,start=1):
    print(f"sentence {i}: {sentence}")

print("\n Total no.of sentence:",len(sentence))

print("success")