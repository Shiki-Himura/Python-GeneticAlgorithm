import random
from random import choice

target = 'Sein oder nicht sein'
pool_lowercase = 'abcdefghijklmnopqrstuvwxyz '
pool_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
parent_strings = []
child_strings = []
population_size = 2000
mut_rate = 1
fitness = 0


# initialize randomly generated string and append it to parent-array
def initialize_rnd_str():
    temp_str = ""
    for i in range(0, 20):
        temp_str += choice(pool_lowercase + pool_uppercase)
    parent_strings.append(temp_str)


# get 2000 randomly generated strings
def create_parents():
    for i in range(0, 2000):
        initialize_rnd_str()


# get random number for the mutation
# change char of string if mutation is invoked
# def mutate():


# get list of strings * fitness
def create_fitness_list():
    global fitness
    index = 0
    for string in parent_strings:
        for char in string:
            if char == target[index]:
                fitness += 1
                index += 1
                child_strings.append(string * fitness)
            fitness = 0
        index = 0


#def crossover_selection():
# Implement mutation method. Implement selection method for child strings


create_parents()
print(parent_strings)
create_fitness_list()









