# Import required modules
from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox
import pytest

# Extract key from the configuration file
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q=%7B%7D&appid=%7B%7D'

# Function to get weather details
def getweather(city):
    result = requests.get(url.format(city, api_key))
    
    if result.json():
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin-273.15
        temp_farenheit = (temp_celsius * 1.8) + 32
        weather1 = json['weather'][0]['main']
        final = [city, country, temp_kelvin, temp_celsius, temp_farenheit, weather1]
        return final

    else:
        print("No content found")

# function to search city
def search():
    city = city_text.get()
    weather = getweather(city)

    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[3])+"   Degrees Celsius"
        weather_l['text'] = weather[4]

    else:
        messagebox.showerror('Error', "Can't find {}".format(city))

# Create the object
app = Tk()

# Add a title
app.title("Get Weather")

# Adjust the window size
app.geometry("300x300")

# Add labels, buttons, and text
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

Search_btn = Button(app, text="Search the weather",
                    width=16, command=search)
Search_btn.pack()

location_lbl = Label(app, text="Location",
                     font={'bold', 20})

location_lbl.pack()

temperature_label = Label(app, text="")
temperature_label.pack()

weather_l = Label(app, text="")
weather_l.pack()

app.mainloop()