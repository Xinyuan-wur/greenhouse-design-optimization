from design_element_parameters import design_element_parameters
from EAC_lamp import EAC_lamp
from annuity_factor import annuity_factor
from prices import prices

def fixed_costs(string, r, elec):
    """Fixed costs as equivalent annual costs
     In: string, e.g. DCBABAABA
         r, float, discount rate
         elec, float, electricity use, kWh/m2, for calculating lamp lifetime in year
     Out: float, sum of equivalent annual costs of all design elements
     Dependent function: design_element_parameters(), annuity_factor(), EAC_lamp(lamp_encode, elec)
     """
    design_element = {0:'structure', 1:'cover', 2:'cooling', 3:'heating',\
                 4:'thermal_screen', 5:'shading_screen', 6:'light', 7:'CO2', 8:'whitewash'}
    
    parameters = design_element_parameters()
    fixed_costs = 0
    for nr, i in enumerate(string):
        element = design_element[nr]
        initial_cost = parameters['cost'][element][i]
        lifetime = parameters['lifetime'][element][i]
        maintenance = parameters['maintenance'][element][i]
        if element != 'light':
            EAC = initial_cost/annuity_factor(r, lifetime) + initial_cost*maintenance
            fixed_costs += EAC
    
    # calculate the fixed costs for screen structure & lamp fixture 
    if string[4] != 'A': # if thermal screen is installed
        structure_costs = parameters['cost']['thermal_screen']['structure']
        structure_lifetime = parameters['lifetime']['thermal_screen']['structure']
        structure_maintenance = parameters['maintenance']['thermal_screen']['structure']
        EAC_structure = structure_costs/annuity_factor(r,structure_lifetime) + structure_costs*structure_maintenance
        fixed_costs += EAC_structure
        
    if string[5] != 'A': # if shading screen is installed
        structure_costs = parameters['cost']['shading_screen']['structure']
        structure_lifetime = parameters['lifetime']['shading_screen']['structure']
        structure_maintenance = parameters['maintenance']['shading_screen']['structure']
        EAC_structure = structure_costs/annuity_factor(r,structure_lifetime) + structure_costs*structure_maintenance
        fixed_costs += EAC_structure
        
    if string[6] != 'A': # if lamps are installed
        EAC_lamp_ = EAC_lamp(string[6], elec, r)
        fixed_costs += EAC_lamp_
       

    return fixed_costs
