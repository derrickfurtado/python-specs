from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length

# Add user creation form

class TeamForm(FlaskForm):
    team_name = StringField("Team Name: ", validators=[DataRequired(), Length(min=4, max=255)])
    submit = SubmitField("Add Team")


class ProjectForm(FlaskForm):
    project_name = StringField("Project Name: ", validators=[DataRequired(), Length(min=4, max=255)])
    description = TextAreaField("Project Description: ", validators=[DataRequired(), Length(min=4, max=255)])
    completed = BooleanField("Has it been completed?")
    team_selection = SelectField("Which team will own this: ")
    submit = SubmitField("Add Project")

    def update_teams(self, teams):
        self.team_selection.choices = [(team.id, team.team_name) for team in teams]  
