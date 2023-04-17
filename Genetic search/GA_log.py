import csv
from decode_string import decode_string


def GA_log(iteration, location, best_design):
    """In: best_string, tuple (best_string, dict),
           dict keys ['yield','gas','elec','revenue','variable_costs','fixed_costs', operational_income','GHG']
       Out: add a row on csv
       Dependent function: decode_string()"""
    info = {}
    info['Iteration'] = iteration
    info['Best design'] = best_design[0]
    info['operational_income'] = best_design[1]['operational_income']
    info['Decoded design string'] = decode_string(best_design[0])
    info['Total yield'] = best_design[1]['yield']
    info['Total gas'] = best_design[1]['gas']
    info['Total elec'] = best_design[1]['elec']
    info['revenue'] = best_design[1]['revenue']
    info['fixed costs'] = best_design[1]['fixed_costs']
    info['variable costs'] = best_design[1]['variable_costs']
    info['GHG'] = best_design[1]['GHG']
    
    with open('{}/GA best score {}.csv'.format(location, location), 'a+', newline="") as f:
        writer = csv.DictWriter(f, fieldnames =list(info.keys()))
        writer.writerow(info)
        f.close()
