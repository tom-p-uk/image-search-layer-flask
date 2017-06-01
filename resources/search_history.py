from flask_restful import Resource

from models.search import SearchModel


class SearchHistory(Resource):
    def get(self):
        all_searches = SearchModel.query.all()
        all_searches = list(map(lambda x: x.json(), all_searches))
        all_searches_descending = list(reversed(all_searches))
        return {'search_history': all_searches_descending}
