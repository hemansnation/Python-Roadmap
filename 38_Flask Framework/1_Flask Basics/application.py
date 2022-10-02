from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from first Flask App"

@app.route('/home')
def home():
    return "<h1>Hello Home</h1>"


@app.route('/profile')
def profile():
    goa = "Hi this is Goa to Indore"
    return render_template('index.html', name="hello")

if __name__ == '__main__':
    app.run(port=5002)


# localhost - 127.0.0.1:5000


# https://github.com/hemansnation/Python-Roadmap-2022
# scheme  domain name  route
#          DNS