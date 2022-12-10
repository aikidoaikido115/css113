
Vertices = 7
Graph = [[0, 4, 3, 0, 7, 0, 0],
        [4, 0, 6, 5, 0, 0, 0],  
        [3, 6, 0, 11, 8, 0, 0],
        [0, 5, 11, 0, 2, 2, 10],
        [7, 0, 8, 2, 0, 0, 5],
        [0, 0, 0, 3, 0, 0, 3],
        [0, 0, 0, 10, 5, 3, 0]]

Selected = [0, 0, 0, 0, 0, 0, 0]

Edge = 0

Selected[0] = True

INFINITY = 9999999

print("Edge : Weight")


while (Edge < Vertices - 1):

   
    Minimum = INFINITY
   
    x = 0
    y = 0
    
    for i in range(Vertices):
        if Selected[i]:
            for j in range(Vertices):
                if ((not Selected[j]) and Graph[i][j]):  

                    if Minimum > Graph[i][j]:
                        Minimum = Graph[i][j]
                        x = i
                        y = j
    
    print(str(x) + "-" + str(y) + ":" + str(Graph[x][y]))
    
    Selected[y] = True
    Edge += 1      

# อ้างอิง : https://www.programiz.com/dsa/prim-algorithm