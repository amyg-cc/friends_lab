def get_name(person): 
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    snack_match = False
    for snack in person["favourites"]["snacks"]:
        if food in person["favourites"]["snacks"]:
            snack_match = True
    return snack_match