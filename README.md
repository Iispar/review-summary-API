# review-summary-backend

Backend for the reviews application. Other repositories:
<br />
[frontend](https://github.com/Iispar/reviews-frontend)
<br />
[backend](https://github.com/Iispar/reviews-backend)

## About this project

This is the API for my reviews application. It includes the training of my two models and a small Flask API that I created so that I can call the model from the backend. The API also includes top word calculation with TF-IDF and returns the top most important words / word pairs.

**!! For a detailed look at the whole project and also this API please refer to the document in the frontend github that was created for the college course.!!**

## Background

The application uses natural language processing to process reviews and rate them on a scale from 1-5 as a sentiment to the review. I created two different models one that you can find from the colab file [model.ipynb](https://github.com/Iispar/review-summary-API/blob/main/model.ipynb) that is a basic feed forward model that I created myself from start to end and the other one is a finetuned BERT model that you can find in [BERT-finetuned-model](https://github.com/Iispar/review-summary-API/blob/main/BERT-finetuned-model.ipynb). The finetuned BERT model achieved naturally better results so it is the one that is used in the backend.

In addition to this, I also used some basic data processing and TF-IDF to calculate the top words/word pairs with the most important to the reviews. 

Then I created a really simple API in Flask so that I can easily make a call to an endpoint and get to use the model and the top word calculations.

## Prerequisites 

You will need to have Python installed. You will need the API key for the huggingface model from me. Please contact me so I can give you this and all other secret keys with instructions on using them.

## Using

The API might need a bit of time to wake up so don't mind if the first rate calls don't work, just try again.

### Docker
If you want to use Docker you just need to have docker installed. Then run the following in the folder that has the
dockerfile  ```docker build --tag api .```. And after this just run ```docker run -p 8080:5000 api``` and the application
should start and be accessable from http://127.0.0.1:8080

### Command line

You can also run the application as follows: <br />
Before using you need to install the following with pip in the command line:
```
pip3 install flask
pip3 install flask-restful
pip3 install scikit-learn
pip3 install requests
pip3 install python-dotenv
```
The usage of the app after this should be really simple. Just clone the repository and run the app.py file or from the command line run ```python3 -m flask run``` and it opens the API locally. There is a test file test.rest that can be used to make a API call to the API. Just make sure the address is correct!

## Technologies

The model uses HuggingFaces dataset [amazon-reviews-multi](https://huggingface.co/datasets/amazon_reviews_multi/viewer/en/train) for training. The training is done in Python with the help of a few libraries like sklearn, torch, transformers, numpy and optuna. For the API I used Python with Flask. To know more about the training please refer to the document in the frontend repository.

