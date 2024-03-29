from flask import Flask, render_template, url_for, redirect
from cupcakes import display_menu, display_random_cupcakes, find_cupcake_name, add_cupcake_to_order, show_cart


app = Flask(__name__)


# @app.route("/endpoint_alpha")


@app.route("/main")
def showcase_display():
    return render_template("index.html", cupcakes = display_random_cupcakes("inventory.csv"))

@app.route("/cupcake_menu")
def menu_display():
    return render_template("all_view.html", cupcakes = display_menu("inventory.csv"))
def add_cupcake(name_query):
    cupcake = find_cupcake_name("inventory.csv", name_query)
    if cupcake:
        add_cupcake_to_order("order.csv", cupcake)
        return redirect(url_for("/cupcake_menu"))
    else:
        return "Sorry cupcake is not found."

@app.route("/cupcake_order")
def order_display():
    return render_template("order_view.html", cupcakes = show_cart("order.csv"))

# @app.route("/cupcake_single")
# def single():
#     return render_template("single_view.html")




if __name__ == "__main__":
    app.debug = "development"                                 #env will be deprecated in Flask 2.3 -- use .debug instead
    app.run(debug = True, port = 4040, host = "localhost")