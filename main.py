from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

class LoginForm(FlaskForm):
    eml = StringField(label='Email', validators=[DataRequired(), Email()])
    psd = PasswordField(label='Password', validators=[DataRequired(), Length(min=3)])
    sbt = SubmitField(label='Log Inn')

app = Flask(__name__)
app.secret_key = "mynameisvas"
Bootstrap(app=app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    lf = LoginForm()
    if lf.validate_on_submit():
        if lf.eml.data == "abc@g.c" and lf.psd.data == "vas":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=lf)


if __name__ == '__main__':
    app.run(debug=True)