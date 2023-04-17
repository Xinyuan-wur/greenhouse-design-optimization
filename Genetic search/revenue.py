def revenue(location, yield_, tomato_prices):
    """In: location, str, ['Jinshan', 'Langfang', 'Weifang', 'Pingliang']
           yield_: dict, key: month, val: tomato yield of the month, kg/m2
           tomato_prices: dict, key: month, val: tomato price of the month, ¥/kg
       Out: revenue from selling tomato, ¥/m2
    """
    # assuming 5% loss rate 
    revenue = 0.95*sum(yield_[i]*tomato_prices[location][i] for i in yield_.keys())
    
    return revenue
