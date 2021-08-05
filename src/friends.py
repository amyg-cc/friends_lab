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

def add_friend(person, new_friend):
    person["friends"].append(new_friend)

def remove_friend(person, friend):
    person["friends"].remove(friend)

def total_money(list):
    money_total = 0

    for person in list:
        money_total += person["monies"]
    return money_total

def lend_money(lender, lendee, amount):
    lendee["monies"] += amount
    lender["monies"] -= amount

def all_favourite_foods(list):
    favourites_list = []

    for person in list:
        for snack in person["favourites"]["snacks"]:
            favourites_list.append(snack)
    return favourites_list

def find_no_friends(list):
    no_mates = []
    for person in list:
        if len(person["friends"]) == 0:
            no_mates.append(person)
    return no_mates

def find_mutual_friends(person_1, person_2):
    mutual_mates = []
    for friend in person_1["friends"]:
        if friend in person_2["friends"]:
            mutual_mates.append(friend)
    return mutual_mates

def find_people_who_like_tv_show(tv_show, list):
    like_tv_show = []
    for person in list:
        if person["favourites"]["tv_show"] == tv_show:
            like_tv_show.append(person)
    return like_tv_show

def find_oldest_person(list):
    oldest_person = list[0]
    
    for person in list:
        if person["age"] > oldest_person["age"]:
            oldest_person = person
    return oldest_person
