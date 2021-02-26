import math

def get_trialgle2times(base, height):
    """
    四角形の面積は三角形の面積の2倍
    base: 底辺[m]
    height: 高さ[m] 
    """
    triangle = base * height /2

    return 2 *triangle


print('-'*10 + f'{__name__}' + '-'*10)
print(f'__name__ は{__name__}となっている。')