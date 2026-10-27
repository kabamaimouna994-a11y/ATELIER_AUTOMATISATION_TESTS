# ---------------------------------------------------------------
#  Mon site Web Flask — Maïmouna Kaba
# ---------------------------------------------------------------

from flask import Flask, render_template, request, jsonify
import sqlite3
from tester.runner import execute_run
from storage import save_run, list_runs

app = Flask(__name__)

# --- Routes des exercices précédents ---

@app.get("/")
def accueil():
    return render_template("accueil.html")

@app.get("/consignes")
def consignes():
    return render_template('consignes.html')

@app.get("/presentation")
def presentation():
    return render_template(
        "presentation.html", 
        prenom="Maïmouna", 
        nom="KABA",
        loisirs=["Natation", "Musique", "Code"]
    )

@app.get("/loisirs")
def loisirs():
    return "Je m'aime la natation."

@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    return render_template("bonjour.html", prenom=prenom)

@app.get("/calcul")
def calcul():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    op = request.args.get("op", "plus")
    
    if op == "fois":
        resultat = a * b
        symbole = "×"
    elif op == "moins":
        resultat = a - b
        symbole = "-"
    else:
        resultat = a + b
        symbole = "+"
        
    return f"{a} {symbole} {b} = {resultat}"

@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")

@app.route("/salut", methods=["GET", "POST"])
def salut():
    if request.method == "POST":
        prenom = request.form.get("prenom", "inconnu")
        ville = request.form.get("ville", "nulle part")
        couleur = request.form.get("couleur", "black")
    else:
        prenom = request.args.get("prenom", "inconnu")
        ville = request.args.get("ville", "nulle part")
        couleur = request.args.get("couleur", "black")
        
    return f'<h1 style="color: {couleur};">Bonjour {prenom}, qui vient de {ville} !</h1> (reçu en {request.method})'


# --- Nouvelles routes : Atelier Testing as Code & API Monitoring ---

@app.get("/run")
def trigger_run():
    """Exécute un run de tests sur l'API Agify et sauvegarde en SQLite"""
    run_data = execute_run()
    save_run(run_data)
    return jsonify({"message": "Run executed successfully", "data": run_data})

@app.get("/dashboard")
def dashboard():
    """Affiche le tableau de bord des performances et de l'historique"""
    runs = list_runs(10)
    latest_run = runs[0] if runs else None
    return render_template("dashboard.html", runs=runs, latest=latest_run)

@app.get("/health")
def health():
    """Endpoint de santé (Bonus) exposant l'état du dernier run au format JSON"""
    runs = list_runs(1)
    if not runs:
        return jsonify({"status": "WARNING", "message": "No runs recorded yet"}), 200
    
    latest = runs[0]
    status = "OK" if latest["failed"] == 0 and latest["error_rate"] == 0 else "DEGRADED"
    return jsonify({
        "status": status,
        "last_timestamp": latest["timestamp"],
        "error_rate": latest["error_rate"],
        "avg_latency_ms": latest["avg_latency"]
    }), 200


# ---------------------------------------------------------------
#  Lancement en local
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
