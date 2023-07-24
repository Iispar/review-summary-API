from flask import Flask
from flask import request
from flask_restful import Resource, Api

from getReviews import getReviews

app = Flask('ReviewsAPI');
api = Api(app);

class Review(Resource):
    def post(self):
        try:
            # get reviews from the call. If no reviews then return 400.
            reviews = request.json['reviews'];
        except:
            return 'bad request', 400;
        try:
            # get ratings for reviews and also most common words.
            res = getReviews(reviews);
        except:
            return 'Fail whilst calculating reviews', 404;
        return res;
        

api.add_resource(Review, '/rate')

if __name__ == '__main__':
    app.run();
