# Import required modules
from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox

# Create the object
app = Tk()

# Add a title
app.title("Get Weather")

# Adjust the window size
app.geometrry("300x300")

# Add labels, buttons, and text
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

Search_btn = Button(app, text="Search the weather",
                    width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text="Location",
                     font={'bold', 20})

location_lbl.pack()

temperature_label = Label(app, text="")
temperature_label.pack()

weather_l = Label(app, text="")
weather_l.pack()

app.mainloop()

# Extract key from the configuration file
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'

# Function to get weather details
