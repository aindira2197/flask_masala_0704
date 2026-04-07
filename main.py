from flask import Flask, render_template

app = Flask(__name__)

roy = ["Lobar", "Indira", "Shohruza", "Shakarjon", "Durumboy"]

@app.route("/")
def home():
    return render_template("index.html", roy=roy)

@app.route('/roy/<int:indeks>')
def element(indeks):
    if 0<= indeks < len(roy):
        el = roy[indeks]
    else:
        el = 'Error'
    
    return render_template("elementlar.html", el=el)

@app.route('/roy/qidiruv/<name>')
def find(name):
    if name.lower() in list(map(lambda el: el.lower(), roy)):
        res = f'Topildi: {name.capitalize()}'
    else:
        res = f'Topilmadi: {name.capitalize()}'
    
    return render_template('find.html', res=res)

if __name__ == "__main__":
    app.run(debug=True)
