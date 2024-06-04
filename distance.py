from math import radians, cos, sin, asin, sqrt
def distance(latA,logA,latB,logB):
    # Convertir grados a radianes
    latA, logA, latB, logB = map(radians, [latA, logA, latB, logB])
    # Fórmula de Haversine
    dlat = latB - latA
    dlog = logB - logA
    a = sin(dlat/2)**2 + cos(latA)*cos(latB)*sin(dlog/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radio de la Tierra en km
    return c * r