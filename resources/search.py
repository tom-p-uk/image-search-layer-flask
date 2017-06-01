from flask_restful import Resource, reqparse
from models.search import SearchModel


class Search(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('offset', type=int)

    def get(self, query):
        api_string = 'https://www.googleapis.com/customsearch/v1?searchType=image&num=10&'
        api_string += 'key=' + 'AIzaSyAX5iooHx6U2mhbsZN1TKer0hZkOBZMdRc' + '&cx=' + '012413247225941039823:5rf47ft6kfi' + '&q=' + query

        offset = Search.parser.parse_args()['offset']
        if offset > 0:
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
