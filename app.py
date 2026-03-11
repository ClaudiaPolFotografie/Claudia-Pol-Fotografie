import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Helper functie om alle foto's uit een map te halen
def get_photos(category):
    folder = os.path.join(app.static_folder, "images", category)
    files = sorted(os.listdir(folder))
    photos = [f"{category}/{f}" for f in os.listdir(folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    photos.sort()
    return photos

# ROUTES
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sport")
def sport():
    photos = get_photos("sport")
    return render_template("sport.html", photos=photos)

@app.route("/team")
def team():
    photos = get_photos("team")
    return render_template("team.html", photos=photos)

# @app.route("/portret")
# def portret():
#     photos = get_photos("portret")
#     return render_template("portret.html", photos=photos)

# @app.route("/familieshoot")
# def familieshoot():
#     photos = get_photos("familieshoot")
#     return render_template("familieshoot.html", photos=photos)

# @app.route("/bruiloft")
# def bruiloft():
#     photos = get_photos("bruiloft")
#     return render_template("bruiloft.html", photos=photos)

@app.route("/overig")
def overig():
    photos = get_photos("overig")
    return render_template("overig.html", photos=photos)

@app.route("/tarieven")
def tarieven():
    return render_template("tarieven.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)