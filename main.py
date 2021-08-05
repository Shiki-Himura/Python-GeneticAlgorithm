import genalgo

# refactor program with classes

#create starting population values
genalgo.create_parents()
gen = 0

#condition when to end the program
while not genalgo.matchFound:
    genalgo.crossover_selection()
    gen += 1
    print(genalgo.best_match, gen)











