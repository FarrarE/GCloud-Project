"""
A recipe book flask app.
Copyright Ezra Farrar 2019
"""
import flask
from flask.views import MethodView

"""
Imported routes
"""
from index import Index
from add import Add
from list import List

app = flask.Flask(__name__)       # our Flask app

"""
Default path for landing page
Acts as a route for the other two pages.
"""
app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

"""
Path to recipe book add form page
Allows user to add new recipes
"""

app.add_url_rule('/add/',
                 view_func=Add.as_view('add'),
                 methods=['GET', 'POST'])

"""
Path to recipe book list page
Displays all stored recipes
"""
app.add_url_rule('/list/',
                view_func=List.as_view('list'),
                methods=['GET', 'POST'])

                 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
