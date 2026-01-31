import csv

mosquito_count = 0
normal_count = 0

with open("mosquito_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["label"].strip().lower() == "mosquito":
            mosquito_count += 1
        else:
            normal_count += 1

print("Mosquito detected samples:", mosquito_count)
print("Normal samples:", normal_count)

if mosquito_count > normal_count:
    print("⚠️ Mosquito risk HIGH – Turn ON killer")
else:
    print("✅ Normal condition – No action needed")