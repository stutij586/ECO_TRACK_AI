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
    badge = None

    monthly_co2=0
    cleaner_percent=0

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

        # Sustainability Badge

        if score < 30:
            badge = "🏅 Gold Eco Champion"

        elif score < 70:
            badge = "🥈 Silver Green Warrior"

        elif score < 120:
            badge = "🥉 Bronze Eco Learner"

        else:
            badge = "🌱 Beginner Badge"

        # Sustainability Impact Summary

        monthly_co2 = round(score, 1)

        cleaner_percent = round(
            max(
                0,
                ((average_score - score) / average_score) * 100
            ),
            1
        )


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
    badge=badge,
    vehicle=vehicle,
    distance=distance,
    electricity=electricity,
    average_score=average_score,
    battle_message=battle_message,
    progress_width=progress_width,
    battle_color=battle_color,
    monthly_co2=monthly_co2,
    cleaner_percent=cleaner_percent
)

@app.route('/eco-coach')
def eco_coach():

    score = request.args.get(
        "score",
        default=50,
        type=float
    )

    if score < 30:

        tips = [

            "🌟 Excellent work! Maintain your eco-friendly lifestyle.",

            "🚲 Continue using sustainable transport.",

            "🌳 Encourage friends to reduce their footprint.",

            "♻️ Keep recycling and reducing waste."

        ]

    elif score < 70:

        tips = [

            "🚶 Walk for short distances whenever possible.",

            "💡 Switch to LED lighting.",

            "🚰 Reduce water wastage.",

            "♻️ Increase recycling habits."

        ]

    elif score < 120:

        tips = [

            "⚠️ Your footprint is moderate.",

            "🚌 Use public transport more often.",

            "🔌 Reduce unnecessary electricity usage.",

            "🌱 Try carpooling or cycling."

        ]

    else:

        tips = [

            "🚨 High carbon footprint detected.",

            "🚗 Reduce personal vehicle usage.",

            "⚡ Cut electricity consumption significantly.",

            "🌳 Plant trees and offset emissions.",

            "♻️ Adopt sustainable daily habits."

        ]

    return render_template(
        "eco_coach.html",
        tips=tips,
        score=score
    )

if __name__ == '__main__':
    app.run(debug=True)