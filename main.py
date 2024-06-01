from flask import Flask, render_template
import pandas as pd
from datetime import datetime

# Create a website object
app = Flask(__name__)

# Table to be visualised on the home webpage
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


# Connect html pages to the website object (DECORATOR)
@app.route("/")
# Define a function to open the html page
# (create a template folder to keep all the html files)
# Add data using to_html method to add the table - in the html file add {{data|safe}}
def home():
    return render_template("home.html", data=stations.to_html())


# By using <station> <date> you make this variable dynamic
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


# Create the option to select a specific station and get all the data with years and temperatures
@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # Modify the dataframe so that it will show just the date and the temperature
    df = df[["    DATE", '   TG']]
    result = df.to_dict(orient="records")
    return result


# Crete URL based on the date.
# '    DATE' needs to be converted into a string with .astype() function
# .str.startswith(str(year)) will select the year typed in
@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))].to_dict(orient="records")
    return result


# If run multiple Flask apps, change the port (default port is 5000)
if __name__ == "__main__":
    app.run(debug=True, port=5001)
