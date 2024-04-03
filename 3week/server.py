from flask import Flask, render_template, redirect, flash, request
import jinja2, pdb
from melons import melon_dict, get_melon_list

app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined        # for debugging




@app.route("/")
def homepage():
    return render_template("index.html")



@app.route("/melons")
def show_all_melons(melon_dict):
    all_melons = get_melon_list(melon_dict)
    pdb.set_trace()
    return render_template("melons.html", all_melons = all_melons)
    



@app.route("/melons/<melon_id>")
def show_single_melon(melon_id):

    return render_template("single_melon.html")



@app.route("/add_to_cart/<melon_id>")
def add_melon_to_cart(melon_id):
    return f"{melon_id} 🍉 has been added to the cart."



@app.route("/cart")
def show_cart():
    return render_template("cart.html")












if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, port=4040, host="localhost")