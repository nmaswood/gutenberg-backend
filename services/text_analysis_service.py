import requests
import time
import logging
from transformers import DistilBertTokenizer

# Initialize the tokenizer for the model
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

logging.basicConfig(level=logging.DEBUG)

HUGGING_FACE_TOKEN = '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'

API_URL = "https://api-inference.huggingface.co/models/"

HEADERS = {"Authorization": "Bearer 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"}

def query_huggingface(model_name, payload):
    while True:
        try:
            response = requests.post(API_URL + model_name, headers=HEADERS, json=payload)
            result = response.json()
            
            # If the model is still loading, retry after the estimated time
            if 'error' in result and 'currently loading' in result['error']:
                estimated_time = result.get('estimated_time', 10)  # Default to 10 seconds if not provided
                print(f"Model is loading, retrying after {estimated_time} seconds...")
                time.sleep(estimated_time)
            else:
                return result
        except Exception as e:
            print("Error querying Hugging Face:", str(e))
            return {"error": str(e)}

def identify_characters(text):
    model_name = "dbmdz/bert-large-cased-finetuned-conll03-english"
    payload = {"inputs": text}
    response = query_huggingface(model_name, payload)
    return response

def detect_language(text):
    model_name = "papluca/xlm-roberta-base-language-detection"
    payload = {"inputs": text}
    response = query_huggingface(model_name, payload)
    return response

def truncate_text(text, max_length=512):
    tokens = tokenizer.encode(text, truncation=True, max_length=max_length, return_tensors='pt')
    truncated_text = tokenizer.decode(tokens[0], skip_special_tokens=True)
    return truncated_text

def sentiment_analysis(text):
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    truncated_text = truncate_text(text)  # Ensure the text is within limits
    payload = {"inputs": truncated_text}
    response = query_huggingface(model_name, payload)
    return response

def summarize_text(text):
    model_name = "facebook/bart-large-cnn"
    # Truncate text if necessary
    truncated_text = truncate_text(text)
    payload = {"inputs": truncated_text}
    logging.debug(f"Summarize Text payload: {payload}")
    response = query_huggingface(model_name, payload)
    return response

