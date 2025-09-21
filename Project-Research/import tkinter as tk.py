import tkinter as tk
from tkinter import messagebox
import requests

# ---- Enter your OpenWeatherMap API Key here ----
API_KEY = "your_openweather_api_key"  # Get one free at https://openweathermap.org/api

# Function to analyze location
def analyze_location():
    try:
        lat = float(lat_entry.get())
        lon = float(lon_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for latitude and longitude")
        return

    # Fetch weather data from OpenWeather API
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code != 200:
        messagebox.showerror("API Error", "Could not fetch weather data")
        return

    data = response.json()

    # Extract weather details
    temperature = f"{data['main']['temp']}°C"
    humidity = f"{data['main']['humidity']}%"
    weather = data['weather'][0]['description'].capitalize()
    rainfall = "0 mm"
    if "rain" in data and "1h" in data["rain"]:
        rainfall = f"{data['rain']['1h']} mm (last 1h)"

    # ---- Simulated Soil Data (in real case, fetch from soil API or dataset) ----
    # Rule: based on lat/lon (very simplified!)
    if lat > 20 and lon > 80:
        soil_type = "Loamy"
        soil_ph = "6.5"
    else:
        soil_type = "Sandy"
        soil_ph = "7.2"

    # Recommendations logic
    if soil_type == "Loamy":
        crops = "Wheat, Barley, Vegetables"
        irrigation = "Moderate irrigation needed"
        fertilizer = "Use balanced fertilizers"
    else:
        crops = "Millets, Groundnut, Pulses"
        irrigation = "Low irrigation needed"
        fertilizer = "Add organic compost"

    # Display results
    result_text = f"""
*Location Analysis Results*
Temperature: {temperature}
Humidity: {humidity}
Weather Condition: {weather}
Rainfall: {rainfall}
Soil Type: {soil_type}
Soil pH: {soil_ph}

*Recommendations*
Crop Recommendation: {crops}
Irrigation Requirement: {irrigation}
Fertilizer Advice: {fertilizer}
"""
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, result_text)


# ---- GUI setup ----
root = tk.Tk()
root.title("Precision Farming Location Analysis")

tk.Label(root, text="Enter Latitude:").pack()
lat_entry = tk.Entry(root)
lat_entry.pack()

tk.Label(root, text="Enter Longitude:").pack()
lon_entry = tk.Entry(root)
lon_entry.pack()

tk.Button(root, text="Analyze", command=analyze_location).pack(pady=5)

tk.Label(root, text="Analysis Results:").pack()
result_box = tk.Text(root, height=20, width=70)
result_box.pack()

root.mainloop()
