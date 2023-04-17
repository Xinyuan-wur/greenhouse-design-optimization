from design_element_parameters import design_element_parameters
from annuity_factor import annuity_factor

def EAC_lamp(lamp_encode, elec, r):
    """In: lamp_encode, str, single letter, ['B','C',...'I']
           elec:  elec, float, electricity use, kWh/m2, for calculating lamp lamp lifetime in year
           r: discount rate
       Out: float, equivalent annual costs of all design elements
       Embeded functions: design_element_parameters(), annuity_factor()
    """
    parameters = design_element_parameters()
    # ---- bulb -------
    # lighting hour = elec/nr.lamp
    nr_lamp = {'B':0.0281, 'C':0.0562, 'D':0.0843, 'E':0.1124, 'F':0.0161, 'G':0.0323, 'H':0.0484, 'I':0.0645}
    lighting_hour = elec/nr_lamp[lamp_encode] 
    lifetime_bulb = parameters['lifetime']['light'][lamp_encode]
    lifetime_bulb_year = round(lifetime_bulb/lighting_hour,2) # lifetime of lamps in year     
    
    initial_cost_bulb = parameters['cost']['light'][lamp_encode]
    maintenance_bulb = parameters['maintenance']['light'][lamp_encode]
    EAC_bulb = initial_cost_bulb/annuity_factor(r, lifetime_bulb_year) + initial_cost_bulb*maintenance_bulb
    
    # ---- cable -------
    initial_cost_cable = parameters['cost']['light']['cable'][lamp_encode]
    lifetime_cable = parameters['lifetime']['light']['cable']
    maintenance_cable = parameters['maintenance']['light']['cable']
    EAC_cable = initial_cost_cable/annuity_factor(r, lifetime_cable) + initial_cost_cable*maintenance_cable
    
    if lamp_encode in ['B','C','D','E']: # If HPS lamps were used
        # ---- fixtures -------
        initial_cost_fixtures = parameters['cost']['light']['HPS fixtures'][lamp_encode]
        lifetime_fixtures = parameters['lifetime']['light']['HPS fixtures']
        maintenance_fixtures = parameters['maintenance']['light']['HPS fixtures']
        
        EAC_fixture = initial_cost_fixtures/annuity_factor(r, lifetime_fixtures) + initial_cost_fixtures*maintenance_fixtures
    else: # If LED lamps were used
        EAC_fixture = 0

    EAC_lamp = EAC_bulb + EAC_fixture + EAC_cable
    return EAC_lamp
