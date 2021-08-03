import random
from random import choice

target = 'Sein oder nicht sein'
pool_lowercase = 'abcdefghijklmnopqrstuvwxyz '
pool_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
parent_strings = []
child_strings = []
population_size = 2000
mut_rate = 1


# initialize randomly generated string and append it to parent-array
def initialize_rnd_str():
    temp_str = ""
    for i in range(0, 20):
        temp_str += choice(pool_lowercase + pool_uppercase)
    parent_strings.append(temp_str)


# get 2000 randomly generated strings
def create_parents():
    for i in range(population_size):
        initialize_rnd_str()


# get random number for the mutation
# change char of string if mutation is invoked
def mutate():
    temp = []
    for string in child_strings:
        for i in string:
            mutation = random.randint(0, 100)
            if mutation < 1:
                print(string)
                 choice(pool_lowercase + pool_uppercase)
        temp.append(string)


# get list of strings * fitness
def create_dna_list():
    temp = []
    for string in parent_strings:
        for i in range(len(string)):
            if string[i] == target[i]:
                temp.append(string)
        temp.append(string)
    return temp


# Get strings and put 1/2 from each together
def crossover_selection():
    temp = create_dna_list()
    for i in range(population_size):
        rnd_string_one = choice(temp)
        rnd_string_two = choice(temp)

        string_one = rnd_string_one[:10]
        string_one += rnd_string_two[10:]
        string_two = rnd_string_one[10:]
        string_two += rnd_string_two[:10]

        child_strings.append(string_one)
        child_strings.append(string_two)


create_parents()
crossover_selection()
mutate()









