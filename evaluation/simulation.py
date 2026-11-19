import random
from planner.scoring import MAX_VALUES, scale_features, score_schedule


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

def student_pick(schedule_a,schedule_b, weights):
    """This function will get the scores of two random schedules and compare their scores"""
    # gets scores for each schedule
    score_a = score_schedule(schedule_a,weights)
    score_b = score_schedule(schedule_b,weights)
    # compare scores
    if score_a < score_b:
        return "A"
    else:
        return "B"

def make_pairs(weights,num_pairs):
    """This function will generate random schedule pairs (A and B), filter out ties,
    Record the correct anser for each pair (one the student picks) and return the full list (num_pairs)"""
    # empty list to hold the pairs
    pairs = []
    # keep going while the length of pairs is less than the number of pairs needed
    while len(pairs) < num_pairs:
        # create two random schedules
        schedule_a = random_schedule()
        schedule_b = random_schedule()
        # get the scores of each
        score_a = score_schedule(schedule_a,weights)
        score_b = score_schedule(schedule_b,weights)
        # compare if a tie - ignore
        if score_a == score_b:
            continue
        # get result
        result = student_pick(schedule_a,schedule_b,weights)
        # append to list of pairs
        pairs.append({"a": schedule_a,"b": schedule_b,"answer": result})

    return pairs
        
    
if __name__ == "__main__":

    # random schedule
    schedule_a = random_schedule()
    schedule_b = random_schedule()
    print(f"Random schedule features for A: {schedule_a}")
    print(f"Random schedule features for B: {schedule_b}")
    print(f"Features scaled (0-1) for A: {scale_features(schedule_a)}")
    print(f"Features scaled (0-1) for B: {scale_features(schedule_b)}")
    print(f"Score A: {score_schedule(schedule_a,STUDENTS['hates_early'])}")
    print(f"Score B: {score_schedule(schedule_b,STUDENTS['hates_early'])}")
    print(f"Schedule {student_pick(schedule_a,schedule_b,STUDENTS['hates_early'])} WINS!")
    print('-'*30)
    # known answer - 'hates_early' student will pick schedule b
    test_a = {"gaps": 0, "walk": 5, "early": 1, "friday": 0}
    test_b = {"gaps": 0, "walk": 5, "early": 0, "friday": 0}
    print(f"Schedule {student_pick(test_a,test_b,STUDENTS['hates_early'])} WINS!")
    print('-'*30)
    # make 5 pairs for 'hates_early' student
    test_pairs = make_pairs(STUDENTS['hates_early'],5)
    print(f"Test pairs: {len(test_pairs)}")
    # print each pair
    for pairs in test_pairs:
        print(pairs)
# Sample output: {'a': {'gaps': 1, 'walk': 13, 'early': 0, 'friday': 0}, 
# 'b': {'gaps': 3, 'walk': 6, 'early': 1, 'friday': 0}, 'answer': 'A'}
# ^^ Student picks A, accepting to walk more than twice as long to avoid the 8am class - Exactly how hates-early would behave
