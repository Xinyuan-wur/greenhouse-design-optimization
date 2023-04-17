def prices():
    """key: location, month, val: monthly mean prices 
    LNG: hostrical prices from 2017-2022 (¥/m3)
    Tomato prices: 2021 wholesale prices with 50% premium (¥/kg)
    elec_price: ¥/kWh
    CO2_price: ¥/kg"""
    
    tomato_price = {'Jinshan':{1:12, 2:11.18, 3:9.62, 4:11.03, 5:11.35, 6:11.63, 7:11.81, 8:12.84, 9:14.19, 10:15.09, 11:17.82, 12:18.71},
                 'Langfang':{1:15.23, 2:14.6, 3:16.91, 4:15.93, 5:14.43, 6:12.78, 7:11.58, 8:11.43, 9:11.79, 10:12.35, 11:17.18, 12:17.96},
                 'Weifang':{1:10.86, 2:12.99, 3:12.66, 4:11.12, 5:9.05, 6:6.75, 7:8.58, 8:9.12, 9:9.93, 10:11.6, 11:12.84, 12:13.68},
                 'Pingliang':{1:12.81, 2:12.23, 3:14.36, 4:13.46, 5:12.08, 6:10.56, 7:9.45, 8:9.32, 9:9.65, 10:10.16, 11:14.6, 12:15.32}
                   }
    
    gas_price = {'Jinshan':{1:4.93, 2:5.03, 3:4.56, 4:4.32, 10:4.37, 11:4.95, 12:5.11},
                 'Langfang':{1:4.76, 2:4.69, 3:4.44, 4:4.12, 10:4.36, 11:4.93, 12:4.84},
                 'Weifang':{1:4.89, 2:4.91, 3:4.75, 4:4.51, 10:4.45, 11:5.07, 12:5.23},
                 'Pingliang':{1:4.62, 2:4.24, 3:4.05, 4:3.87, 10:4.25, 11:5.02, 12:5.05}
                }
    
    elec_price = {'Jinshan':0.682, 'Langfang':0.512, 'Weifang':0.525, 'Pingliang':0.439}
    
    CO2_price = 1 # ¥/kg
    
    # rent+water+fertilizer+rockwool+seedlings+other material
    other_costs = {'Jinshan':28.06, 'Langfang':27.63, 'Weifang':27.58, 'Pingliang':27.5} # ¥/m2
    
    
    return tomato_price, gas_price, elec_price, CO2_price, other_costs
