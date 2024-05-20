from flask import Flask, render_template

# Create a website object
app = Flask(__name__)


# Connect html pages to the website object (DECORATOR)
@app.route("/")
# Define a function to open the html page
# (create a template folder to keep all the html files)
def home():
    return render_template("home.html")


# By using <statio> <date> you make this variable dynamic
# So the users can insert the station and date they want
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 1
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)