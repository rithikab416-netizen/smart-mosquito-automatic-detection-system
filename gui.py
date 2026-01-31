import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

def detect():
    try:
        sound = int(sound_entry.get())
        temp = int(temp_entry.get())
        humidity = int(hum_entry.get())
    except:
        messagebox.showerror("Error", "Please enter valid numbers")
        return

    # AI decision logic
    if sound > 90 and humidity > 70 and temp > 25:
        result_text.set("🔴 MOSQUITO DETECTED\n⚡ Killer Activated")
        result_label.config(fg="red")
        status = "mosquito"
    else:
        result_text.set("🟢 NORMAL CONDITION\nNo Action Needed")
        result_label.config(fg="green")
        status = "normal"

    # Save history
    with open("history.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), sound, temp, humidity, status])

def future_hardware():
    messagebox.showinfo(
        "Future Hardware",
        "In future, this system will connect to:\n"
        "- Sound Sensor\n- DHT11 Sensor\n"
        "- Electric Mosquito Killer\n- IoT (ESP32)"
    )

# GUI window
window = tk.Tk()
window.title("Advanced Mosquito Detection System")
window.geometry("400x450")

tk.Label(window, text="Mosquito Detection System", font=("Arial", 16)).pack(pady=10)

# Inputs
tk.Label(window, text="Sound Level").pack()
sound_entry = tk.Entry(window)
sound_entry.pack()

tk.Label(window, text="Temperature").pack()
temp_entry = tk.Entry(window)
temp_entry.pack()

tk.Label(window, text="Humidity").pack()
hum_entry = tk.Entry(window)
hum_entry.pack()

tk.Button(window, text="Detect", command=detect).pack(pady=15)

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, font=("Arial", 12))
result_label.pack(pady=10)

tk.Button(window, text="Future Hardware Integration", command=future_hardware).pack(pady=10)

window.mainloop()