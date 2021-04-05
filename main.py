import tkinter as tk 
import requests
import time, datetime as dt



def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    print(json_data['weather'][0]['main'][0])
    temp = int(json_data['main']['temp'] - 273.15)
    #min_temp = int(json_data['main']['temp_min'] - 273.15)
    #max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    #sunrise = time.strftime('%H:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    #sunset = time.strftime('%H:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Temperature: " + str(temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "hPa" + "\n" +"Humidity: " + str(humidity) + "%"+"\n" + "Wind Speed: " + str(wind) + "m/s" "\n"
    now = dt.datetime.now()
    today = now.strftime("\n""Date: %d/%m/%Y")
    label1.config(text = final_info)
    label2.config(text = final_data)
    label3.config(text = today)


canvas = tk.Tk()
canvas.geometry("500x450")
canvas.title("Weather App" + " Mr.Muzrob 👨🏾‍💻")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")
n = ("poppins", 15, "bold") 
 

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
label3 = tk.Label(canvas, font=n)
label3.pack()

canvas.mainloop() 
