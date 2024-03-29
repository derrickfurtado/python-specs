from flask import Flask, render_template
from cupcakes import display_menu, display_random_cupcakes, find_cupcake_name, add_cupcake_to_order


app = Flask(__name__)


# @app.route("/endpoint_alpha")


@app.route("/main")
def home():
    return render_template("index.html", cupcakes = display_random_cupcakes("inventory.csv"))

@app.route("/cupcake_menu")
def menu():
    return render_template("all_view.html", cupcakes = display_menu("inventory.csv"))

@app.route("/cupcake_order")
def order():
    return render_template("order_view.html", cupcakes = find_cupcake_name())

# @app.route("/cupcake_single")
# def single():
#     return render_template("single_view.html")




if __name__ == "__main__":
    app.debug = "development"                                 #env will be deprecated in Flask 2.3 -- use .debug instead
    app.run(debug = True, port = 4040, host = "localhost")