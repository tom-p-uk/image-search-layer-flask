# Image Search Abstraction Layer

A URL shortening microservice built using Python. I originally made this with Node, Express and MongoDB as part of Free Code Camp's backend challenges, but rebuilt it to get some more practice with Python. The original repo can be found [here](https://github.com/tom-p-uk/image-search-abstraction-layer).

### User Stories:

1. I can get the image URLs, alt text and page urls for a set of images relating to a given search string.
2. I can paginate through the responses by adding a ?offset=2 parameter to the URL.
3. I can get a list of the most recently submitted search strings.

### Technology Used:

* Python 3.6
* Flask
* Flask-RESTful
* Flask SQLAlchemy

### Heroku Demo:

Make GET requests to https://tom-p-uk-image-search-flask.herokuapp.com/api/imagesearch/<searchterm> to receive a JSON response.
Paginate through the results by passing in a query string of offset followed by a positive integer. E.g., https://tom-p-uk-image-search-flask.herokuapp.com/api/imagesearch/<searchterm>?offset=5 .
Make a GET request to https://tom-p-uk-image-search-flask.herokuapp.com/api/searchhistory to view past searches.
