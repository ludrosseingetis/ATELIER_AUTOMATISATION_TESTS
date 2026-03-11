from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)

@app.get("/")

def consignes():
     return render_template('consignes.html')
with app.app_context():
    storage.init_db()
     
@app.route("/dashboard")
def dashboard():
    # On récupère les 10 derniers runs depuis SQLite
    runs = storage.get_runs()
    return render_template('dashboard.html', runs=runs)

@app.route("/run")
def trigger_test():
    # Cette route permet de lancer le test via un bouton sur le dashboard
    from tester import runner
    runner.run_tests()
    return redirect(url_for('dashboard'))


if __name__ == "__main__":

    # utile en local uniquement

    app.run(host="0.0.0.0", port=5000, debug=True)
