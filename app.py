from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():

    score = None
    level = None
    tree = None

    average_score = 75
    battle_message = ""
    progress_width = 10

    vehicle = "Bike"
    distance = ""
    electricity = ""

    if request.method == 'POST':

        vehicle = request.form['vehicle']
        distance = float(request.form['distance'])
        electricity = float(request.form['electricity'])

        vehicle_factor = {
            "Bike": 0.10,
            "Car": 0.25,
            "Bus": 0.05,
            "Train": 0.03
        }

        score = (
            distance * vehicle_factor[vehicle]
            + electricity * 0.20
        )

        # Better sustainability logic

        if score < 30:
            level = "Eco Champion 🌲"
            tree = "🌲"

        elif score < 70:
            level = "Great 🌳"
            tree = "🌳"

        elif score < 120:
            level = "Average 🌿"
            tree = "🌿"

        else:
            level = "Needs Improvement 🌱"
            tree = "🌱"


        average_score = 75

        if score < average_score:
            battle_message = "🎉 Great Job! You are greener than average students."
        else:
            battle_message = "⚠️ Your carbon footprint is higher than average students."
        progress_width = max(10, 100 - score)

    return render_template(
    "calculator.html",
    score=score,
    level=level,
    tree=tree,
    vehicle=vehicle,
    distance=distance,
    electricity=electricity,
    average_score=average_score,
    battle_message=battle_message,
    progress_width=progress_width
)



if __name__ == '__main__':
    app.run(debug=True)