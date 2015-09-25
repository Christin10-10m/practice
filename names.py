name = "christin"


def findletters(name):
    eval_dictionary ={}
    for x in list(name):
        if (x not in eval_dictionary):
            eval_dictionary[x] = 1
        elif (x in eval_dictionary):
             eval_dictionary[x] += 1
    print eval_dictionary

findletters(name)