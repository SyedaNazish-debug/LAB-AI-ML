import nltk
from nltk.corpus import treebank 

nltk.download('treebank')
print("Top 20 words:",treebank.words())
print("\n Total no.of words:",len(treebank.words()))
print("\n First sentence:",treebank.sents()[0])
print("pos tagged first sentence :",treebank.tagged_sents()[0])