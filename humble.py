import os
import random
from tinydb import TinyDB, Query
from flask import render_template, Flask

app = Flask(__name__)
path = os.getenv("TINY_DB_PATH")
db = TinyDB(path)
recipes = db.all()
random_index = random.randint(0, len(recipes) - 1)
recipe = recipes[random_index]
print(recipe)


@app.route("/")
def root(recipe=recipe):
    return render_template("index.html", recipe=recipe)

