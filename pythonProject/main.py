a = range(1, 6)
tuples = []
for x in a:
    for y in a:
        if 2 * x - 2 * y in a:
            tuples.append((x, y))
print(tuples)

a = [1, 2, 3, 4, 5]
r = [(x, y) |  x<-a, y<-a, 2*x-2*y>0,2*x-2*y<6]
[(2,1),(3,1),(3,2),(4,2),(4,3),(5,3),(5,4)]