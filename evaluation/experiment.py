from planner.learner import predict, STARTING_WEIGHTS, update
from evaluation.simulation import STUDENTS, make_pairs

# variables for training and test pairs
# more test pairs for a better measure of accuracy 
NUM_TEST = 200
# we initally said 5-10 test pairs but need to advocate for leveling off 20-30 might be more realistic - what learner learns from - check output
NUM_TRAIN = 20

def accuracy(pairs,weights):
    """
    This function is given a list of pairs and a set of weights, it will return
    the share of pairs where predict() matches the stored answer
    """
    # counter for correct predictions
    count = 0
    for pair in pairs:
        # get schedule_a, get schedule_b, correct answer
        result = predict(pair["a"],pair["b"],weights)
        # if the prediction is equal to the stored answer: count + 1
        if result == pair["answer"]:
            count += 1
    return count/len(pairs)

def run_experiment(student_weights):
    """

    """
    # training pairs and test pairs
    train_pairs = make_pairs(student_weights,NUM_TRAIN)
    test_pairs = make_pairs(student_weights,NUM_TEST)
    # set to starting weights because update() never changes dictionary given
    # baseline is untouched because it does not learn
    learner_weights = STARTING_WEIGHTS
    # lists for accuracies of learner and baseline
    learner_acc = []
    baseline_acc = []
    # starting point is 0 for both
    learner_acc.append(accuracy(test_pairs,learner_weights))
    baseline_acc.append(accuracy(test_pairs,STARTING_WEIGHTS))
    # looping over training pairs
    for pair in train_pairs:
        # predict with pair's scheudle and learner's current weights
        learn_predict = predict(pair["a"],pair["b"],learner_weights)
        # if wrong answer
        if learn_predict != pair["answer"]:
            # update leaner_weights
            learner_weights = update(pair["a"],pair["b"],learner_weights,pair["answer"])
        learner_acc.append(accuracy(test_pairs,learner_weights))
        baseline_acc.append(accuracy(test_pairs,STARTING_WEIGHTS))
    return learner_acc, baseline_acc

        
if __name__ == "__main__":
    import random
    random.seed(42)
    # 100 test pairs
    test_pairs = make_pairs(STUDENTS['hates_early'],100)
    print(f"Students' weights: {accuracy(test_pairs,STUDENTS['hates_early'])}")
    print(f"Starting weights: {accuracy(test_pairs, STARTING_WEIGHTS)}")
    print(f"Experiment (LEARNER,BASELINE): {run_experiment(STUDENTS['hates_early'])}")
    # sample output: Students' weights: 1.0 , Starting weights: 0.80, baseline starts at around 89%
    # learning has to close the last 20% 

# After output: hate_early's real weights are gaps: 0, walk: 3, earl: 5 and friday: 2
# so the planner is moving toawrds the right output but it has not reached the true values
# BUT it is learning! Both start at 85.5% learner climbs to 95.5% by pick 11 so actually our 5-10 picks was pretty close.
