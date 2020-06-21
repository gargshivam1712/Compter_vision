from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError,Length
from Blood_Donor.models import User

class LoginForm(FlaskForm):
	email=StringField("Email",validators=[DataRequired()])
	password = PasswordField("Password" ,validators=[DataRequired(),Length(min=6,max=20)])
	remember_me = BooleanField("Remember me")
	submit = SubmitField("Login")

class RegisterForm(FlaskForm):
	email = StringField("Email",validators=[DataRequired(),Email()])
	name = StringField("Name",validators=[DataRequired(),Length(min=6,max=50)])
	password = PasswordField("Password" ,validators=[DataRequired(),Length(min=6,max=20)])
	confirm_password = PasswordField("Confirm Password" ,validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField("Register")

	def validate_email(self,email):
		user=User.objects(email=email.data).first()
		if user:
			raise ValidationError("Email already exists use another one.")

	def validate_name(self,name):
		user = User.objects(name=name.data).first()
		if user:
			raise ValidationError("Name already exists use another one.")


	

