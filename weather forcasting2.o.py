import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Function to fetch weather data
def get_weather_data(city_name):
    api_key = '3f9add9526fafb77531adef9762ffdbb'  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Create the full URL
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    
    try:
        # Send the GET request to fetch data
        response = requests.get(complete_url)
        response.raise_for_status()  # Raises an error for HTTP issues
        data = response.json()
        
        if data.get('cod') == 200:
            main = data['main']
            weather = data['weather'][0]
            wind = data['wind']
            
            # Extract required data
            weather_info = {
                'city': city_name,
                'temperature': main['temp'],
                'humidity': main['humidity'],
                'description': weather['description'],
                'wind_speed': wind['speed']
            }
            return weather_info
        else:
            return None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch data: {e}")
        return None

# Function to display weather data
def show_weather():
    city_name = city_var.get()
    
    if not city_name:
        messagebox.showwarning("Input Error", "Please select a city!")
        return
    
    weather_info = get_weather_data(city_name)
    
    if weather_info:
        # Display the weather information in the GUI
        temp_label.config(text=f"Temperature: {weather_info['temperature']}°C")
        humidity_label.config(text=f"Humidity: {weather_info['humidity']}%")
        description_label.config(text=f"Weather: {weather_info['description'].capitalize()}")
        wind_label.config(text=f"Wind Speed: {weather_info['wind_speed']} m/s")
    else:
        messagebox.showerror("Error", "City not found! Please try again.")

# Create the main window
root = tk.Tk()
root.title("Weather Forecasting System")
root.geometry("800x600")
root.configure(bg="lightblue")

# List of Indian cities
indian_cities = [
    "Delhi", "Mumbai", "Bengaluru", "Kolkata", "Chennai", "Hyderabad", 
    "Pune", "Ahmedabad", "Jaipur", "Lucknow", "Surat", "Bhopal", "Chandigarh", 
    "Visakhapatnam", "Nagpur", "Patna", "Indore", "Thiruvananthapuram", "Goa","satara"
]

# Variable to store selected city
city_var = tk.StringVar()

# Add labels and input fields for the user interface
title_label = tk.Label(root, text="Weather Forecasting System", font=("Algerian", 30, "bold", "underline"), bg="lightblue")
title_label.pack(pady=10)

city_label = tk.Label(root, text="Select City:", font=("Arial", 25, "bold"), bg="lightblue")
city_label.pack(pady=10)

# Dropdown menu for city selection
city_dropdown = ttk.Combobox(root, textvariable=city_var, values=indian_cities, font=("Arial", 20))
city_dropdown.pack(pady=10)
city_dropdown.set("Select a city")  # Default text

# Add a button to fetch weather data
search_button = tk.Button(root, text="Get Weather", command=show_weather, font=("Arial", 25), bg="white", fg="black")
search_button.pack(pady=10)

# Labels to display weather data
temp_label = tk.Label(root, text="Temperature: N/A", font=("Arial", 25), bg="lightblue")
temp_label.pack(pady=5)

humidity_label = tk.Label(root, text="Humidity: N/A", font=("Arial", 25), bg="lightblue")
humidity_label.pack(pady=5)

description_label = tk.Label(root, text="Weather: N/A", font=("Arial", 25), bg="lightblue")
description_label.pack(pady=5)

wind_label = tk.Label(root, text="Wind Speed: N/A", font=("Arial", 25), bg="lightblue")
wind_label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()