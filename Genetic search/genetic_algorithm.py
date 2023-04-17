import random
from init_population import init_population
from population_eval import population_eval
from all_string_record import all_string_record
from GA_log import GA_log
from new_population import new_population

def genetic_algorithm(r, p_crossover, p_mutation, N, n, max_iter, location):
    """
    r: float, discount rate
    p_crossover, p_mutation: float, probability of crossover/mutation
    N: int, size of each generation, usually N= 25*(nr of bits)
    n: int, preserve the best n parent designs in the next generation
    max_iter: int, stopping condition after the number of explored designs reached max_iter
    initial_population: list of alphabet-coded strings
    current_population: list of alphabet-coded strings
    explored_designs: set of alphabet-coded strings
    best_design: tuple (alphabet-coded string, float)
    coverage_percent: float (percent of already explored designs)
    population_score: dict, key: alphabet-coded string, val: float
    
    Embeded functions: init_population(), population_eval(), all_string_record(), GA_log(), new_population()
    """
    # -------------------- Intialization ----------------------
    total_designs = 1360797 # total number of design alternatives
    # number of explored unique designs 已探索的design个数
    explored_designs = set() 
    coverage_percent = 0 # percentage of designs explored
    best_design = (None, {'operational_income':-9999999}) # best design and score so far, 初始化最高得分

    # generate initial population 生成初始群体
    initial_population = init_population(N)
    # print(initial_population)
    current_population = initial_population # assign initial population as the current population指定初始群体为当前群体

    # -------------------- Main loop --------------------
    for i in range(max_iter):
        print('Now at iteration {}'.format(i))
        # -------------------- One iteration ----------------------
        # calculate econ&env fitness score for each design in the current_population   对当前群体计算fitness得分
        population_score = population_eval(r, current_population,location)
        # record results of all strings in csv
        all_string_record(population_score, location)

        # print('\ncurrent population scores:',population_score)
        # 将计算过得分的design加到explored design集合中
        explored_designs.update(current_population)
        # print(explored_designs)
        # get the best operational_income of the current population 更新当前群体的最高利润
        current_best_string = max(population_score, key= lambda x: population_score[x]['operational_income'])
        # compare it with the best_socre so far 将当前群体的最高利润和至今最高利润作比较
        if population_score[current_best_string]['operational_income'] > best_design[1]['operational_income']:
            best_design = (current_best_string, population_score[current_best_string]) # update so-far best design

        # record this iteration in csv file 在csv里记录结果
        GA_log(i, location, best_design)
        coverage_percent = len(explored_designs)/total_designs

        # population after mutation   得到下一代群体
        # random.seed(i)
        next_population = new_population(population_score, N, n, p_crossover, p_mutation)
        current_population = next_population # 更新指定下一代群体
        print('best_design', best_design)
        print('next population:', current_population)


#     print('\nThe sofar best design is: ', best_design, 'We already explored {} designs , takes up {} of all design alternatives'.format(len(explored_designs),coverage_percent))

    return best_design, explored_designs

