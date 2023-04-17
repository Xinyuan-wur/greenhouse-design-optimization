# greenhouse-design-optimization

### This is a brief description of the code under Genetic search folder.

| Function | Dependent function | Input | Output |
| -------- | -------- | -------- | -------- |
| fixed_costs(string, r, elec) | design_element_parameters(),  annuity_factor(), EAC_lamp(lamp_encode, elec)| string: e.g. DCBABAABA. r: float, discount factor. elec: float, electricity use, kWh/m2, for calculating lamp lifetime in year | float, sum of equivalent annual costs of all design elements |
| EAC_lamp(lamp_encode, elec) | design_element_parameters(), annuity_factor() | lamp_encode: letter | Equivalent annual cost of lamp installation and maintenance|
| annuity_factor(r, n) | none | r: float, discount factor. n: int, lifetime in year | float, a annuity factor |
|variable_costs(location, gas, elec, CO2, gas_price, elec_price, CO2_price, other_costs)| none | location: str. gas: dict, key: month, val: gas use of the month. elec:float, electricity use of all months. CO2: CO2 use, kg/m2. prices: unit prices of gas, elec, and other costs |float, yearly variable costs |
|revenue(location, yield_, tomato_prices)| none | location, yield_: dict, key: month, val: tomato yield of the month, kg/m2. tomato_prices: dict, key: month, val:tomato price of the month, ¥/kg| yearly revenue from selling tomato, ¥/m2|
|prices()| none | none |tomato_price (dict of dict), gas_price (dict of dict), elec_price (dict), CO2_price, other_costs|
|GHG_emission(gas, elec, yield_, location)| none |gas: gas use, unit: m3/m2/year. elec: electricity use, unit: kWh/m2/year. yield_: tomato yield, unit: kg/m2/year|float, GHGs emission per m2|
|run_design(path, filename) (not uploaded) |API_2_csv()|path: "json parameters/{}/{}.json".format(location, filename). filename: '{}_{}'.format(string, location)|Out: API output (csv) saved in the same path & filename|
|API_2_csv(r_dict, path, filename) (not uploaded) | none |r_dict: API response. path:"json. parameters/{location}/{filename}.json". filename: '{}_{}'.format(string, location) |csv output|
|retrieve_API_output(string, location)| none |string, e.g. DCBABAABA. location: str| yield_: dict, key: month, val: tomato yield of the month. gas: dict, key: month, val: gas use. elec: float, electricity use of all months|
|init_population(N)|encoding(), eliminate_illegal_string()|N: size of the initial population|list of strs: the initial design populations|
|eliminate_illegal_string(string)| none |string: str, alphabet-coded design string| original or revised legal string |
|population_eval(population,location)|gen_parameter(), run_design(), retrieve_API_output(), prices(), revenue(), variable_costs(), fixed_costs(), GHG_emission()|population: list of design strings|dict of dict, key1: string, key2s:['yield','gas','elec','revenue','variable_costs', 'fixed_costs', 'operational_income','GHG']|
|GA_log(iteration, location, best_design)|none |best_string, tuple (best_string, dict), dict keys ['yield','gas','elec','revenue','variable_costs','fixed_costs', operational_income','GHG']|add a row to GA log csv |
|new_population(population_score, N, n, p_crossover, p_mutation)| nlargest(), crossover(), mutation() |N: size of population. n: preserve the best n parent designs in the next generation; |list of alphabet-coded strings (next generation after crossover and mutation)|
|nlargest(n, population_score)| none |population_score: dict, key:string, val: float, operating income from population_eval()|dict, key:string, top n designs with the best operating incomes|
|select_parents(population_score)| none |population_score: dict, key:string, val: float, operating income derived from population_eval()|list of design strings, some designs will be selected more than once (a new population with the same population size)|
|crossover(p_crossover, parents, n)| none |p_crossover: float, crossover probability. parents: list of parent strings. n: int, number of preserved elitstic individuals|list, a subset of parent strings selected after crossover|
|mutation(p_mutation, parents) | none |p_mutation: mutation probability. parents: list of strings selected after crossover|a list of strings after mutation|
|genetic_algorithm(p_crossover, p_mutation, N, n, max_iter, location)||max_iter: terminating condition||
