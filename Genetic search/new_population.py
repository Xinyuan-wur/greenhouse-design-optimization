from nlargest import nlargest
from crossover import crossover
from mutation import mutation
from select_parents import select_parents

def new_population(population_score, N, n, p_crossover, p_mutation):
    """In: dict, key:string, val: float, profit of the given string
    N: int, size of population/generation
    n: preserve the best n parent designs in the next generation
    Elitist preservation 保留最好的n个亲本，其余亲本进入mating pool，替换为子代
    p_crossover, p_mutation: float
    Out: list of alphabet-coded strings (next generation after crossover and mutation)
    embedded functions: nlargest(), select_parents(), crossover(), mutation()"""
    # initialize new population, preserve the top n parents from the current population 初始化新群体，保留上代最优的三个设计
    new_population = nlargest(n, population_score)
    # select parents through tournament selection 锦标赛选择亲本
    parents = select_parents(population_score)
    print('parents pool repetitive_rate', round((N - len(set(parents)))/N, 2))

    # crossover 进行交叉互换
    after_crossover = crossover(p_crossover, parents, N, n)
    print('after_crossover repetitive_rate', round((N - len(set(after_crossover))) / N, 2))

    # mutation 进行突变
    after_mutation = mutation(p_mutation, after_crossover)
    print('after_mutation repetitive_rate', round((N - len(set(after_mutation))) / N, 2))
    # merge elistic preserved individuals & individuals obtained after crossover & mutation 
    new_population.extend(after_mutation)

    repetitive_rate = round((N - len(set(new_population)))/N, 2)
    print('repetitive_rate', repetitive_rate)
    return new_population
