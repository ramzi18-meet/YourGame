from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('home.html')
    
if __name__ == "__main__":
    app.run()

@app.route('/upcoming')
def upcoming():
    return app.send_static_file('upcoming.html')
    
if __name__ == "__main__":
    app.run()

@app.route('/upcoming')
def contact():
    return app.send_static_file('contact.html')
    
if __name__ == "__main__":
    app.run()


@app.route('/about')
def about():
    return app.send_static_file('about.html')
    
if __name__ == "__main__":
    app.run()