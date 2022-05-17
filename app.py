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

        soorthuis1 = None
        soorthuis2 = None
        soorthuis3 = None

        selected1 = None
        selected2 = None
        selected3 = None
        selected4 = None
        selected5 = None
        selected6 = None
        selected7 = None
        selected8 = None
        selected9 = None
        selected10 = None

        if soorthuis == 'vrijstaand':
            soorthuis1 = 'selected'

        elif soorthuis == 'halfvrijstaand':
            soorthuis2 = 'selected'

        elif soorthuis == 'tussenliggend':
            soorthuis3 = 'selected'

        if int(aantalbewoners) == 1:
            selected1 = 'selected'

        elif int(aantalbewoners) == 2:
            selected2 = 'selected'

        elif int(aantalbewoners) == 3:
            selected3 = 'selected'

        elif int(aantalbewoners) == 4:
            selected4 = 'selected'

        elif int(aantalbewoners) == 5:
            selected5 = 'selected'

        elif int(aantalbewoners) == 6:
            selected6 = 'selected'

        elif int(aantalbewoners) == 7:
            selected7 = 'selected'

        elif int(aantalbewoners) == 8:
            selected8 = 'selected'

        elif int(aantalbewoners) == 9:
            selected9 = 'selected'

        elif int(aantalbewoners) == 10:
            selected10 = 'selected'

        return render_template("index.html",
                               electriciteitsverbruik=electriciteitsverbruik,
                               electriciteitteruggeleverd=electriciteitteruggeleverd,
                               gasverbruik=gasverbruik,
                               soorthuis=soorthuis,
                               volumehuis=volumehuis,
                               aantalbewoners=aantalbewoners,
                               selected1=selected1,
                               selected2=selected2,
                               selected3=selected3,
                               selected4=selected4,
                               selected5=selected5,
                               selected6=selected6,
                               selected7=selected7,
                               selected8=selected8,
                               selected9=selected9,
                               selected10=selected10,
                               soorthuis1=soorthuis1,
                               soorthuis2=soorthuis2,
                               soorthuis3=soorthuis3)

    return render_template("index.html",
                               electriciteitsverbruik=electriciteitsverbruik,
                               electriciteitteruggeleverd=electriciteitteruggeleverd,
                               gasverbruik=gasverbruik,
                               volumehuis=volumehuis,
                               )


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)