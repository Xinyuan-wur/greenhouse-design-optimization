from gen_parameter import gen_parameter
from run_design import run_design
from retrieve_API_output import retrieve_API_output
from revenue import revenue
from variable_costs import variable_costs
from fixed_costs import fixed_costs
from GHG_emission import GHG_emission
from prices import prices
import os.path

def population_eval(r, population, location):
    """
    r: discount rate
    population, list of alphabet-coded design strings
    Out, dict of dict, key1: string, key2s:['yield','gas','elec','revenue','variable_costs', 'fixed_costs', 'operational_income','GHG']
    Embeded function: gen_parameter(), run_design(), retrieve_API_output(), prices(), revenue(), variable_costs(), fixed_costs(), GHG_emission()
    """
    # import prices
    tomato_prices, gas_price, elec_price, CO2_price, other_costs = prices()
    
    population_score = {}
    for string in population:
        # initiate parameters for this design string
        path, filename = gen_parameter(string, location)
        
        output_path = 'API outputs/{}/{}_{}.csv'.format(location, string, location)
        if not os.path.exists(output_path):
            # run simulation for this design string 
            run_design(path, filename)
            
        # retrive yield, gas, and electricity use
        yield_, gas, elec, CO2 = retrieve_API_output(string, location)
        # ----- economic evaluation ------
        revenue_ = revenue(location, yield_, tomato_prices)
        variable_costs_ = variable_costs(location, yield_, gas, elec, CO2, gas_price, elec_price, CO2_price, other_costs)
        fixed_costs_ = fixed_costs(string, r, elec)
        operational_income = -fixed_costs_ + revenue_ - variable_costs_
        # ----- environmental evaluation ------
        GHG = GHG_emission(gas, elec, yield_, location)
        
        population_score[string] = {'yield': sum(yield_[i] for i in yield_.keys()),
                                    'gas': sum(gas[i] for i in gas.keys()),
                                    'elec': elec,
                                    'revenue': revenue_,
                                    'variable_costs': variable_costs_,
                                    'fixed_costs': fixed_costs_ ,
                                    'operational_income': operational_income,
                                    'GHG': GHG}
    return population_score