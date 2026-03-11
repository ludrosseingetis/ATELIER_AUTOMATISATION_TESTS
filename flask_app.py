from flask import Flask, render_template, redirect, url_for
import storage
import os

app = Flask(__name__)

# Assure-toi que la BDD est initialisée au démarrage
with app.app_context():
    storage.init_db()

@app.route("/")
def index():
    # On redirige l'accueil vers le dashboard pour plus de clarté
    return redirect(url_for('dashboard'))

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
    app.run(debug=True)
