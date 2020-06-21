from Blood_Donor import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Document):
	user_id=db.IntField(unique=True)
	name = db.StringField(max_length=50)
	email = db.StringField(max_length=50)
	password = db.StringField(max_length=150)

	def set_password(self,password):
		self.password=generate_password_hash(password)

	def get_password(self,password):
		return check_password_hash(self.password,password)

class Donor(db.Document):
	username = db.StringField(max_length=50)
	name = db.StringField(max_length=50)
	email = db.StringField(max_length=50)
	password = db.StringField(max_length=50)