def calculate_total(city_costs):
    
    return (
        city_costs["rent"]
        + city_costs["food"]
        + city_costs["transport"]
        + city_costs["internet"]
    )

def print_report(city_name, city_costs, total):
    print("City cost estimate")
    print(f"City: {city_name}")
    print(f"Rent: ${city_costs['rent']}")
    print(f"Food: ${city_costs['food']}")
    print(f"Transport: ${city_costs['transport']}")
    print(f"Internet: ${city_costs['internet']}")
    print(f"Total: ${total}")