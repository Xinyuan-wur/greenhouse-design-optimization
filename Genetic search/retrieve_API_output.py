import os.path 
import csv

def retrieve_API_output(string, location):
    """In: string, e.g. DCBABAABA
           location, str, ['Jinshan', 'Langfang', 'Weifang', 'Pingliang']
       Out: yield_: dict, key: month, val: tomato yield of the month, kg/m2
            gas_use: dict, key: month, val: gas use of the month,
            elec_use: float, electricity use of all months, 
            CO2_use: float, total CO2 supply of all months
    """
    # read yield and energy simulation for the given design 
    output_path = 'API outputs/{}/{}_{}.csv'.format(location, string, location)
#     if not os.path.exists(output_path): # If output not available, run simulation 如果API output不存在，进行simulation 
#         path, filename = gen_parameter(string, location)
#         run_design(path, filename)
    
    with open (output_path, newline="") as f:  
        reader = csv.DictReader(f)
        for i, line in enumerate(reader):
            yield_ = {i:float(line .get('month {} yield'.format(i),0)) for i in range(1,13)}
            gas_use = {i:float(line .get('month {} gasuse'.format(i),0)) for i in [1,2,3,4,10,11,12]}
            elec_use = float(line ['ElecUse'])
            CO2_use = float(line ['CO2 supply'])
    
    return yield_, gas_use, elec_use, CO2_use
