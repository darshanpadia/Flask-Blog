from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bfca5d6bb45ca88cf38c854d58fa7b12'




post = [
	{
		'author': 'Someone',
		'title' : 'title 1',
		'content': 'something',
		'date_posted': 'April 20'
	},
	{
		'author': 'Sometwo',
		'title' : 'title 2',
		'content': 'somethink',
		'date_posted': 'April 420'
	}
]

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts = post)

@app.route('/about')
def about():
	return render_template('about.html',title = 'About')

@app.route('/register',methods = ['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f"Account Created for {form.username.data}!","success")
		return redirect(url_for('home'))
	return render_template('register.html', title = 'Register', form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title = 'login', form=form)

if __name__ == "__main__":
	app.run(debug = True)