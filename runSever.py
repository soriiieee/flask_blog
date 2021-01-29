from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
#instance making..
app = Flask(__name__)
app.config["SECRET_KEY"] = 'c0cee159c47e87bca14994d2d7577cc0'

#---------------------
# tmp
#---------------------
posts = [
    {
        'author': "soriiieee",
        'title': "Blog Post 1",
        'content': "First post content",
        "date_posted": "April 20 , 2020"
    },
    {
        'author': "soriiieee",
        'title': "Blog Post 2",
        'content': "Second post content",
        "date_posted": "April 22 , 2020"
    },

]


#---------------------
# routing table..
#---------------------
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form = form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form = form)

if __name__ == "__main__":
  app.run(debug=True)

