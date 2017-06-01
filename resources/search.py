from flask_restful import Resource, reqparse
from models.search import SearchModel
import os


class Search(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('offset', type=int)

    def get(self, query):
        api_string = 'https://www.googleapis.com/customsearch/v1?searchType=image&num=10&'
        api_string += 'key=' + os.environ['CSE_API_KEY'] + '&cx=' + os.environ['CSE_ID'] + '&q=' + query

        offset = Search.parser.parse_args()['offset']

        if offset and offset > 0:
            api_string += '&start=' + str(offset)

        search = SearchModel(query, api_string)

        try:
            search.save_to_db()
        except:
            return {'error': 'Search could not be saved to the db'}

        try:
            results = search.fetch_search_results() or []
        except:
            return {'error': 'Search results could not be returned'}

        return {'results': results}
