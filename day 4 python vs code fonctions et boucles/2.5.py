"""
(n) bottles of beer on the wall.
(n) bottles of beer.
If one of the bottles just happen to fall,
(n−1) bottles of beer on the wall.
"""

nbouteille = 100
print(str(nbouteille) + " bottles of beer on the wall.")
print(str(nbouteille) + " bottles of beer.")
print("If one of the bottles just happen to fall,")
nbouteille = nbouteille - 1
print(str(nbouteille) + " bottles of beer on the wall.")
while nbouteille > 2:
    print(str(nbouteille) + " bottles of beer on the wall.")
    print(str(nbouteille) + " bottles of beer.")
    print("If one of the bottles just happen to fall,")
    nbouteille = nbouteille - 1
    print(str(nbouteille) + " bottles of beer on the wall.")
while nbouteille > 0:
    print(str(nbouteille) + " bottle of beer on the wall.")
    print(str(nbouteille) + " bottle of beer.")
    print("If one of the bottle just happen to fall,")
    nbouteille = nbouteille - 1
    print(str(nbouteille) + " bottle of beer on the wall.")