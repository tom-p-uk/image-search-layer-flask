import datetime
import pytz
import requests

from db import db


class SearchModel(db.Model):
    __tablename__ = 'search'

    id = db.Column(db.Integer, primary_key=True)
    search_term = db.Column(db.String(80))
    searched_on = db.Column(db.Date)
    api_string = db.Column(db.String(200))

    def __init__(self, search_term, api_string):
        self.search_term = search_term
        self.searched_on = pytz.utc.localize(datetime.datetime.utcnow())
        self.api_string = api_string

    def json(self):
        print(self.searched_on)
        return {'search_term': self.search_term, 'searched_on': str(self.searched_on)}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def fetch_search_results(self):
        r = requests.get(self.api_string)
        items = list(r.json()['items'])

        return list(map(lambda x: {
                'url': x['link'],
                'snippet': x['snippet'],
                'thumnbail': x['image']['thumbnailLink'],
                'context': x['image']['contextLink']
            }, items))
