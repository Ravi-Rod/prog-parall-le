def calc_distance(point1, point2):
    """fonction qui retourne la distance entre 2 points""" 

#   assert len(point1) == len(point2), "Les points doivent avoir la même dimension"
    somme_carres = sum((x - y) ** 2 for x, y in zip(point1, point2))
    return somme_carres ** 0.5

def my_map(func, arg1, arg2):
    
    print("calling function "+ func.__name__ +" with arguments "+ str(arg1)+ " and "+ str(arg2))

    res= []

    for i,j in zip(arg1,arg2):
        res.append(func(i,j))

    return res

points1 = [(1.0,1.0,1.0), (2.0,2.0,2.0), (3.0,3.0,3.0)]
points2 = [(4.0,4.0,4.0), (5.0,5.0,5.0),( 6.0,6.0,6.0)]
#result = calc_distance(point_a, point_b)

distances= my_map(calc_distance, points1, points2)

print(distances)
#print(f"Distance euclidienne : {result:.6f}")