# def hg():
#     x = 0
#     def hgg():
#          print(x)
#          x += 1
#          print(x)
#     hgg()
#     print(x)
# def hg():
#     x = []
#     def hgg():
#          print([])
#          x.append(1)
#          print(x)
#     hgg()
#     print(x)
# hg()

# def hgg():
#     x = 0
#     def hg():
#         print(x)
#         y = x + 1
#         print(y)
#     hg()
# hgg()

def hgg():
    x = [0, 0]
    def hg():
        print(x)
        x[0] = x[0] + 1
        print(x)
    hg()
hgg()
