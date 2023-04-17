import random
from init_population import init_population
from eliminate_illegal_string import eliminate_illegal_string
from population_eval import population_eval

def select_parents(population_score):
    """Tournament selection (binary)
    In: dict of dict, key:string, val: float, derived from population_eval()
    Out: list of design strings, some designs will be selected more than once (a new population with the same population size N)"""
    random.seed(0)
    parents = []
    for i in range(len(population_score)): # N, size of the population
        # without replacement
        player_1 = random.choice(list(population_score.keys()))  # return a random key (index,design) of the first chromosome
        player_2 = random.choice(list(population_score.keys()))

        if population_score[player_1]['operational_income'] >= population_score[player_2]['operational_income']: # add the design with better fitness
            parents.append(player_1) 
        else:
            parents.append(player_2)

    return parents

if __name__ == "__main__":
    location = 'Jinshan'
    r = 0.057  # discount rate
    N = 400
    init_population = init_population(N)
    population_score = population_eval(r, init_population,location)
    parents = select_parents(population_score)
    parents
