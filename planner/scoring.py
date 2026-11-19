# max values of features
MAX_VALUES = {"gaps": 4,"walk": 15, "early": 1, "friday": 1}

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
