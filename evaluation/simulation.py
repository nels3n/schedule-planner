import random

# max values of features
MAX_VALUES = {"gaps": 4,"walk": 15, "early": 1, "friday": 1}

# create fake students
# 0-5 scale determines how much this student dislikes this feature
# 0 = doesn't care, 5 = I HATE THIS!
STUDENTS = {
    "hates_early": {"gaps": 0,"walk": 3, "early": 5, "friday": 2},
    "hates_gaps": {"gaps": 5,"walk": 1, "early": 0, "friday": 1},
    "hates_walking_fridays": {"gaps": 2,"walk": 4, "early": 1, "friday": 5}
}

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

def score_schedule(schedule, weights):
    """This function will loop over the scaled features from a schedule and 
    weights given by a student's dislikes, multiply and add them up to get a total score """
    # call scale_features on schedule so scaling is not forgotten
    scaled_schedule = scale_features(schedule)
    # initiate a total
    total = 0
    # loop over keys in scaled_schedule
    for key in scaled_schedule:
       # multiply the features and weights and add them to the total
       total += scaled_schedule[key]*weights[key]

    return total

if __name__ == "__main__":
    # random schedule
    rand = random_schedule()
    print(f"Random schedule features: {rand}")
    print(f"Features scaled: {scale_features(rand)}")
    print(f"Score: {score_schedule(rand,STUDENTS["hates_early"])}")
