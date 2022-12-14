"""  Prim's Algorithm ดุดันไม่เกรงใจใคร """

""" โดยขั้นตอนหลักๆของ Prim's Algorithm มี 3 ขั้นตอน
    1. เลือกจุดยอดในกราฟอันไหนก็ได้อันหนึ่ง ให้กลายเป็นจุดเริ่มต้น (จุดราก)
    2. หาจุดยอดต่อไป โดยต้องเป็นจุดยอดที่เชื่อมต่อกับจุดเราเลือกอยู่ เลือกด้านที่มีน้ำหนักน้อยที่สุดและไม่เกิดวงจร
    3. ทำขั้นตอน 2 ซ้ำไปเรื่อยๆ จนกว่าจะได้ต้นไม้แผ่ทั่วที่มีน้ำหนักต่ำสุด  """

""" จำนวนจุดยอดทั้งหมดในกราฟที่เราจะใช้ """
Vertices = 7

""" สร้าง 2d array เพื่อให้เป็น adjacency matrix ในการแสดงถึงกราฟ """
                                             #           ไป a   b   c   d   e   f   g
Graph = [[0, 4, 3, 0, 7, 0, 0],              # จากจุด  a(0) [0 , 4 , 3 , 0 , 7 , 0 , 0 ]  
        [4, 0, 6, 5, 0, 0, 0],               #        b(1) [4 , 0 , 6 , 5 , 0 , 0 , 0 ]    
        [3, 6, 0, 11, 8, 0, 0],              #        c(2) [3 , 6 , 0 , 11, 8 , 0 , 0 ]
        [0, 5, 11, 0, 2, 2, 10],             #        d(3) [0 , 5 , 11, 0 , 2 , 2 , 10]
        [7, 0, 8, 2, 0, 0, 5],               #        e(4) [7 , 0 , 8 , 2 , 0 , 0 , 5 ]   
        [0, 0, 0, 3, 0, 0, 3],               #        f(5) [0 , 0 , 0 , 3 , 0 , 0 , 3 ]
        [0, 0, 0, 10, 5, 3, 0]]              #        g(6) [0 , 0 , 0 , 10, 5 , 3 , 0 ]    

"""  สร้าง array อีกอัน (Selected) เพื่อติดตามจุดยอดที่กำลังเลือกอยู่ """
"""  โดยจุดยอดที่กำลังเลือกอยู่จะมีค่าเป็นความจริงหรือไม่ก็เท็จ """
Selected = [0, 0, 0, 0, 0, 0, 0]

"""  ให้ เส้นเชื่อม (Edge) มีค่าเป็น 0 """
Edge = 0
"""  จำนวนของเส้นเชื่อมในต้นไม้แผ่ทั่วที่มีน้ำหนักต่ำสุดจะ น้อยกว่า (V - 1) เสมอ-   """
"""  -โดยที่ V คือจำนวนจุดยอดทั้งหมดในกราฟที่เราใช้ (ตัวแปร Vertices) """

""" เลือกจุดรากแล้วทำให้มันมีค่าเป็นจริง (เพราะเราเลือกจุดนี้เป็นจุดแรกในการหา) """
Selected[0] = True

""" ให้ อินฟินิตี้ (INFINITY) เป็นจำนวนเลขเต็มบวกที่มหาศาลเพื่อเอาไปใช้คำนวณใน algo """
INFINITY = 9999999

""" สร้าง list เพื่อน้ำหนักทั้งหมดมารวมกันในลิส และนำไปคำนวณหาผลรวมทั้งหมดของน้ำหนัก"""
Total_list = []

# print Edge : weight ให้แสดงถึงว่า จากจุดนี้ไปจุดนั้น ใช้น้ำหนักเท่าไหร่
print("Edge : Weight")

""" เข้า Algorithm """
""" โดย ลูป while จะหยุดทำงานเมื่อได้ต้นไม้แล้ว """
while (Edge < Vertices - 1):
    """ ในทุกๆจุดในกราฟ จะหาจุดทั้งหมดที่เชื่อมกัน"""
    """ คำนวณน้ำหนักของระยะจากจุดที่เลือกไปอีกจุด โดยให้น้ำหนักต้ำสุดจากทุกเส้นที่เชื่อมกับจุดที่เราเลือก"""
    """ แต่ถ้าจุดนั้นอยู่ในเซตที่เราเลือกว่ามันต่ำสุดแล้ว จะทิ้งหรือข้ามผลลัพธ์ไป"""
    """ เลอกจุดยอดจุดอื่นที่ใกล้กับจุดที่เราเลือก """
   
    """ ให้ตัวแปร minimum ตั้งต้นมีค่าเต็มบวกมหาศาล """
    Minimum = INFINITY
   
    """ ให้ x และ y มีค่าตั้งต้นเป็น 0 """
    x = 0
    y = 0
    
    for i in range(Vertices): # for จะหยุดทำงาน โดยขึ้นอยู่กับจำนวนจุดยอดทั้งหมดในกราฟ (Vertices)
        if Selected[i]:
            for j in range(Vertices):
                if ((not Selected[j]) and Graph[i][j]):  
                    """ จุดนี้ไม่ได้อยู่ใน array Selected และมีเส้นเชื่อมอยู่ """
                    if Minimum > Graph[i][j]:
                        Minimum = Graph[i][j]
                        x = i
                        y = j
    
    """  print ให้แสดงว่า จากจุดนี้ไปจุดนั้นใช้น้ำหนักเท่าไหร่ """
    print(str(x) + "-" + str(y) + ":" + str(Graph[x][y]))
    
    """  ให้ Selected เป็นค่า True """
    Selected[y] = True
    
    """  เพื่อเสร็จ 1 จุดแล้วจะ +1 ให้กับตัวแปร Edge (เส้นเชื่อม) """ 
    Edge += 1
    Total_list.append(int(Graph[x][y]))
    
    """  เพื่อจะให้ลูป while จบที่เส้นเชื่อมอันสุดท้าย """
    """  จะได้ต้นไม้แผ่ทั่วที่มีน้ำหนักต่ำสุด จึงจะเสร็จสิ้นตัว algorithm """

""" แสดงผลรวมทั้งหมดของน้ำหนักในต้นไม้แผ่ทั่วที่มีน้ำหนักต่ำสุด """
Total = sum(Total_list)
print("Total weight :",Total)



# อ้างอิง : https://www.programiz.com/dsa/prim-algorithm      