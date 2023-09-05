# review-summary-backend

This is the API for my reviews application. It includes the training of my two models and the small Flask API that I created so that I can call the model from the backend. The API also includes top word calculation with TF-IDF and returns the top most imiportant words.

## !!

If you would like to know more about the project for example training, why I made choises I made ie. why finetuned BERT or python for this or why TF-IDF. Please check the document that I made for the course in the frontend of this application (THIS IS COMING LATER). Here I tell about the API and model in short.

## Background

The application uses natural language processing to process reviews and rate them on a scale from 1-5 as an sentiment to the review. I created two different models one that you can find from the colab file [model.ipynb](https://github.com/Iispar/review-summary-API/blob/main/model.ipynb) that is a basic model that I created myself from start to end and the other one is a finetuned BERT model that you can find in [BERT-finetuned-model](https://github.com/Iispar/review-summary-API/blob/main/BERT-finetuned-model.ipynb). The finetuned BERT model achieved naturally better results so it is the one that is used in the backend.

In addition to this I also used some basic data processing and TF-IDF to calculate the top words with most importace to the reviews. 

Then I created a really simple API in Flask so that I can easily make a call to an endpoint and get to use the model.

## Technologies

The model uses HuggingFaces dataset [amazon-reviews-multi](https://huggingface.co/datasets/amazon_reviews_multi/viewer/en/train) for training. The training is done in Python with the help of a few libraries like sklearn, torch, transformers, numpy and optuna. For the API I used Python with Flask. To know more about the training please refer to the document (COMING SOON).

## Using
There will be a dockerfile later here but currently you can run the application as follows: <br />
Before using you need to install the following with pip in the command line:
```
pip install flask
pip install flask-restful
pip install scikit-learn
pip install requests
pip install python-dotenv
```
And you will need the API key for the huggingface model from me. Please contact me so I can give you this and all other secret keys with instructions on using them.
The usage of the app after this should be really simple. Just clone the repository and run the app.py file or from the command line run ```flask run``` and it opens the API locally. There is a test file test.rest that can be used to make a API call to the API. Just make sure the address is correct!
