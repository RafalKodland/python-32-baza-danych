# Import
from flask import Flask, render_template,request, redirect
# Importowanie biblioteki bazy danych
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Podłączanie SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creating a DB
db = SQLAlchemy(app)

#Zadanie nr 1. Utwórz tabelę DB
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Card id={self.id}>"

# Uruchamianie strony z treścią
@app.route('/')
def index():
    # Wyświetlanie obiektów Bazy
    # Assignment #2. Display the objects from the DB in index.html
    cards = Card.query.order_by(Card.id).all()
    print(cards)

    return render_template('index.html',
                           #karty = cards
                           cards=cards
                           )

# Uruchomienie strony z kartą
@app.route('/card/<int:id>')
def card(id):
    #Zadanie #2. Wyświetl właściwą kartę według jej identyfikatora
    card = Card.query.get(id)

    return render_template('card.html', card=card)

# Uruchomienie strony i utworzenie karty
@app.route('/create')
def create():
    return render_template('create_card.html')

# Formularz karty
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        #Zadanie #2. Stwórz sposób przechowywania danych w bazie danych
        
        card = Card(title=title, subtitle=subtitle, text=text)
        db.session.add(card)
        db.session.commit()


        return redirect('/')
    else:
        return redirect('/create')


if __name__ == "__main__":
    app.run(debug=True)