from flask import Flask, render_template, request, redirect, url_for
import random
from tabulate import tabulate
from sys import exit

app = Flask(__name__)

otp = None

# Function to calculate BMI and determine condition
def calculate_bmi(weight, height):
    bmi = (float(weight) / (float(height) / 100) ** 2)  # BMI calculation
    if bmi < 16:
        bcat = "Starvation"
    elif bmi < 17:
        bcat = "Anorexic"
    elif bmi < 18.5:
        bcat = "Underweight"
    elif bmi < 25:
        bcat = "Ideal"
    elif bmi < 30:
        bcat = "Overweight"
    elif bmi < 35:
        bcat = "Obese"
    elif bmi < 40:
        bcat = "Morbidly Obese"
    else:
        bcat = "Severely Obese"

    return round(bmi, 1), bcat

# Route for home page
@app.route("/")
def home():
    global otp
    otp = random.randint(1111, 9999)
    return render_template("otp.html", otp=otp)

# Route to verify OTP
@app.route("/verify", methods=["POST"])
def verify_otp():
    global otp
    user_otp = request.form.get("otp")
    if user_otp and int(user_otp) == otp:
        return redirect(url_for("calculator"))
    else:
        otp = random.randint(1111, 9999)
        return render_template("otp.html", otp=otp, error="Invalid OTP. A new OTP has been generated.")

# Route for BMI Calculator page
@app.route("/calculator")
def calculator():
    return render_template("calculator.html")

# Route to handle BMI calculation
@app.route("/calculate", methods=["POST"])
def calculate():
    name = request.form.get("name")
    gender = request.form.get("gender")
    age = request.form.get("age")
    weight = request.form.get("weight")
    height = request.form.get("height")

    if not (name and gender and age and weight and height):
        return render_template("calculator.html", error="All fields are required.")

    bmi, bcat = calculate_bmi(weight, height)
    details = [
        ["Name", name],
        ["Gender", gender],
        ["Age", age],
        ["Weight (kg)", weight],
        ["Height (cm)", height],
        ["BMI", bmi],
        ["Category", bcat],
    ]
    return render_template("result.html", details=details)

# Route for diseases information
@app.route("/diseases")
def diseases():
    return render_template("diseases.html")

# Route to exit the application
@app.route("/exit")
def exit_app():
    return render_template("exit.html")

if __name__ == "__main__":
    app.run(debug=True)
