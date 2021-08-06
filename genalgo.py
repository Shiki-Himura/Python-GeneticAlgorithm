import random
from random import choice
from sys import exit


class Generation:
    def __init__(self):
        self.parent_strings = []
        self.child_strings = []
        self.target = 'Sein oder nicht sein'
        self.gene_pool = ' aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
        self.population_size = 2000
        self.mut_rate = 1
        self.gen = 0
        self.matchFound = False
        self.best_match = None

    def initialize_parents(self):
        temp_str = ""
        for j in range(len(self.target)):
            temp_str += choice(self.gene_pool)
        self.parent_strings.append(temp_str)

    # generate random strings based on population_size
    def create_parents(self):
        for i in range(self.population_size):
            self.initialize_parents()

    # get random number for the mutation
    # change char of string if mutation is invoked
    def mutate(self, string):
        temp_string = ""
        for char in string:
            mutation = random.randint(0, 100)
            if mutation < 1:
                temp_string += choice(self.gene_pool)
            else:
                temp_string += char
        return temp_string

    # get strings and put 1/2 from each together
    def crossover_selection(self):
        temp_list = self.create_dna_list()
        for i in range(2000):
            rnd_string_one = choice(temp_list)
            rnd_string_two = choice(temp_list)
            temp_one = rnd_string_one[:10]
            temp_one += rnd_string_two[10:]
            string_one = self.mutate(temp_one)
            if string_one == self.target:
                print(string_one)
                self.matchFound = True
                exit()
            self.child_strings.append(string_one)

        self.parent_strings = []
        self.parent_strings = self.child_strings
        self.child_strings = []

    # get list of strings based on matching characters of target and string
    def create_dna_list(self):
        temp_array = []
        best_counter = 0
        for string in self.parent_strings:
            counter = 0
            for i in range(len(string)):
                if string[i] == self.target[i]:
                    temp_array.append(string)
                    counter += 1
            temp_array.append(string)

            if counter > best_counter:
                best_counter = counter
                self.best_match = string
        return temp_array







