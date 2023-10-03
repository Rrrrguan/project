from flask import Flask, render_template

app = Flask("__main__")


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/store')
def store():
    return render_template('store.html')



if __name__ == "__main__":
    app.run()