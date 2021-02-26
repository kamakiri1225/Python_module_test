import math

def get_trialgle(base, height):
    """
    三角形の面積を計算
    base: 底辺[m]
    height: 高さ[m] 
    """
    return base * height /2

def get_circle(radius):
    """
    円の面積を計算
    Area : 円の面積[m]
    radius: 半径[m]
    """
    Area = radius * radius *math.pi
    return Area


print('-'*10 + f'{__name__}' + '-'*10)
print(f'__name__ は{__name__}となっている。')