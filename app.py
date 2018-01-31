from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Yo, it's working!"
@app.route('/home/')
def root():
    return app.send_static_file('home.html')
if __name__ == "__main__":
    app.run()