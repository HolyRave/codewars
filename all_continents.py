# https://www.codewars.com/kata/58291fea7ff3f640980000f9
def all_continents(lst): 
    afr, usa, asia, europe, ocean = False,False,False,False,False
    for dcts in lst:
        if dcts['continent'] == 'Africa':
            afr = True
        elif dcts['continent'] == 'Americas':
            usa = True
        elif dcts['continent'] == 'Asia':
            asia = True
        elif dcts['continent'] == 'Europe':
            europe = True
        elif dcts['continent'] == 'Oceania':
            ocean = True
    return afr and usa and asia and europe and ocean
