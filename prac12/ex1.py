cities = ["Київ", "Одеса", "Львів", "Харків", "Житомир"]
city_set = set(cities)

for city in ["Одеса", "Полтава"]:
    if city in city_set:
        print(f"{city} є у списку міст")
    else:
        print(f"{city} відсутнє у списку міст")
