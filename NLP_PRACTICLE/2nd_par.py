import nltk
from nltk.corpus import brown
from nltk.probability import FreqDist

nltk.download('brown')
print("Brown corpus categories:",brown.categories())
print("\n First 20 words:",brown.words()[:20])
print("\n Total number of words:", len(brown.words()))

fdist= FreqDist(brown.words())

print("\n 10 Most common words:",fdist.most_common(10))
