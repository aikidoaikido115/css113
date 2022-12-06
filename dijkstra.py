

#กำหนดกราฟ
graph = {
'a':{'b':4, 'c':3, 'e':7},#
'b':{'c':6, 'd':5},#
'c':{'d':11, 'e':8},#
'd':{'e':2, 'f':2, 'g':10},
'e':{'g':5},
'f':{'g':3},
'g':{'f':3}
}

def dijkstra(graph, start, goal):
    shortest_distance = {}
    track_predecessor = {}
    unseen_node = graph #ตอนแรกจะเท่ากับกราฟแล้วจะค่อยๆหายไปจนเป็น {} เพราะ pop ออก
    infinity = 99999999
    track_path = []

    for node in unseen_node:
        shortest_distance[node] = infinity #ทำให้ทุก node เป็น inf
    shortest_distance[start] = 0 #เหลือเพียงแค่ node start ที่มีค่าเป็น 0

    while unseen_node: # {} มีค่าเป็น False ออก loop
        min_distance_node = None

        for node in unseen_node:
            if min_distance_node is None:
                min_distance_node = node # เป็น 'a'
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node #ถ้ามีน้อยกว่าให้สลับ ในตอนแรกๆจะเป็น inf เลยไม่น้อยกว่า **ต้นเหตุที่ unseen ค่อยๆหายคือบรรทัดนี้กับ pop
        
        #ใช้ graph เพราะจะใช้ข้อมูลในนั้น ไม่เอา unseen_node
        path_option = graph[min_distance_node].items() # dict ที่มี value เป็น dict อีกทีนึงเลยใช้ items() ได้

        for child_node, weight in path_option:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]: # น้อยกว่า inf อยู่แล้ว
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node] # เปลี่ยนจาก inf เป็น value ที่นับได้
                track_predecessor[child_node] = min_distance_node # ตอนแรกเท่ากับ 'a' แล้ว pop ออกจะเปลี่ยนเป็นตัวถัดไป
                # track_predecessor[child_node] คือ จุดเซฟ(เส้นที่มีค่าน้อยสุดของแต่ละ node)
        # print(unseen_node) # เช็คว่าอะไรหายไปในแต่ละ loop
        unseen_node.pop(min_distance_node)
    
    current_node = goal
    while current_node != start:
        try:
            track_path.insert(0,current_node) #เรียงจาก node f ไป a (คำตอบ)
            current_node = track_predecessor[current_node] #ก่อนจะเรียงครั้งถัดไปเปลี่ยนเป็นเส้นที่มีค่าน้อยสุด (มาจากจุดเซฟ)
        except KeyError:
            print('เข้าถึง path ไม่ได้')
            break

    track_path.insert(0,start)

    if shortest_distance[goal] != infinity:
        print(f'shortest distance is {shortest_distance[goal]}')
        print("-".join(track_path))


#output a-b-d-f
dijkstra(graph, 'a', 'f')