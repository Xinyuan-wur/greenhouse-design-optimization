import random
from eliminate_illegal_string import eliminate_illegal_string

def crossover_operator(parent_1, parent_2):
    """one point crossover is operated on the individuals with prob p
    In: parent_1,2, alphabet-coded design stings
    Out: two offspring strings """
    # ==== one-point crossover =======
#     pos = random.randint(1, len(parent_1)-1)  # randomly select a bit position, excluding index 0 and 9
#     offspring_1 = parent_1[:pos] + parent_2[pos:]
#     offspring_2 = parent_2[:pos] + parent_1[pos:]
    
    # ==== two-point crossover =======
    a = random.randint(1, len(parent_1)-1)
    b = random.randint(1, len(parent_1)-1)
    pos_1 = min(a,b)
    pos_2 = max(a,b)
    offspring_1 = parent_1[:pos_1] + parent_2[pos_1:pos_2+1] + parent_1[pos_2+1:]
    offspring_2 = parent_2[:pos_1] + parent_1[pos_1:pos_2+1] + parent_2[pos_2+1:]
    offspring_1 = eliminate_illegal_string(offspring_1)
    offspring_2 = eliminate_illegal_string(offspring_2)
    return offspring_1, offspring_2


def crossover(p_crossover, parents, N, n):
    """p_crossover: float, crossover probability
       In: parents, list of parent strings
       N: population size
       n: number of preserved elitstic individuals 
       Out: list, a subset of parent strings selected after crossover"""

    population = []
    # initialize mating pool 
    mating_pool = []
    for design in parents:
        if random.random() <= p_crossover:
            mating_pool.append(design) 
        else:
            population.append(design) # add non-crossover parent to population
    # avoiding empty mating pool
    if len(mating_pool) <2:  # if all parents were not selected for crossover, force random two parents to enter mating pool
        player_1 = random.choice(population)
        population.remove(player_1)
        mating_pool.append(player_1)
        player_2 = random.choice(population)
        population.remove(player_2)
        mating_pool.append(player_2)
    
    current_population_size = len(population)
    while current_population_size < N-n:
        parent_1 = random.choice(mating_pool)
        parent_2 = random.choice([i for i in mating_pool if i != parent_1])
        offspring_1, offspring_2 = crossover_operator(parent_1, parent_2)
        population.append(offspring_1) 
        current_population_size = len(population)
        if current_population_size < N-n: # if current_population_size = N, stop adding more offspring
            population.append(offspring_2) 
        current_population_size = len(population)

    return population

    

