def get_city_country(city,country,population=""):
    if population:
        city_country = city +", "+country+" - "+str(population)
    else:
        city_country=city +" "+country
    return city_country
