from flask import (Flask, render_template, request, redirect, url_for)

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/energielabel", methods=["GET", "POST"])
def energielabel():

    electriciteitsverbruik = 1770
    electriciteitteruggeleverd = 3480
    gasverbruik = 1730
    volumehuis = 800

    if request.method == "POST":

        electriciteitsverbruik = request.form.get("electriciteitsverbruik")
        electriciteitteruggeleverd = request.form.get("electriciteitteruggeleverd")
        gasverbruik = request.form.get("gasverbruik")
        soorthuis = request.form.get("soorthuis")
        volumehuis = request.form.get("volumehuis")
        aantalbewoners = request.form.get("aantalbewoners")

        return render_template("index.html",
                               electriciteitsverbruik=electriciteitsverbruik,
                               electriciteitteruggeleverd=electriciteitteruggeleverd,
                               gasverbruik=gasverbruik,
                               soorthuis=soorthuis,
                               volumehuis=volumehuis,
                               aantalbewoners=aantalbewoners)

    return render_template("index.html",
                               electriciteitsverbruik=electriciteitsverbruik,
                               electriciteitteruggeleverd=electriciteitteruggeleverd,
                               gasverbruik=gasverbruik,
                               volumehuis=volumehuis,
                               )


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)