class Difference():
    def __init__(self,a):
        self.__elements = a

    def computeDifference(self):
        minn = self.__elements[0]
        maxx  = self.__elements[0]

        for i in self.__elements:
            if minn > i:
                minn = i
            elif maxx < i:
                maxx = i
        self.maxDifference = maxx - minn




_ = input()
a = [int(x) for x in input().split(' ')]
obj = Difference(a)
obj.computeDifference()
print(obj.maxDifference)

#3
# 1 2 5
# op - 4
