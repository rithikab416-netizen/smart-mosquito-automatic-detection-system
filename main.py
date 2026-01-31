import csv

print("Program started...\n")

with open("mosquito_data.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Headers:", reader.fieldnames, "\n")

    for row in reader:
        sound = int(row["sound_level"])
        temperature = int(row["temperature"])
        humidity = int(row["humidity"])
        label = row["label"]

        print(f"Sound={sound}, Temp={temperature}, Humidity={humidity}, Label={label}")

        if sound >= 100 and humidity >= 65:
            print("👉 Mosquito Detected 🚨 → Insect Killer ON\n")
        else:
            print("👉 No Mosquito 🙂\n")
