

#กำหนดกราฟ
graph = {
'a':{'b':4, 'c':3, 'e':7},
'b':{'c':6, 'd':5},
'c':{'d':11, 'e':8},
'd':{'e':2, 'f':2, 'g':10},
'e':{'g':5},
'f':{'g':3},
'g':{'f':3}
}

def dijkstra(graph, start, goal):
    shortest_distance = {}#เก็บ น้ำหนักของแต่ละ node ที่เดินมา จะอัพเดตเมื่อเดินไปเจอทางที่สั้นกว่า(กำหนดให้เริ่มต้นที่ infinity)
    track_predecessor = {}#เก็บเส้นทางที่ทำให้เดินมาถึง node นี้(สั้นสุด)
    unseen_node = graph
    infinity = 99999999
    track_path = []

    #ทำให้ทุกจุดเป็น inf ยกเว้น node เริ่มต้น (node a)
    for node in unseen_node:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseen_node:
        min_distance_node = None
        '''หา node ที่สั้นสุด(ที่มองเห็น) มาเป็น min_distance_node'''
        for node in unseen_node:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node
        
        path_option = graph[min_distance_node].items()

        for child_node, weight in path_option:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node

        unseen_node.pop(min_distance_node)#node ที่เดินแล้วต้องลบออกเพราะ dijkstra backtracking ไม่ได้
    
    current_node = goal
    while current_node != start:
        try:
            '''
            เก็บคำตอบใน list โดยเริ่มจากจุดสุดท้ายไปจุดเริ่มต้น(ขวาไปซ้าย)
            เพราะ track_predecessor ที่เก็บเส้นทางที่สั้นที่สุดทำให้เดินมาถึง node นี้อยู่ทางซ้ายเสมอ
            '''
            track_path.insert(0,current_node)
            '''ทำให้ node ปัจจุบันเป็น node ถัดไป'''
            current_node = track_predecessor[current_node]
        except KeyError:
            print('เข้าถึง path ไม่ได้')
            break
  
    track_path.insert(0,start)

    if shortest_distance[goal] != infinity:
        print(f'shortest distance is {shortest_distance[goal]}')#ผลรวมเส้นทาง
        print("Optimal path is "+"-".join(track_path)) #path


#output a-b-d-f
dijkstra(graph, 'a', 'f')
#ref https://www.youtube.com/watch?v=Ub4-nG09PFw&list=PLr7KH5QXUale6a0EsWHPeTVvnIPL_oGO0&index=1&t=39s