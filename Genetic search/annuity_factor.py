def annuity_factor(r, n):
    """ In: r, float, discount factor
            n, int, lifetime of equipment
       Out: annuity_factor, float, for calculating equivalent annual cost"""
    numerator = 1-1/(1+r)**n
    annuity_factor = numerator/r
    
    return round(annuity_factor, 3)
