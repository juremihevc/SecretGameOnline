from flask import Flask, render_template, request, make_response
import random

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():

    secret_number = request.cookies.get("secret_number")
    response = make_response(render_template("index.html"))
    if not secret_number:  # if not, create a new cookie
        new_secret = random.randint(1, 30)
        response.set_cookie("secret_number", str(new_secret))
    return response

@app.route("/result", methods=["POST"])
def result():

    user_guess = int(request.form.get("user_guess"))
    secret_number = int(request.cookies.get("secret_number"))

    if user_guess == None:
        return make_response(render_template("index.html"))

    if secret_number == user_guess:
        message = f"Bingo! The secret number is {secret_number}."
        response = make_response(render_template("result.html", message=message))
        response.set_cookie("secret_number", str(random.randint(1, 30)))
        return response

    if secret_number < user_guess:
        message = "Wrong! Try smaller!"
        response = make_response(render_template("result.html", message=message))
        return response

    if secret_number > user_guess:
        message = "Wrong! Try bigger!"
        response = make_response(render_template("result.html", message=message))
        return response



if __name__ == '__main__':
    app.run(use_reloader=True)