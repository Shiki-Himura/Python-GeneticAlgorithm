import genalgo

Evo = genalgo.Generation()
Evo.create_parents()  # create starting population values
while not Evo.matchFound:  # condition when to end the program
    Evo.crossover_selection()
    Evo.gen += 1
    print(Evo.best_match, Evo.gen)











