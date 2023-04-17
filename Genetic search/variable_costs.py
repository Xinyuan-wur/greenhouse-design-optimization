def variable_costs(location, yield_, gas, elec, CO2, gas_price, elec_price, CO2_price, other_costs):
    """In: location, str, ['Jinshan', 'Langfang', 'Weifang', 'Pingliang']
           yield_: dict, key: month, val: tomato yield of the month, kg/m2
           gas, dict, key: month, val: gas use of the month, m3/m2
           elec:float, electricity use, kWh/m2 of all months
           CO2: CO2 use, kg/m2
           prices: unit prices of gas, elec, and other costs
       Out: float, variable costs of production ¥/m2
    """
    gas_costs = sum(gas[i]*gas_price[location][i] for i in gas.keys())
    elec_costs = elec*elec_price[location]
    CO2_costs = CO2*CO2_price
    
    # labour costs = harvest labour costs + non-harvest labour costs
    # non-harvest labour = 0.64 hour/m2/year, same for each location
    # harvest labour is yield-dependent, 0.032 hour/kg/year (X.Min et al, 2021)
    total_yield = sum(yield_.values())
    wage = {'Jinshan':16.9, 'Langfang':13.3, 'Weifang':11.5, 'Pingliang':9.35} #  ¥/hour 
    
    # basic elec use = 5.67 kWh/m2 (for other small machineries. INTKAM-KASPRO only simulates elec use for major machinery)
    basic_elec = 5.67*elec_price[location]
    labour_costs = 0.64*wage[location] + total_yield*0.032*wage[location]
    
    variable_costs = gas_costs + elec_costs + CO2_costs + labour_costs + other_costs[location] + basic_elec

    return variable_costs
