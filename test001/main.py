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

if __name__ == '__main__':
    print(f'__name__ は{__name__}となっている。')
    print(f'三角形の面積は{get_trialgle(10, 2)}')
    print(f'円の面積は{get_circle(10)}')