import sys

print("PYTHON / NLP ENVIRONMENT TEST")

# Python
print("\nPython:")

print("Version:", sys.version)
print("Executable:", sys.executable)
# NLTK
try:
    import nltk
    print("\n✓ NLTK:", nltk.__version__)

except Exception as e:
    print("\n✗ NLTK ERROR:", e)
    # spaCy
try:
    import spacy
    print("✓ spaCy:", spacy.__version__)
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("This is a test sentence.")
    print("✓ spaCy English model loaded")
    print("Tokens:", [token.text for token in doc])
    
except Exception as e:
        print("✗ spaCy ERROR:", e)
        # Scikit-learn
try:
    import sklearn
    print("✓ Scikit-learn:", sklearn.__version__)
    
except Exception as e:
    print("✗ Scikit-learn ERROR:", e)
    # Gensim
try:
    import gensim
    print("✓ Gensim:", gensim.__version__)
except Exception as e:
    print("✗ Gensim ERROR:", e)
    # Contractions
try:
    import contractions
    print("✓ Contractions")
    text = "I can't believe it isn't working."
    print("Expanded:", contractions.fix(text))
    
except Exception as e:
    print("✗ Contractions ERROR:", e)
    # Transformers
try:
    import transformers
    print("✓ Transformers:", transformers.__version__)
except Exception as e:
    print("✗ Transformers RROR:", e)
    # Datasets
try:
    import datasets
    print("✓ Datasets:", datasets.__version__)
except Exception as e:
    print("✗ Datasets ERROR:", e)
    # Accelerate
try:
    import accelerate
    print("✓ Accelerate:", accelerate.__version__)
except Exception as e:
    print("✗ Accelerate ERROR:", e)
    # PyTorch
try:
        import torch
        print("✓ PyTorch:", torch.__version__)
        print("CUDA available:", torch.cuda.is_available())
except Exception as e:
    print("✗ PyT") 
