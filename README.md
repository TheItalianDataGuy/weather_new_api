# Weather Station Data Visualization

This project is a Flask-based web application that allows users to visualize and interact with historical temperature data from various weather stations. The application provides a simple web interface to view station data and an API to retrieve temperature data based on station ID and date.

## Features

- **Home Page**: Displays a table of available weather stations.
- **API Endpoints**:
  - `/api/v1/<station>/<date>`: Retrieve temperature data for a specific station and date.
  - `/api/v1/<station>`: Retrieve all temperature data for a specific station.
  - `/api/v1/yearly/<station>/<year>`: Retrieve temperature data for a specific station and year.

## Project Structure

```plaintext
.
├── data_small/                 # Folder containing weather station data files
│   ├── TG_STAID000001.txt      # Example data file for a specific station
│   ├── TG_STAID000002.txt      # Example data file for a specific station
│   └── stations.txt            # File containing station ID and names
├── templates/                  # Folder containing HTML templates
│   └── home.html               # HTML template for the home page
├── app.py                      # Main Flask application
└── README.md                   # Project documentation
```

## Requirements
- Python 3.8+
- Flask
- Pandas

## Installation
1. Clone the repository:

  ```bash
  git clone https://github.com/yourusername/weather-station-visualization.git
  cd weather-station-visualization
  ```
2. Install the required packages:

  ```bash
  pip install -r requirements.txt
  ```
3. Place your weather station data files in the data_small/ directory. The stations.txt file should list all stations, and each station should have its own data file.

## Usage
1. Run the Flask App:

  ```bash
  app.py
  ```
2. Access the Web Interface: Open your browser and go to http://127.0.0.1:5001 to view the list of weather stations.

3. Use the API:

    - To get temperature data for a specific station and date:

        ```bash
        http://127.0.0.1:5001/api/v1/<station>/<date>
        ```
        Replace <station> with the station ID and <date> with the date in YYYY-MM-DD format.

    - To get all data for a specific station:
      
        ```ruby
        http://127.0.0.1:5001/api/v1/<station>
        ```
      
    - To get yearly data for a specific station:

        ```ruby
        http://127.0.0.1:5001/api/v1/yearly/<station>/<year>
         Replace <year> with the desired year.

## Example
- Home Page: Displays a table of all available weather stations.
- API Call: Example API call to get the temperature for station 1 on 2023-08-11:
  ```ruby
  http://127.0.0.1:5001/api/v1/1/2023-08-11
  ```
  
## License
This project is licensed under the MIT License.

## Acknowledgments
- Flask
- Pandas
