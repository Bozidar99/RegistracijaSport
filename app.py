from flask import Flask, render_template,request,redirect
from cs50 import SQL


app = Flask(__name__)

db = SQL("sqlite:///spisak.db")



SPORTOVI = [
    "FUDBAL",
    "KOSARKA",
    "RUKOMET",
    "ODBOJKA",
    "TENIS",
    "VATERPOLO"
]


@app.route("/")
def index():
    return render_template("index.html", sport=SPORTOVI)

@app.route("/izbrisi", methods = ["POST"])
def izbrisi():
    
    id  = request.form.get("id")
    print("id za brisanje:", id)
    if id:
        db.execute("DELETE FROM spisak WHERE id = ?", id)
    return redirect("/spisak")

@app.route("/registar", methods=["POST"])
def registar():
    
    ime = request.form.get("ime")
    if not ime:
        return render_template("error.html", message = "Nema imena")
    
    prezime = request.form.get("prezime")
    if not prezime:
        return render_template("error.html", message = "Nema prezimena")

    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Nema sporta")
    if sport not in SPORTOVI:
        return render_template("error.html", message="Ne spada u sportove")
    

    db.execute("INSERT INTO spisak(ime, prezime, sport) VALUES(?, ?, ?)", ime, prezime, sport)


    return redirect("/spisak")

@app.route("/spisak")
def spisak():
    spisak = db.execute("SELECT * FROM spisak")
    return render_template("spisak.html", spisak = spisak)

