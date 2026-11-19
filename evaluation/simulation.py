import random

# max values of features
MAX_VALUES = {"gaps": 4,"walk": 15, "early": 1, "friday": 1}

def random_schedule():
    """This function chooses a random schedule with random 
    features we can use as test data"""
    # gaps = random number of hour(s) between classes
    # walk = realistic distance in minutes to walk to a class
    # early = yes or no to a early class
    # friday = having a class on friday - yes or no 
    schedule = {"gaps": random.randint(0,MAX_VALUES["gaps"]), "walk": random.randint(1,MAX_VALUES["walk"]), "early": random.randint(0,MAX_VALUES["early"]), "friday": random.randint(0,MAX_VALUES["friday"])}
    
    return schedule

def scale_features(schedule):
    """This function will take in a schedule and 
    scale its features on a 0-1 scale"""
    # dictionary to hold the scaled values
    scaled_values = {}
    # loop through the keys of the schedule
    for key in schedule:
        # variable to hold schedule keys divided by their max values to scale
        scaled = schedule[key]/MAX_VALUES[key] 
        # add to dictionary
        scaled_values[key] = scaled

    return scaled_values



if __name__ == "__main__":
    rand = random_schedule()
    print(rand)
    print(scale_features(rand))
