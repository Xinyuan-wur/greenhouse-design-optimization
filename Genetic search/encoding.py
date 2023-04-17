
def encoding():
    # encoding each option of design component
    structure = {'A':'multispan-vent10', 'B':'multispan-vent20', 'C':'multispan-vent30',
                'D':'venlo-vent10', 'E':'venlo-vent20', 'F':'venlo-vent30'}
    
    cover = {'A':'PE', 'B':'doublePE', 'C':'glass'}
    
    cooling = {'A':'no', 'B':'fogging200', 'C':'fogging300', 'D':'fogging400',
               'E':'padfan60', 'F':'padfan90', 'G':'padfan120'}
    
    heating = {'A':'boiler116', 'B':'boiler174', 'C':'boiler232'}
    
    thermal_screen = {'A':'noscr1', 'B':'Luxous1347', 'C':'Obscura9950', 'D':'Obscura10070', 'E':'RBO100AB+B'}
    
    shading_screen = {'A':'noscr2', 'B':'Harmony2947', 'C':'Harmony3315', 'D':'Harmony4515'}
    
    light = {'A':'nolight', 'B':'HPS_50', 'C':'HPS_100', 'D':'HPS_150', 'E':'HPS_200',
             'F': 'LED30_50', 'G':'LED30_100', 'H':'LED30_150', 'I':'LED30_200'}

    CO2 = {'A':'CO0', 'B':'CO50', 'C':'CO100', 'D':'CO150', 'E':'CO200'}
    
    whitewash = {'A':'whitewash0', 'B':'whitewash0.5'}
    
    # order of design componentt in the gene string 
    design_element = {1:structure, 2:cover, 3:cooling, 4:heating,\
                 5:thermal_screen, 6:shading_screen, 7:light, 8:CO2, 9:whitewash}
    
    
    return design_element


