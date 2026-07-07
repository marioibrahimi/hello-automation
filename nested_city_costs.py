cities = {
    "Chernivtsi": {
        "rent": 300,
        "food": 250,
        "transport": 30,
        "internet": 15,
    },
"Bucharest": {
    "rent": 500,
    "food": 300,
    "transport": 50,
    "internet": 10,
},
"Tbilisi": {
    "rent": 450,
    "food": 280,
    "transport": 35,
    "internet": 15,
},
}

chernivtsi_total = (
    cities["Chernivtsi"]["rent"]
    + cities["Chernivtsi"]["food"]
    + cities["Chernivtsi"]["transport"]
    + cities["Chernivtsi"]["internet"]

)

print("City cost estimate")
print("City: Chernivtsi")
print(f"Rent: ${cities['Chernivtsi']['rent']}")
print(f"Food: ${cities['Chernivtsi']['food']}")
print(f"Transport: ${cities['Chernivtsi']['transport']}")
print(f"Internet: ${cities['Chernivtsi']['internet']}")
print(f"Total: ${chernivtsi_total}")

bucharest_total = (
    cities["Bucharest"]["rent"]
    + cities["Bucharest"]["food"]
    + cities["Bucharest"]["transport"]
    + cities["Bucharest"]["internet"]
)

tbilisi_total = (
    cities["Tbilisi"]["rent"]
    + cities["Tbilisi"]["food"]
    + cities ["Tbilisi"]["transport"]
    + cities["Tbilisi"]["internet"]
)

print()
print("All city totals")
print(f"Chernivtsi total: ${chernivtsi_total}")
print(f"Bucharest total: ${bucharest_total}")
print(f"Tbilisi total: ${tbilisi_total}")
