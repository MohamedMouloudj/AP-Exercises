cities=[]
input_city=input("Please type in a city: ")
while input_city.lower().strip()!="stop":
    cities.append(input_city.strip())
    input_city=input("Please type in a city: ")

cities_populations={}
for city in cities:
    population=len(city)
    cities_populations[city]=population*1000000

cities_populations_sorted=sorted(cities_populations.items(), key=lambda city: city[1], reverse=True)

for city in cities_populations_sorted:
    print(f"The city {city[0]} has {len(city[0])} letters so its population is {city[1]:,}")