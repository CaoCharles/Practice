# 建構Python類別

# class MyFirstClass:
#     pass
# 
# a = MyFirstClass()
# b = MyFirstClass()
# 
# print(a)
# print(b)

# 加入屬性

# class Point:
#     pass
# 
# p1 = Point()
# p2 = Point()
# 
# # <object>.<attribute> = <value> 點記號法(dot notation) 
# p1.x = 5
# p1.y = 4 
# 
# p2.x = 3
# p2.y = 6
# 
# print(p1.x, p1.y)
# print(p2.x, p2.y)

# 覆蓋
# class Point:
#     def reset(self):
#         self.x = 0
#         self.y = 0
# 
# p = Point()
# p.reset()
# print(p.x, p.y)

# import math
# 
# class Point:
#     def move(self, x, y):
#         self.x = x
#         self.y = y
#     
#     def reset(self):
#         self.move(0, 0)
#     
#     def calculate_distance(self, other_point):
#         return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
# 
# # 如何使用
# point1 = Point()
# point2 = Point()
# 
# point1.reset()
# point2.move(5, 0)
# print(point2.calculate_distance(point1))
# assert (point2.calculate_distance(point1) == point1.calculate_distance(point2))
# point1.move(3, 4)
# print(point1.calculate_distance(point2))
# print(point1.calculate_distance(point1))
# print(point1)

# # 初始化
# class Point:
#     def __init__(self, x, y):
#         self.move(x, y)
#     
#     def move(self, x, y):
#         self.x = x
#         self.y = y
#         
#     def reset(self):
#         self.move(0, 0)
# 
# # 建構一個Point
# point = Point(3, 5)
# print(point.x, point.y)

# import math
# 
# class Point:
#     '代表二維空間中的座標點'
#     
#     def __init__(self, x=0, y=0):
#         '''點位置初始化。可以指定x與y座標，若無指定，預設為原點'''
#         self.x = x
#         self.y = y
#     
#     def move(self, x, y):
#         "移動點到新的2D空間位置"
#         self.x = x
#         self.y = y
# 
#     def reset(self):
#         '將點重置回到原點:0, 0'
#         self.move(0, 0)
#     
#     def calculate_distance(self, other_point):
#         """計算這一點與當作參數傳入的第二點的距離。
#         
#                     此函數使用勾股定理來計算兩點的距離，距離以浮點數回傳。"""
#         return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
#     
# a = Point()
# print(a)
# a.move(3, 4)
# b = Point()
# print(a.calculate_distance(b))