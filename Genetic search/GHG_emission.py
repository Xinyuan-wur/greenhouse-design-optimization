def GHG_emission(gas, elec, yield_, location):
    """gas: gas use, unit: m3/m2/year
       elec: electricity use, unit: kWh/m2/year
       yield_: tomato yield, unit: kg/m2/production cycle
       total_emission: total GHGs from using gas and electricity per m2 floor area
       or unit_emission: GHGs emission from using gas and electricity for per kg tomato produced
       """
    #-------------- Parameters --------------
    # emission factors of LNG,  unit: kg/TJ
    LNG_EF = {'CO2':64200, 
             'CH4': 10,
             'NO2': 0.6} # 
    
    # global warming potentials (GWP) of different gases,  unit: kg CO2e/kg
    GWP = {'CO2': 1, 
           'CH4': 28,
           'NO2': 265} 
    
    # emission factors of electricity,  unit: kg CO2e/kWh
    Elec_EF = {'Langfang':  0.9236,
               'Weifang':   0.8007,
               'Jinshan':   0.6392,
               'Pingliang': 0.5312 }
    
    #-------------- Convert gas (m3) into net calorific value (TJ) --------------
    # 1 ton LNG = 51434 MJ, 1kg LNG =51.434 MJ
    # 1 m3 natural gas = 38.921 MJ 
    # 1 ton LNG = 1320 m3 natural gas  --> 1 m3 = 1000/1320 kg LNG,  38.921 ~= 1000/1320*51.434 
    # 1 TJ = 1000 GJ, 1 GJ = 1000 MJ 
    # 1 m3 natural gas = 38.921 MJ = 38.921/1000,000 TJ
    total_gas = sum(gas[i] for i in gas.keys())
    LNG_emission = total_gas*38.921/1000000*(LNG_EF['CO2']*GWP['CO2'] + LNG_EF['CH4']*GWP['CH4'] + LNG_EF['NO2']*GWP['NO2']) 
    elec_emission = elec*Elec_EF[location]
    total_emission = LNG_emission + elec_emission  # unit: kg CO2e /m2/year
    total_yield = sum(yield_[i] for i in yield_.keys())
    unit_emission = total_emission/total_yield

    return total_emission
