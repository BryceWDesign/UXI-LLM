# data/preprocess.py

import re

def preprocess_text(text):
    """
    Basic text preprocessing: lowercase, remove special chars, normalize whitespace.
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
