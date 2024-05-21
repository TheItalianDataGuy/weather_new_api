from flask import Flask, render_template
import pandas as pd



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
    # We import the csv file. However as they are different files we give
    # the common beginning of the name and add the zfill() method to make the series of the numbers in the name itself.
    # Check the jupyter file!!!
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}


# If run multiple Flask apps, change the port (default port is 5000)
if __name__ == "__main__":
    app.run(debug=True, port=5001)