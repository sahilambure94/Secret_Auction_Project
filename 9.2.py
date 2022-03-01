# Nesting Dictionaries in List
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]


def add_new_country(country_visited, cities_visited, times_visited):
    new_country = {
        "country": country_visited,
        "cities_visited": cities_visited,
        "total_visits": times_visited
    }
    travel_log.append(new_country)


add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)
add_new_country("India", ["Delhi", "Mumbai", "Punjab", "Kashmir"], 26)

for i in travel_log:
    print(i)
