from encoding import encoding
import random
from eliminate_illegal_string import eliminate_illegal_string

def mutation_operator(p_mutation, string):
    """p_mutation: mutation probability (very small)
    mutation is performed on a bit-by-bit basis
    randomly select a bit to mutate with probability p
    embeded function: encoding()"""

    design_component = encoding() # dict of dict, key1:(1-9); key2:[A,B,...]
    for ind,bit in enumerate(string):
        r = random.random()
        if r <= p_mutation: # mutate this bit
            candidate_bits = list(design_component[ind+1].keys())
            candidate_bits.remove(bit) # remove this bit from the list of this design compnents options
            new_bit = random.choice(candidate_bits)
            string = string[:ind] + new_bit + string[ind+1:]
            string = eliminate_illegal_string(string)
    return string
         
def mutation(p_mutation, parents):
    """p_mutation: float, p_mutation probability of a single bit
       In: parents, list of parent strings after crossover
       Out: list, a list of strings after mutation
       embeded function: mutation_operator()"""
    population = []
    for parent in parents:
        mutated = mutation_operator(p_mutation, parent)
        population.append(mutated)
    return population

