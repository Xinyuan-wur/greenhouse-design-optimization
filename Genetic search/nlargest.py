import heapq

def nlargest(n, population_score):
    """find the n largest designs in the dictionary
    In: dict, key:string, val: float, derived from population_eval()
    Out: dict, key:string, top n designs with the best scores"""

    top_designs = heapq.nlargest(n, population_score, key = population_score.get('operational_income'))
    return top_designs