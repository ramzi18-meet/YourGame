from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('home.html')
    
if __name__ == "__main__":
    app.run()

@app.route('/upcoming')
def index():
    return app.send_static_file('upcoming.html')
    
if __name__ == "__main__":
    app.run()