def get_city(city,country,population=''):
    if population:
        name=city.title()+","+country.title()+" - population "+str(population)
    else:
        name=city.title()+","+country.title()
    return name
