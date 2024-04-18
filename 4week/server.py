from flask import Flask, render_template, flash, url_for, redirect
from pdb import set_trace
from forms import TeamForm, ProjectForm
from key import app_key
from model import User, Team, Project, connect_to_db



app = Flask(__name__)

app.secret_key = app_key    

user_id = 1


@app.route("/")
def homepage():
    team_form = TeamForm()
    project_form = ProjectForm()
    # project_form.update_teams(User.query.get(user_id).teams)                                          ############
    return render_template("home.html", team_form = team_form, project_form = project_form)


@app.route("/add_team", methods=["POST"])
def add_team():
    team_form = TeamForm()

    if team_form.validate_on_submit():
        print(f"TEAM DATA: {team_form.team_name.data}")
        flash(f"{team_form.team_name.data} Team created!")
    else:
        flash("Form failed to validate on submit")
    return redirect(url_for("homepage"))


@app.route("/add_project", methods=["POST"])
def add_project():
    project_form = ProjectForm()
    project_form.update_teams(User.query.get(user_id).teams) 
    set_trace()


    if project_form.validate_on_submit():
        print(f"PROJECT DATA: {project_form.project_name.data}")
        print(f"DESCRIPTION DATA: {project_form.description.data}")
        flash(f"{project_form.project_name.data} Project Created!")
    else:
        flash("Form failed to validate on submit")
    return redirect(url_for("homepage"))






if __name__ == "__main__":
    app.debug = "development"
    connect_to_db(app)                                            ##############
    app.run(debug=True, port = 4040, host = "localhost")