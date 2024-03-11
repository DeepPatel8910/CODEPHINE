import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk

API_KEY = 'e7704bc895b4a8d2dfd4a29d404285b6'

class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather App")
        self.master.configure(bg="#f0f0f0")

        # Weather App Logo
        self.logo = Image.open("weather.png")  # Add your logo file path here
        self.logo = self.logo.resize((50, 50), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_label = ttk.Label(master, image=self.logo, background="#f0f0f0")
        self.logo_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Heading
        self.heading_label = ttk.Label(master, text="Weather App", background="#f0f0f0", font=("Helvetica", 20, "bold"), foreground="#333")
        self.heading_label.grid(row=0, column=1, columnspan=3, padx=10, pady=10, sticky="w")

        self.location_label = ttk.Label(master, text="Enter City:", background="#f0f0f0", font=("Helvetica", 12))
        self.location_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.location_entry = ttk.Entry(master, width=30, font=("Helvetica", 12))
        self.location_entry.grid(row=1, column=1, padx=10, pady=5)

        self.search_button = ttk.Button(master, text="Search", command=self.get_weather, style="TButton")
        self.search_button.grid(row=1, column=2, padx=10, pady=5)

        self.weather_info_label = ttk.Label(master, text="", background="#f0f0f0", font=("Helvetica", 12), anchor="center")
        self.weather_info_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

    def get_weather(self):
        location = self.location_entry.get()
        if not location:
            return
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            weather_description = data['weather'][0]['description'].capitalize()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            city = data['name']
            country = data['sys']['country']
            weather_info = f"City: {city}, {country}\nWeather: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
            self.weather_info_label.config(text=weather_info)
        else:
            self.weather_info_label.config(text="Error: City not found.")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
