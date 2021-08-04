import random
from random import choice
from sys import exit

target = 'Sein oder nicht sein'
gene_pool = 'aAbBcCdDeEfFgGhHiIjJkK lLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
parent_strings = []
child_strings = []
population_size = 2000
mut_rate = 1
matchFound = False
best_match = None


def initialize_parents():
    temp_str = ""
    for j in range(len(target)):
        temp_str += choice(gene_pool)

    parent_strings.append(temp_str)


# get 2000 randomly generated strings
def create_parents():
    for i in range(population_size):
        initialize_parents()


# get random number for the mutation
# change char of string if mutation is invoked
def mutate(string):
    temp_string = ""
    for char in string:
        mutation = random.randint(0, 100)
        if mutation < 1:
            temp_string += choice(gene_pool)
        else:
            temp_string += char
    return temp_string


# get list of strings based on matching characters with target
def create_dna_list():
    global best_match
    temp_array = []
    best_counter = 0

    for string in parent_strings:
        counter = 0
        for i in range(len(string)):
            if string[i] == target[i]:
                temp_array.append(string)
                counter += 1
        temp_array.append(string)

        if counter > best_counter:
            best_counter = counter
            best_match = string

    return temp_array


# Get strings and put 1/2 from each together
def crossover_selection():
    global parent_strings, child_strings, matchFound
    temp_list = create_dna_list()
    for i in range(1000):
        rnd_string_one = choice(temp_list)
        rnd_string_two = choice(temp_list)
        temp_one = rnd_string_one[:10]
        temp_one += rnd_string_two[10:]
        temp_two = rnd_string_one[10:]
        temp_two += rnd_string_two[:10]
        string_one = mutate(temp_one)
        string_two = mutate(temp_two)

        if string_one == target:
            print(string_one)
            matchFound = True
            exit()
        elif string_two == target:
            print(string_two)
            matchFound = True
            exit()

        child_strings.append(string_one)
        child_strings.append(string_two)

    parent_strings = []
    parent_strings = child_strings
    child_strings = []


#create starting point
create_parents()
gen = 0
#condition when to end the program
while not matchFound:
    crossover_selection()
    gen += 1
    print(best_match, gen)

print(parent_strings)










