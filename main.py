from flask import Flask
from flask import request
from flask_restful import Resource, Api
from getReviews import getReviews

app = Flask('ReviewsAPI');
api = Api(app);

class Review(Resource):
    def get(self):
        reviews = request.json['reviews'];
        res = getReviews(reviews);
        print(res);
        return res;

api.add_resource(Review, '/')

if __name__ == '__main__':
    app.run();
