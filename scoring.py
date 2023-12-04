import parse_ground_truth

def score(answer_file, system_file, list = False):
    correct = 0
    no_system = 0
    answer_region = parse_ground_truth.parse(answer_file)
    no_answer = len(answer_region)
    if list == False:
        system = open(system_file, 'r')
        for end in system:
            if end == '\n':
                break
            end = int(end)
            if end in answer_region:
                correct += 1
            no_system += 1
    else: 
        for end in system_file:
            if end in answer_region:
                correct += 1
        no_system = len(system_file)
    return correct, no_system, no_answer



