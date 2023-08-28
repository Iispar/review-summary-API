from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np;

def getTopWords(reviews):
    pos = [];
    neg = [];
    # loop reviews and sor byt rating 1-2 negative 4-5 positive.
    for i in range(len(reviews)):
        rating = int(reviews[i]['star']);
        if rating > 3:
            pos.append(reviews[i]['review']);
        elif rating < 3:
            neg.append(reviews[i]['review']);
    try:
        # calculate the positive and negative words.
        negWords = get_tfidf_top_features(neg, 10);
        posWords = get_tfidf_top_features(pos, 10);
    # not enought words so we just return empty.
    except:
        return {'topNeg': ["not enough words"], 'topPos': ["not enough words"]}
    # return the words.
    return {'topNeg': negWords, 'topPos': posWords}


def get_tfidf_top_features(documents,n_top=5):
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