import math

class CalcMath:
    def __init__(self, base, height, radius):
        self.base = base
        self.height = height
        self.radius = radius

    def get_trialgle(self):
        """
        三角形の面積を計算
        base: 底辺[m]
        height: 高さ[m] 
        """
        return self.base * self.height /2

    def get_trialgle2times(self):
        """
        四角形の面積は三角形の面積の2倍
        base: 底辺[m]
        height: 高さ[m] 
        """
        triangle = self.base * self.height /2

        return 2 *triangle        
    def get_circle(self):
        """
        円の面積を計算
        Area : 円の面積[m]
        radius: 半径[m]
        """
        Area = self.radius * self.radius *math.pi
        return Area

print('-'*10 + f'{__name__}' + '-'*10)
print(f'__name__ は{__name__}となっている。')