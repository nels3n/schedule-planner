from planner.learner import predict, STARTING_WEIGHTS, update
from evaluation.simulation import STUDENTS, make_pairs
import matplotlib.pyplot as plt

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
    This function runs the whole test for one simulated student and tracks 
    how the two planners do as picks come in.
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

def plot_results(name,learner,baseline):
    """
    This function creates a line plot of each student
    """
    plt.figure()
    plt.title(f"{name}: Learner vs. Baseline")
    plt.plot(range(len(learner)),learner, label="Learner Accuracy")
    plt.plot(range(len(baseline)),baseline, label="Baseline Accuracy")
    plt.legend()
    plt.xlabel("Picks")
    plt.xticks(ticks=[0,5,10,15,20])
    plt.ylabel("Accuracy")
    plt.ylim(0.5,1)
    plt.savefig(f"evaluation/{name}.png")
    plt.close()




        
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
    # loop over all 3 students - keys and values
    print('-'*30)
    for name,weights in STUDENTS.items():
        # save both lists
        learner,baseline = run_experiment(weights)
        plot_results(name,learner,baseline)
        print(f"Student: {name}, Learner: {learner[-1]:.1%}, Baseline: {baseline[-1]:.1%}")
# sample output 
# Student: hates_early, Learner: 91.5%, Baseline: 85.5%
# Student: hates_gaps, Learner: 74.5%, Baseline: 71.0%
# Student: hates_walking_fridays, Learner: 83.5%, Baseline: 81.0%
# all students improve over the baseline

