from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

def getReviews(reviews):
    try:
        MODEL_NAME = 'Iiro/bert_reviews';
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME);
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME);
    except:
        raise Exception('couldn\' find model')

    pipe = pipeline(
        'text-classification',
        model=model,
        tokenizer=tokenizer,
        device=model.device
    )

    prompt = reviews;

    try:
        res = pipe(prompt);
    except:
        raise Exception('Pipeline Failed')

    return res