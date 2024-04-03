from flask import Flask, render_template, redirect, flash, request
import jinja2

app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined



@app.route("/")
def homepage():
    return render_template("base.html")

@app.route("/all_melons")
def all_melons():
    return render_template("all_melons.html")

@app.route("/melon/<melon_id>")
def melon_details(melon_id):
    return render_template("melon_details.html")

@app.route("/cart")
def show_cart():
    return render_template("cart.html")

@app.route("/add_to_cart/<melon_id>")
def add_to_cart(melon_id):
    return f"{melon_id} added to cart"





if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 4040, host = "localhost")