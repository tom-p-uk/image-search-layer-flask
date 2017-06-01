from flask_restful import Resource

from models.search import SearchModel


class SearchHistory(Resource):
    def get(self):
        return {'search_history': list(map(lambda x: x.json(), SearchModel.query.all()))}
