from transformers import pipeline
import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt")
abstractive_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def extractive_summary(text, num_sentences=3):
    sentences = sent_tokenize(text)
    return " ".join(sentences[:num_sentences])

def abstractive_summary(text):
    text = text.strip().replace("\n", " ")
    if len(text.split()) < 50:
        min_len, max_len = 10, 50
    else:
        min_len, max_len = 30, 130

    result = abstractive_pipeline(text, max_length=max_len, min_length=min_len, do_sample=False)
    return result[0]['summary_text']

def generate_summary(text, summary_type, size):
    if summary_type == "extractive":
        return extractive_summary(text, size)
    else:
        return abstractive_summary(text)
