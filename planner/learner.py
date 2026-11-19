from planner.scoring import score_schedule,scale_features


# Planner does not know anything about the student - 3 acts as indifference
STARTING_WEIGHTS = {"gaps": 3, "walk": 3, "early": 3, "friday": 3}
# constant learning rate we chose
LEARNING_RATE = 0.5 


def predict(schedule_a,schedule_b,weights):
    """
    This function will return the planner's guess by getting the scores of two schedules and comparing
    """
    # gets scores for each schedule
    score_a = score_schedule(schedule_a,weights)
    score_b = score_schedule(schedule_b,weights)
    # compare scores
    if score_a < score_b:
        return "A"
    else:
        return "B"

def update(schedule_a,schedule_b,weights,answer):
    """
    This function will adjust the weights when the planner is wrong by our learning rate 0.5
    """
    # set picked/rejected 
    if answer == "A":
        picked = schedule_a
        rejected = schedule_b
    else:
        picked = schedule_b
        rejected = schedule_a 
    
    scaled_picked = scale_features(picked)
    scaled_rejected = scale_features(rejected)
    new_weights = {}
    # for each weight here - figure out the new value
    for key in weights:
        difference = scaled_rejected[key] - scaled_picked[key]
        new_weight = weights[key] + LEARNING_RATE * difference
        # add to dictionary
        new_weights[key] = new_weight

    return new_weights





if __name__ == "__main__": 
    from evaluation.simulation import student_pick, STUDENTS
    
    print()
    test_a = {"gaps": 0, "walk": 5, "early": 1, "friday": 0}
    test_b = {"gaps": 0, "walk": 5, "early": 0, "friday": 0}
    print(f"Planner predicts: Schedule {predict(test_a,test_b,STARTING_WEIGHTS)} will win...")
    print(f"Student picks: Schedule {student_pick(test_a,test_b,STUDENTS['hates_early'])} WINS!")

    print('-'*30)
    test_c = {"gaps": 0, "walk": 1, "early": 1, "friday": 0}
    test_d = {"gaps": 4, "walk": 3, "early": 0, "friday": 0}
    print(f"Planner predicts: Schedule {predict(test_c,test_d,STARTING_WEIGHTS)} will win...")
    print(f"Student picks:  Schedule {student_pick(test_c,test_d,STUDENTS['hates_early'])} WINS!")
    new_weights = update(test_c,test_d,STARTING_WEIGHTS,"B")
    print(f"New Weights: {new_weights}")
    print(f"Planner updates:  Schedule {predict(test_c,test_d,new_weights)} WINS!")
    print(STARTING_WEIGHTS)
    print()

# planner thinks 4 hours of gaps in test D are worse so it picks C - this is the fix, the learning aspect (need to put in report)
# whereas 'hates_early' student picks D because 
# they would rather wait around than have an 8am


