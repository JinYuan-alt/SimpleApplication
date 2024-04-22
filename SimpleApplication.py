from flask import Flask, render_template

app=Flask(__name__)

@app.route('/') #controller- controls where it is redirected#
def layout():
    return render_template('layout.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()

