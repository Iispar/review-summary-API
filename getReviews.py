from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

def getReviews(reviews):
    try:
        # load the model
        MODEL_NAME = 'Iiro/bert_reviews';
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME);
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME);
    except:
        raise Exception('couldn\' find model')

    # set the pipeline
    pipe = pipeline(
        'text-classification',
        model=model,
        tokenizer=tokenizer,
        device=model.device
    )

    # get reviews.
    prompt = reviews;

    try:
        # calculate the stars
        stars = pipe(prompt);
    except:
        raise Exception('Pipeline Failed')
    
    try:
        # create a response from the data
        res = createRes(reviews, stars);
    except:
        raise Exception('Response creation failed')

    return res

def createRes(reviews, stars):
    listOfReviews = [];
    # loop all reviews and create a list of json objects with
    # the rating and its stars.
    for i in range(len(reviews)):
        star = int(stars[i]['label'].split('_')[1]) + 1
        listOfReviews.append({'review': reviews[i],
                              'star': star})
    # return reviews and also the top words.
    res = {'reviews': listOfReviews}
    return res;