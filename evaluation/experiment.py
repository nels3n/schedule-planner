from planner.learner import predict, STARTING_WEIGHTS
from evaluation.simulation import STUDENTS, make_pairs


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

        
if __name__ == "__main__":
    import random
    random.seed(42)
    # 100 test pairs
    test_pairs = make_pairs(STUDENTS['hates_early'],100)
    print(f"Students' weights: {accuracy(test_pairs,STUDENTS['hates_early'])}")
    print(f"Starting weights: {accuracy(test_pairs, STARTING_WEIGHTS)}")
    # sample output: Students' weights: 1.0 , Starting weights: 0.80, baseline starts at around 89%
    # learning has to close the last 20% 
