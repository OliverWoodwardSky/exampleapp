from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page, I have made an edit'

@app.route('/about')
def about():
    return 'This is the about page. this is cool.'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
