from flask import Flask, render_template, redirect, flash, request
import jinja2, pdb, melons

app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined



@app.route("/")
def homepage():
    return render_template("base.html")

@app.route("/all_melons")
def all_melons_page():
    melon_list = melons.get_all()
    return render_template("all_melons.html", melon_list=melon_list)

@app.route("/melon/<melon_id>")
def melon_details_page(melon_id):
    melon = melons.get_by_id(melon_id)
    return render_template("melon_details.html", melon = melon)

@app.route("/cart")
def show_cart_page():
    return render_template("cart.html")

@app.route("/add_to_cart/<melon_id>")
def add_to_cart_func(melon_id):
    return f"{melon_id} added to cart"





if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 4040, host = "localhost")