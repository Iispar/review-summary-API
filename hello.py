from flask import Flask
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

MODEL_NAME = 'Iiro/bert_reviews'

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

pipe = pipeline(
    'text-classification',
    model=model,
    tokenizer=tokenizer,
    device=model.device
)

prompt = ["this chainsaw sucks", "wow i love this item"]

output = pipe(prompt)

app = Flask(__name__)


@app.route('/')
def hello():
    return output