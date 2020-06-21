from flask import Flask,render_template,session,redirect,url_for,request,flash,Response
from Blood_Donor import app,db
from Blood_Donor.models import User,Donor
from Blood_Donor.forms import LoginForm,RegisterForm


@app.route('/home')
@app.route('/')
def index():
	return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		email = form.email.data
		password = form.password.data

		user=User.objects(email=email).first()
		if user and user.password==password:
			flash("Successfully logged in ","success")
			return redirect(url_for('index'))
		else:
			flash("Invalid username or password","danger")
	return render_template('login.html',form=form)


@app.route('/register',methods=['GET','POST'])
def register():
	form=RegisterForm()
	if form.validate_on_submit():
		name=form.name.data
		email=form.email.data
		password = form.password.data

		user_id=User.objects.count()+1
		user=User(user_id=user_id,name=name,email=email)
		user.set_password(password)
		user.save()
		flash("Successfully Registered..")
		return redirect(url_for('index'))
	return render_template('register.html',form=form)


@app.route('/search')
def search():
	search=request.args.get('search')
	if search=='o' or search=='o+' or search=='A':
		return render_template('search.html',data=register_Data.Bloodgroup)



@app.route('/user')
def user():
	#User(user_id=1,name="shviam garg",email="gargshivam1712@gmail.com",password="shivam123").save()
	#User(user_id=2,name="aman agrawal",email="aman1712@gmail.com",password="aman123").save()

	users=User.objects.all()

	return render_template('api.html',users=users)
