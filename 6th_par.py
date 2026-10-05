import re

text="""NLP is useful in AI.
python is used for NLP.
My phone Number is 123-456-7890.
My email is student@gmail.com."""

text1="Hello!!!! Welcome to NLP @ 2026"

words=re.findall(r'\b\w+\b',text)
print("words:",words)

numbers=re.findall(r'\d{3}-\d{3}-\d{4}',text)
print("numbers:",numbers)

email=re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',text)
print("email:",email)

vowels=re.findall(r'[aeiouAEIOU]',text)
print("vowels:",vowels)

disjunction=re.findall(r'Python|NLP|AI',text)
print("disjunction:",disjunction)

repeat=re.findall(r'\d{10}',text)
print("repeat:",repeat)

clean_text=re.sub(r'[^a-zA-Z0-9\s]','',text1)
print("clean_text:",clean_text)