from flask import render_template
from flask.views import MethodView
import gbmodel

class List(MethodView):
    def get(self):
        model = gbmodel.get_model()
        entries = model.select()
        return render_template('list.html', entries=entries)
