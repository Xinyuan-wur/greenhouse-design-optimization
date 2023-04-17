from encoding import encoding
import os.path
from generate_designs import generate_designs

def gen_parameter(string, location):
    """generate parameters.json for the string-encoded design
       generate path and filename
       In: 'ABDCACGDAA'
       Out_1:'glass/vent30/fogging & padfan/single screen/LED/'
       Out_2:''Jinshan_G_vent30_pad120_fog300_Harmony3315_LED30_100_bo160_ww0_CO0'
       Embeded function: generate_designs()
       """
    design_index = {1:'structure', 2:'cover', 3:'cooling', 4:'heating', 5:'thermal_screen', 6:'shading_screen', 7:'light', 8:'CO2', 9:'whitewash'}
    encode = encoding() # dict of dict, key1 = index integer, key2 = letter, val = string
    structure = encode[1][string[0]]
    cover = encode[2][string[1]]
    cooling = encode[3][string[2]]
    heating = encode[4][string[3]]
    thermal_screen = encode[5][string[4]]
    shading_screen = encode[6][string[5]]
    light = encode[7][string[6]]
    CO2 = encode[8][string[7]]
    whitewash = encode[9][string[8]]
    
    # get path & filename
    filename = '{}_{}'.format(string, location)
    path = "json parameters/{}/{}.json".format(location, filename)
    # only generate parameters.json when the file does not exists
    if not os.path.exists(path):
        # generate json parameters for the given design string
        parameters = generate_designs(location, filename, path, structure, cover, cooling, heating,\
                                      thermal_screen, shading_screen, light, CO2, whitewash)
    return path, filename