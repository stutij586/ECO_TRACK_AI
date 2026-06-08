from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():

    score = None
    level = None

    if request.method == 'POST':

        vehicle = request.form['vehicle']
        distance = float(request.form['distance'])
        electricity = float(request.form['electricity'])

        vehicle_factor = {
            "Bike": 0.1,
            "Car": 0.25,
            "Bus": 0.05,
            "Train": 0.03
        }

        score = (
            distance * vehicle_factor[vehicle]
            + electricity * 0.2
        )

        if score < 50:
            level = "Green 🌱"

        elif score < 100:
            level = "Moderate 🌿"

        else:
            level = "High 🔥"

    return render_template(
        "calculator.html",
        score=score,
        level=level
    )

if __name__ == '__main__':
    app.run(debug=True)