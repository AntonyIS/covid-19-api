def normalize(country_name):
    names = [name.capitalize() for name in country_name.replace("-", " ").split()]
    print(" ".join(names))


normalize("antony-injila-shikubu")