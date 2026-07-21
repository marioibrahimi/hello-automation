original_text = "  TBILISI  "

stripped_text = original_text.strip()
lowercase_text = original_text.lower()
title_text = original_text.title()
clean_city = original_text.strip().title()

print(f"[{original_text}]")
print(f"[{stripped_text}]")
print(f"[{lowercase_text}]")
print(f"[{title_text}]")
print(f"[{clean_city}]")

cities_text = "Bucharest,Tbilisi,Chernivtsi"
city_list = cities_text.split(",")

print(city_list)
print(city_list[0])
print(city_list[1])
print(city_list[2])