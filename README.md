# 🌦️ Weather App (CLI)

## Description

The **Weather App (CLI)** is a simple Python project that allows users to check the current weather of any city directly from the command line. The application uses the **OpenWeatherMap API** to retrieve live weather information.

This project is designed for beginners who want to learn how to work with APIs, HTTP requests, JSON data, and Python programming. It is a great project for students and can be uploaded to GitHub as part of a programming portfolio.

---

## Features

* 🌍 Search weather by city name
* 🌡️ Display current temperature in Celsius
* 🤗 Show "Feels Like" temperature
* 💧 Display humidity
* 🌤️ Show weather condition
* 💨 Display wind speed
* ❌ Handles invalid city names
* 🖥️ Easy-to-use Command Line Interface (CLI)

---

## Technologies Used

* Python 3
* Requests Library
* OpenWeatherMap API

---

## Project Structure

```
Weather-App/
│── weather.py
│── requirements.txt
└── README.md
```

---

## Requirements

* Python 3.x
* Internet connection
* OpenWeatherMap API Key
* Requests library

Install the required package:

```bash
pip install -r requirements.txt
```

or

```bash
pip install requests
```

---

## Installation

1. Clone this repository.

```bash
git clone https://github.com/Sahilrawal243/Weather-App.git
```

2. Open the project folder.

3. Install the required library.

```bash
pip install -r requirements.txt
```

4. Open `weather.py`.

5. Replace the API key with your own OpenWeatherMap API key.

```python
API_KEY = "YOUR_API_KEY"
```

6. Run the project.

```bash
python weather.py
```

---

## Example

**Input**

```
Enter city name: Delhi
```

**Output**

```
===== Weather Report =====
City: Delhi
Temperature: 34 °C
Feels Like: 37 °C
Humidity: 55 %
Weather: Clear Sky
Wind Speed: 3.5 m/s
```

---

## Learning Outcomes

By completing this project, you will learn:

* Python basics
* User input
* Variables
* Conditional statements
* Using the Requests library
* Working with APIs
* Reading JSON data
* Error handling
* Building a Command Line Interface (CLI) application

---

## Future Improvements

* 5-day weather forecast
* Weather icons
* Save search history
* Multiple city search
* Colored terminal output

---
