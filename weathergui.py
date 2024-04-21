import tkinter as tk
import requests

def fetch_weather():
    city = city_entry.get()
    api_key = '1bd54b904e7cf5f16db1a2e4d8c8a08b'  # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_label.config(text=f'Weathert: {weather_desc}\nTemperature: {temp}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s')
    else:
        weather_label.config(text='City not found')

# GUI setup
root = tk.Tk()
root.title('Weather App')

city_label = tk.Label(root, text='Enter city:')
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

fetch_button = tk.Button(root, text='Fetch Weather', command=fetch_weather)
fetch_button.pack()

weather_label = tk.Label(root, text='')
weather_label.pack()

root.mainloop()
