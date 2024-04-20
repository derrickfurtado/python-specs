from flask import Flask, render_template, flash, url_for, redirect, request
from pdb import set_trace
from forms import TeamForm, ProjectForm, UserForm
from key import app_key
from model import User, Team, Project, connect_to_db, get_teams, db



app = Flask(__name__)

app.secret_key = app_key    



@app.route("/")
def homepage():
    team_form = TeamForm()
    user_form = UserForm()
    project_form = ProjectForm()
    project_form.update_teams(get_teams())
                                        
    return render_template("home.html", team_form = team_form, project_form = project_form, user_form = user_form)

@app.route("/projects")
def projects_page():
        project_list = Project.query.all()
        return render_template("projects.html", project_list = project_list)


@app.route("/teams")
def team_page():
    team_list = Team.query.all()
    return render_template("teams.html", team_list=team_list)

@app.route("/users")
def user_page():
    user_list = User.query.all()
    return render_template("users.html", user_list=user_list)

###################################################

@app.route("/add_user", methods = ["POST"])
def add_user():
    user_form = UserForm()
    name_list = []
    user_list = User.query.all()
    # set_trace()

    for user in user_list:
        name_list.append(user.username)
    if user_form.validate_on_submit():
        if user_form.username.data in name_list:
            flash("Username already exists!")
        else:
            username = user_form.username.data
            password = user_form.password.data
            new_user = User(username, password)
            db.session.add(new_user)
            db.session.commit()
            flash(f"Username: {user_form.username.data} created!")
    else:
        flash("Form failed to validate on submit")

    return redirect(url_for("homepage"))
    

@app.route("/add_team", methods=["POST"])
def add_team():
    team_form = TeamForm()
    team_list = Team.query.all()
    name_list = []

    for team in team_list:
        name_list.append(team.team_name)
    if team_form.validate_on_submit():
        if team_form.team_name.data in name_list:
            flash("Team name already exists!")
        else:
            team_name = team_form.team_name.data
            new_team = Team(team_name, 1)
            db.session.add(new_team)
            db.session.commit()
            flash(f"{team_form.team_name.data} team created!")
    else:
        flash("Form failed to validate on submit")
    return redirect(url_for("homepage"))


@app.route("/add_project", methods=["POST"])
def add_project():
    project_form = ProjectForm()
    project_form.update_teams(get_teams())
    project_list = Project.query.all()
    name_list = []

    for project in project_list:
        name_list.append(project.project_name)



    if project_form.validate_on_submit():
        if project_form.project_name.data in name_list:
            flash("Project name already exists!")
        else:
            project_name = project_form.project_name.data
            description = project_form.description.data
            completed = project_form.completed.data
            team_owner = project_form.team_selection.data

            new_project = Project(project_name, description, completed, team_owner)
            db.session.add(new_project)
            db.session.commit()
            flash(f"{project_form.project_name.data} Project Created!")
    else:
        flash("Form failed to validate on submit")
    return redirect(url_for("homepage"))

@app.route("/complete_project")
def complete_project():
    id = request.args.get('project_id')
    project_to_complete = Project.query.filter_by(id = id).all()
    project_to_complete[0].completed = True
    db.session.add(project_to_complete[0])
    db.session.commit()
    return redirect(url_for("projects_page"))


@app.route("/delete_project")
def delete_project():
    id = request.args.get('project_id')
    project_to_delete = Project.query.filter_by(id = id).all()
    db.session.delete(project_to_delete[0])
    db.session.commit()
    
    flash("Project has been deleted!")
    return redirect(url_for("projects_page"))

@app.route("/delete_user")
def delete_user():
    id = request.args.get('user_id')
    user_to_delete = User.query.filter_by(id = id).all()
    db.session.delete(user_to_delete[0])
    db.session.commit()

    flash("User has been deleted!")
    return redirect(url_for("user_page"))

@app.route("/delete team")
def delete_team():
    id = request.args.get('team_id')
    set_trace()
    team_to_delete = Team.query.filter_by(id = id).all()
    db.session.delete(team_to_delete[0])
    db.session.commit()

    flash("Team Deleted!")
    return render_template("team_page")





if __name__ == "__main__":
    app.debug = "development"
    connect_to_db(app)                                           
    app.run(debug=True, port = 4040, host = "localhost")