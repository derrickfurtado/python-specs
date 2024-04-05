from flask import Flask, render_template, redirect, flash, request, session
import jinja2, pdb, melons, bcrypt, customers
from forms import LoginForm


app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined
app.secret_key = 'dev'                                          #this should be longer and more secure



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
    cart_total = 0
    cart_contents = []
    cart = session.get('cart', {})
    for melon_id, qty in cart.items():
        melon = melons.get_by_id(melon_id)
        total_cost = qty * melon.price
        cart_total += total_cost

        melon.quantity = qty
        melon.melon_cost = total_cost

        cart_contents.append(melon)
    return render_template("cart.html", cart_contents=cart_contents, cart_total=cart_total)

@app.route("/add_to_cart/<melon_id>")
def add_to_cart_func(melon_id):
    if 'cart' not in session:
        session['cart'] = {}
    cart = session["cart"]                              #don't really understand this - from session to cart
    cart[melon_id] = cart.get(melon_id, 0) + 1
    session.modified = True
    flash(f"{melon_id} added to cart")

    return redirect("/cart")

@app.route("/empty-cart")
def empty_cart():
    if "cart" in session:
        session["cart"] = {}
    return redirect("/cart")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = customers.get_by_username(username)

        if not user or user["password"] != password:
            flash("Login credentials are incorrect")
            return redirect("/login")
        session["username"] = user['username']
        flash("You are logged in!")
        return redirect("/all_melons")
        
    return render_template("login.html", form=form)




if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 4040, host = "localhost")