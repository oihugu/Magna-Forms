from flask import *
import random

db = {"Amazon" : ['pergunta1_Amazon', 'pergunta2_Amazon', 'pergunta3_Amazon'], "Google" : ['pergunta1_Google', 'pergunta2_Google', 'pergunta3_Google'], "Facebook" : ['pergunta1_Facebook', 'pergunta2_Facebook', 'pergunta3_Facebook'], 'Globo': ['pergunta1_Globo', 'pergunta2_Globo', 'pergunta3_Globo']}

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "GET":
        company = random.choice(list(db.keys()))     
    
    if request.method == "POST":
        company = request.form["company"]
        atende = request.form["atende"]
        if atende == 'yes':
            return redirect(url_for('company', company=company))
        else:
            return redirect(url_for('home'))

    return render_template("home.html", company=company)



@app.route("/company/<company>", methods=["GET", "POST"])
def company(company):
    if request.method == "POST":
        return "Obrigado por responder as perguntas!"

    return render_template("company.html", company=company, perguntas=enumerate(db[company]))

if __name__ == "__main__":
    app.run(debug = True)