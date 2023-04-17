def design_element_parameters():
    """Out: dict of dict of dict, 
        key_1: {'cost', 'lifetime', 'maintenance'},
        key_2: {'structure', 'cover', 'cooling', 'heating', 'thermal_screen', 'shading_screen', 'light', 'CO2', 'whitewash'}
        key_3: {'A', 'B', 'C',...,'H', 'structure', 'HPS fixtures', 'LED fixtures', 'HPS cable', 'LED cable', 'distribution system'}
     """
    def initial_investment_costs():
        """ investment costs
             out: dict of dict,
             unit: rmb per m2 or rom per unit"""
        structure = {'A': 156.3, # multi-span,1 vent /10m2, ¥/m2
                     'B': 143.3, # multi-span,1 vent /20m2, ¥/m2
                     'C': 131.0, # multi-span,1 vent /30m2, ¥/m2
                     'D': 241.7, # venlo,1 vent /10m2, ¥/m2
                     'E': 218.3, # venlo,1 vent /20m2, ¥/m2
                     'F': 208.3} # venlo,1 vent /30m2, ¥/m2

        cover = {'A': 7.8,  # PE, ¥/m2
                 'B': 15.7, # double PE, ¥/m2
                 'C': 55.0} # glass, ¥/m2

        cooling = {'A': 0, # no cooling
                   'B': 25.5, # fogging 200, ¥/m2
                   'C': 29.1, # fogging 300, ¥/m2
                   'D': 46.5, # fogging 400, ¥/m2
                   'E': 22.2, # pad&fan 60, ¥/m2
                   'F': 27.5, # pad&fan 90, ¥/m2
                   'G': 31.0} # pad&fan 120, ¥/m2

        heating = {'A': 412920/10000, # boiler, 1.16 MW, ¥/unit, for 1 ha
                   'B': 432000/10000, # boiler, 1.74 MW, ¥/unit, for 1 ha
                   'C': 475200/10000} # boiler, 2.32 MW, ¥/unit, for 1 ha
                  

        thermal_screen = {'A': 0, # no thermal screen
                          'B': 12, # ¥/m2, Luxous 1347 FR
                          'C': 18, # ¥/m2, Obscura 9950 FR
                          'D': 27.5, # ¥/m2, Obscura 10070 WB+BW
                          'E': 32.2, # ¥/m2, RBO100AB+B
                          'structure': 42} # ¥/m2

        shading_screen = {'A': 0, # no shading screen
                          'B': 13.5, # ¥/m2, Harmony 2947 FR
                          'C': 11, # ¥/m2, Harmony 3315 O FR
                          'D': 12, # ¥/m2, Harmony 4515 O FR
                          'structure': 42} # ¥/m2

        light = {'A': 0, # No lamps
                 'B': 5.6180, # HPS 50, lifetime 10,000 hr
                 'C': 11.2360, # HPS 100, lifetime 10,000 hr
                 'D': 16.8539, # HPS 150, lifetime 10,000 hr
                 'E': 22.4719, # HPS 200, lifetime 10,000 hr
                 'F': 67.7419, # LED 50, lifetime 35,000 hr
                 'G': 135.4839, # LED 100, lifetime 35,000 hr
                 'H': 203.2258, # LED 150, lifetime 35,000 hr
                 'I': 270.9677, # LED 200, lifetime 35,000 hr
                 'HPS fixtures': {'B':25.2809, 'C':50.5618, 'D':75.8427, 'E':101.1236},
                 'cable': {'A':0, 'B':25.2809, 'C':50.5618, 'D':75.8427, 'E':101.1236,\
                           'F':14.5161, 'G':29.0323, 'H':43.5484, 'I':58.0645}
                }

        CO2 = {'A': 0, # No CO2 enrichment
               'B': 3.7, # CO2 50 kg/ha/hr, distribution system: 3.7 ¥/m2
               'C': 3.7, # CO2 100 kg/ha/hr, distribution system: 3.7 ¥/m2
               'D': 3.7, # CO2 150 kg/ha/hr, distribution system: 3.7 ¥/m2
               'E': 3.7} # CO2 200 kg/ha/hr, distribution system: 3.7 ¥/m2
               

        whitewash = {'A': 0, # no whitewash
                     'B': 1} # whitewash factor 0.5

        initial_investment_costs = {'structure' : structure,
                                    'cover': cover,
                                    'cooling': cooling,
                                    'heating': heating, 
                                    'thermal_screen': thermal_screen,
                                    'shading_screen': shading_screen,
                                    'light': light,
                                    'CO2': CO2,
                                    'whitewash': whitewash}

        return initial_investment_costs

    # ================================================================

    def lifetime():
        """ out: dict of dict,
             unit: year or hour"""
        structure = {'A': 15, # multi-span, 1 vent /10m2, ¥/m2
                     'B': 15, # multi-span, 1 vent /20m2, ¥/m2
                     'C': 15, # multi-span, 1 vent /30m2, ¥/m2
                     'D': 15, # venlo, 1 vent /10m2, ¥/m2
                     'E': 15, # venlo, 1 vent /20m2, ¥/m2
                     'F': 15} # venlo, 1 vent /30m2, ¥/m2

        cover = {'A': 7, # PE
                 'B': 7, # double PE
                 'C': 15} # glass

        cooling = {'A': 1, # no cooling, no investment costs
                   'B': 10, # fogging 200
                   'C': 10, # fogging 300
                   'D': 10, # fogging 400
                   'E': 10, # pad&fan 60
                   'F': 10, # pad&fan 90
                   'G': 10} # pad&fan 120

        heating = {'A': 15, # boiler 
                   'B': 15, # boiler
                   'C': 15} # boiler

        thermal_screen = {'A': 1, # no thermal screen, no investment costs
                          'B': 5, # Harmony 2947 FR
                          'C': 5, # Obscura 9950 FR
                          'D': 5, # Obscura 10070 WB+BW
                          'E': 5, # RBO100AB+B
                          'structure': 10}

        shading_screen = {'A': 1, # no shading screen, no investment costs
                          'B': 5, # Harmony 2947 FR
                          'C': 5, # Harmony 3315 O FR
                          'D': 5, # Harmony 4515 O FR
                          'structure': 10}  

        light = {'A': 10000, # # pesudo value, No lamps
                 'B': 10000, # HPS 50, lifetime 10,000 hr
                 'C': 10000, # HPS 100, lifetime 10,000 hr
                 'D': 10000, # HPS 150, lifetime 10,000 hr
                 'E': 35000, # HPS 200, lifetime 10,000 hr
                 'F': 35000, # LED 50, lifetime 35,000 hr
                 'G': 35000, # LED 100, lifetime 35,000 hr
                 'H': 35000, # LED 150, lifetime 35,000 hr
                 'I': 35000, # LED 200, lifetime 35,000 hr
                 'HPS fixtures': 7, # years
                 'cable': 10} # years
                 

        CO2 = {'A': 1, # pseudo value, No CO2 enrichment system 
               'B': 10, # CO2 50 kg/ha/hr, distribution system: 3.7 ¥/m2
               'C': 10, # CO2 100 kg/ha/hr, distribution system: 3.7 ¥/m2
               'D': 10, # CO2 150 kg/ha/hr, distribution system: 3.7 ¥/m2
               'E': 10} # CO2 200 kg/ha/hr, distribution system: 3.7 ¥/m2

        whitewash = {'A': 1, # pesudo value, no whitewash
                     'B': 1} # whitewash factor 0.5, lifetime 1 year

        lifetime = {'structure' : structure,
                    'cover': cover,
                    'cooling': cooling,
                    'heating': heating, 
                    'thermal_screen': thermal_screen,
                    'shading_screen': shading_screen,
                    'light': light,
                    'CO2': CO2,
                    'whitewash': whitewash}

        return lifetime

    # ================================================================

    def maintenance():
        """out: dict of dict,
           unit: % of investment costs"""
        structure = {'A': 0.02, # multi-span
                     'B': 0.02, # multi-span
                     'C': 0.02, # multi-span
                     'D': 0.005, # venlo
                     'E': 0.005, # venlo
                     'F': 0.005} # venlo

        cover = {'A': 0.05, # PE
                 'B': 0.05, # double PE
                 'C':0.005} # glass

        cooling = {'A': 0,
                   'B': 0.05, # fogging 200
                   'C': 0.05, # fogging 300
                   'D': 0.05, # fogging 400
                   'E': 0.05, # pad&fan 60
                   'F': 0.05, # pad&fan 90
                   'G': 0.05} # pad&fan 120

        heating = {'A': 0.01, # boiler 
                   'B': 0.01, # boiler
                   'C': 0.01} # boiler

        thermal_screen = {'A': 0,
                          'B': 0.05,
                          'C': 0.05,
                          'D': 0.05,
                          'E': 0.05,
                          'structure': 0.05}

        shading_screen = {'A': 0,
                          'B': 0.05,
                          'C': 0.05,
                          'D': 0.05,
                          'structure': 0.05}  

        light = {'A': 0, # no lamps
                 'B': 0.01, # HPS 50
                 'C': 0.01, # HPS 100
                 'D': 0.01, # HPS 150
                 'E': 0.01, # HPS 200
                 'F': 0.005, # LED 50
                 'G': 0.005, # LED 100
                 'H': 0.005, # LED 150
                 'I': 0.005, # LED 200
                 'HPS fixtures': 0.01,
                 'cable': 0.01}

        CO2 = {'A': 0, # pseudo value, No CO2 enrichment system 
               'B': 0.05, # CO2 50 kg/ha/hr, distribution system 5% maintenance
               'C': 0.05, # CO2 100 kg/ha/hr, distribution system 5% maintenance
               'D': 0.05, # CO2 150 kg/ha/hr, distribution system 5% maintenance
               'E': 0.05} # CO2 200 kg/ha/hr, distribution system 5% maintenance

        whitewash = {'A': 0, # pesudo value, no whitewash
                     'B': 0} # whitewash factor 0.5

        maintanence = {'structure' : structure,
                       'cover': cover,
                       'cooling': cooling,
                       'heating': heating, 
                       'thermal_screen': thermal_screen,
                       'shading_screen': shading_screen,
                       'light': light,
                       'CO2': CO2,
                       'whitewash': whitewash}

        return maintanence
    
    initial_investment_costs = initial_investment_costs()
    lifetime = lifetime()
    maintenance = maintenance()
    design_element_parameters = {'cost': initial_investment_costs,
                                 'lifetime': lifetime,
                                 'maintenance': maintenance}
    return design_element_parameters
    


