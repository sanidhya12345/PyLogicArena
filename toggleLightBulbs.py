class Solution:
    def __init__(self,bulbs):
        self.bulbs=bulbs
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        d=dict()
        for i in bulbs:
            if i not in d:
                d[i]=True
            else:
                if d[i]==True:
                    d[i]=False
                else:
                    d[i]=True
        l=[i for i in d.keys() if d[i] is True]
        l.sort()
        return l

bulbs=[10,20,30,10]
print(Solution(bulbs).toggleLightBulbs(bulbs))