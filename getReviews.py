import requests

API_URL = "https://api-inference.huggingface.co/models/Iiro/bert_reviews"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def getReviews(reviews):
    try:
        # calculate the stars
        stars = requests.post(API_URL, headers=headers, json=reviews).json()
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
        maxVal = max(stars[i], key=lambda x:x['score'])
        star = int(maxVal['label'].split('_')[1]) + 1
        listOfReviews.append({'review': reviews[i],
                              'star': star})
    # return reviews and also the top words.
    res = {'reviews': listOfReviews}
    return res;