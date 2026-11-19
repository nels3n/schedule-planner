import random

def random_schedule():
    """This function chooses a random schedule with random 
    features we can use as test data"""
    # gaps = random number of hour(s) between classes
    # walk = realistic distance in minutes to walk to a class
    # early = yes or no to a early class
    # friday = having a class on friday - yes or no 
    schedule = {"gaps": random.randint(0,4), "walk": random.randint(1,15), "early": random.randint(0,1), "friday": random.randint(0,1)}
    return schedule



if __name__ == "__main__":
    for i in range(5):
        print(random_schedule())
