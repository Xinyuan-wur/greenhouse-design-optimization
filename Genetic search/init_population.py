from encoding import encoding
from eliminate_illegal_string import eliminate_illegal_string
import random

def random_string():
    """Randomly generate one alphabet-coded design string
    Dependent function: eliminate_illegal_string() """
    # dict of dict: key1-position, val1-design component; key2-letter, val2-design component alternative
    encode = encoding()
    string = ''
    for i in encode.keys():
        string += random.choice(list(encode[i].keys()))
    # check if the generated string is a legal stirng
    legal_string = eliminate_illegal_string(string)
    return legal_string



def init_population(N):
    """In:  N, size of the initial population
       Out: list of alphabet-coded design string
       Dependent function: encoding(), random_string(), eliminate_illegal_string() 
    """
    population = []
    for i in range(N):
        random.seed(i)
        string = random_string()
        population.append(string)
    print('There are {} repetitive strings in the initial population'.format(N-len(set(population))))

    return population



if __name__ == "__main__":
    N = 400
    init_population(N)
        