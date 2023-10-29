from flask import Flask
from flask import request
from flask_restful import Resource, Api

from getReviews import getReviews
from getTopWords import getTopWords

app = Flask('ReviewsAPI');
api = Api(app);

class Review(Resource):
    def post(self):
        try:
            # get reviews from the call. If no reviews then return 400.
            reviews = request.json['reviews'];
        except:
            return 'bad request', 400;

        
        # get ratings for reviews and also most common words.
        res = getReviews(reviews);

        return res;
        

class Rate(Resource):
    def post(self):
        try:
            # get reviews from the call. If no reviews return 400.
            reviews = request.json['reviews'];
        except:
            return 'bad request', 400;

            # get pos and neg reviews as res.
        res = getTopWords(reviews);
        return res;

api.add_resource(Review, '/rate')
api.add_resource(Rate, '/getTop')

if __name__ == '__main__':
    app.run(port="5000");
