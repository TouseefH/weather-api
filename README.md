# Weather Forecasting API

## Table of Contents
- [Project Overview](#project-overview)
- [Team Collaboration](#team-collaboration)
- [API Endpoints](#api-endpoints)
- [Installation](#installation)
- [Usage](#usage)


## Project Overview

The Weather Forecasting API is a Flask-based application that provides real-time weather information, including temperature, city, and weather description. This project aims to serve developers and businesses by offering reliable weather data for various applications such as travel planning, agriculture, and event management. It exemplifies effective collaboration among team members using Git and GitHub, showcasing our ability to work together on a software development project utilizing best practices in version control.

## Team Collaboration

- *Touseef Hanif* (API and Endpoint Development)
  - Developed the core /weather endpoint, implementing logic to retrieve and return weather data based on the specified city.

- *Syed Danayal Raza* (Frontend Integration)
  - Integrated the frontend application with the backend API, ensuring smooth data flow and user interaction. Implemented user-friendly interfaces for requesting weather information.

- *Muhammad Abdullah Malik* (Testing and Documentation)
  - Conducted thorough testing of the API endpoints to ensure functionality and reliability. Created this README.md file and provided comprehensive documentation for users and contributors.


## API Endpoints

### 1. Get Weather Information
- *Endpoint:* /weather
- *Method:* GET
- *Description:* Retrieves basic weather information for a specified city.

#### Example Request
```http
GET /weather?city=London
```

##### Example Response
Here is an example of the JSON response returned by the API:
```bash
json
{
  "city": "London",
  "temperature": "15°C",
  "description": "Partly cloudy"
}
```
## Installation Process

To set up the Weather Forecasting API on your local machine, follow these steps:

1. *Clone the Repository*
   ```bash
   git clone https://github.com/TouseefH/weather-api.git
2. **Navigate to the Project Directory**
   ``` bash
    cd weather-api
3. *Create a Virtual Environment (Optional but recommended)*
    ```bash
    python -m venv venv
4. **Activate the Virtual Environment**
    ```bash
    venv\Scripts\activate
5. *Install Dependencies*
    ```bash
    pip install -r requirements.txt 

## Usage
1. **Run the  app**
    ```bash
    python app.py
2. *Access the API Open your web browser or a tool like Postman and navigate to*
    ```bash
    http://127.0.0.1:5000/weather?city=London
