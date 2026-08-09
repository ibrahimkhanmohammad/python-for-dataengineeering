#   Create a dictionary mapping five countries to their capital cities. Iterate through this dictionary using the items() method and print each pair in the format: Country - Capital.
def cap_cntry(dct):
    for cntry, cap in dct.items():
        print(f'{cntry} - {cap}')

cntry_cap = {'India' : 'New Delhi', 'France' : 'Paris', 'Japan' : 'Tokyo', 'Brazil' : 'Brasilia', 'Australia' : 'Canberra'}
cap_cntry(cntry_cap)