from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import numpy as np;
from sklearn.feature_extraction.text import TfidfVectorizer

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
        # calculate the top words.
        topWords = getTopWords(stars, reviews);
    except:
        raise Exception('Top word calculation failed')
    
    try:
        # create a response from the data
        res = createRes(reviews, stars, topWords);
    except:
        raise Exception('Response creation failed')

    return res

def getTopWords(stars, reviews):
    pos = [];
    neg = [];
    # loop reviews and sor byt rating 1-2 negative 4-5 positive.
    for i in range(len(reviews)):
        label = int(stars[i]['label'].split('_')[1]) + 1
        if label > 3:
            pos.append(reviews[i]);
        elif label < 3:
            neg.append(reviews[i]);

    try:
        # calculate the positive and negative words.
        negWords = get_tfidf_top_features(neg, 20);
        posWords = get_tfidf_top_features(pos, 20);
    except:
        raise Exception('Failure with tfidf')
    # return the words.
    return {'negWords': negWords, 'posWords': posWords}

def get_tfidf_top_features(documents,n_top=10):
  # load the vectorizer.
  vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,  stop_words='english')
  # fit the vectorizer with our reviews
  tfidf = vectorizer.fit_transform(documents)
  # get the words values and sort them to descending 
  importance = np.argsort(np.asarray(tfidf.sum(axis=0)).ravel())[::-1]
  # array with names and values.
  tfidf_feature_names = np.array(vectorizer.get_feature_names_out());
  # take the first n most important words. get name from the list and return as list.
  # to list because json needs it be in a list and no np array.
  return tfidf_feature_names[importance[:n_top]].tolist();


def createRes(reviews, stars, topWords):
    listOfReviews = [];
    # loop all reviews and create a list of json objects with
    # the rating and its stars.
    for i in range(len(reviews)):
        listOfReviews.append({'review': reviews[i],
                              'stars': stars[i]})
    # return reviews and also the top words.
    res = {'reviews': listOfReviews,
           'topNeg': topWords['negWords'],
           'topPos': topWords['posWords']}

    return res;