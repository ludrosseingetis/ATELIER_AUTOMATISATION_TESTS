from flask import Flask, render_template, redirect, url_for
import storage # <--- NE PAS OUBLIER CETTE LIGNE
import os

app = Flask(__name__)

# Initialisation de la BDD au lancement
storage.init_db()

@app.route("/")
def index():
    return render_template('consignes.html')

@app.route("/dashboard")
def dashboard():
    # On récupère les 10 derniers runs depuis SQLite
    try:
        runs = storage.get_runs()
        return render_template('dashboard.html', runs=runs)
    except Exception as e:
        return f"Erreur avec la base de données : {e}"

@app.route("/run")
def trigger_test():
    # On importe le runner ici pour lancer le test
    try:
        from tester import runner
        runner.run_tests()
        return redirect(url_for('dashboard'))
    except Exception as e:
        return f"Erreur lors de l'exécution du test : {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
