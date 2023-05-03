from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

def getReviews(reviews):
    MODEL_NAME = 'Iiro/bert_reviews';
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME);
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME);

    pipe = pipeline(
        'text-classification',
        model=model,
        tokenizer=tokenizer,
        device=model.device
    )

    prompt = reviews;
    res = pipe(prompt);

    return res