from flask import Flask, render_template,url_for
app=Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/places")
def places_page():
    return render_template("places.html")

@app.route("/home")
def home_page():
    return render_template("home.html")
     
if __name__=='__main__':
    app.run(debug=True)
    