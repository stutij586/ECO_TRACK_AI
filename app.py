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
    battle_color="#22c55e"

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


        student_scores = [
            45,
            60,
            80,
            95,
            55,
            70,
            65
        ]

        average_score = round(
            sum(student_scores)
            / len(student_scores),
            1
        )

        if score < average_score:
            battle_message = "🎉 Great Job! You are greener than average students."
            battle_color = "#22c55e"

        else:
            battle_message = "⚠️ Your carbon footprint is higher than average students."
            battle_color = "#ef4444"
        progress_width = max(
            5,
            min(
                100,
                (average_score / score) * 100
            )
        )
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
    progress_width=progress_width,
    battle_color=battle_color
)

@app.route('/eco-coach')
def eco_coach():

    tips = [

        "Use public transport whenever possible.",

        "Switch off unused lights and appliances.",

        "Carry a reusable water bottle.",

        "Plant more trees around your locality.",

        "Reduce plastic consumption.",

        "Prefer cycling or walking for short trips.",

        "Use LED bulbs to save electricity."

    ]

    return render_template(
        "eco_coach.html",
        tips=tips
    )

if __name__ == '__main__':
    app.run(debug=True)