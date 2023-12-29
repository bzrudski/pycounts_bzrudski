from collections import Counter
from string import punctuation

def load_text(input_file: str) -> str:
    """Load text from a text file and return it as a string."""
    with open(input_file, "r") as file:
        text = file.read()
    return text

def clean_text(text: str) -> str:
    """Lowercase and remove punctuation from a string."""
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text

def count_words(input_file: str) -> Counter:
    """Count unique words in a text file."""
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)