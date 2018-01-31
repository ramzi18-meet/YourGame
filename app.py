from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)




@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
    






@app.route('/upcoming')
def upcoming():
    return render_template('upcoming.html')
    







@app.route('/contact')
def contact():
    return render_template('contact.html')
    






@app.route('/about')
def about():
    return render_template('about.html')
  
@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['Name']
    email = request.form['Email']
    password = request.form['Password']
    save = sign(name, email, password)
    db.session.add(save)
    db.session.commit()
    users = sign.query.all() 
    return render_template('upcoming.html')       


class sign(db.Model):
    __tablename__ = "sign"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('Name', db.Unicode)
    email = db.Column('Email', db.Unicode)
    password = db.Column('Password', db.Unicode)
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
db.create_all()



if __name__ == "__main__":
    app.run()