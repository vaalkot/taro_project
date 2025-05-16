from flask import Flask, render_template, jsonify, request
from data import db_session
from data.cards import Cards
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-card")
def get_card():
    spread = request.args.get("spread", "").lower()
    if not spread:
        return jsonify({"error": "Расклад не указан"})

    db_sess = db_session.create_session()
    cards = db_sess.query(Cards).filter(Cards.spread == spread).all()

    if not cards:
        return jsonify({"error": f"Нет карт для расклада '{spread}'"})

    card = random.choice(cards)
    return jsonify({
        "name": card.name,
        "description": card.description,
        "photo": card.photo
    })

if __name__ == "__main__":
    db_session.global_init("db/cards.db")
    app.run(debug=True)
