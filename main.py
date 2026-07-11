from calculations import calculate_total, print_report

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

selected_city = input("Which city do you want to check? ").strip().title()

if selected_city in cities:
    city_costs = cities[selected_city]

    total = calculate_total(city_costs)

    print_report(selected_city, city_costs, total)
else:
    print("City not found.")
    print("Availale cities: Chernivtsi, Bucharest, Tbilisi")