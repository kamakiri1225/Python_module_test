import myget_math.get_math

if __name__ == '__main__':
    print('-'*10 + f'{__name__}' + '-'*10)
    print(f'__name__ は{__name__}となっている。')
    print(f'三角形の面積は{myget_math.get_math.get_trialgle(10, 2)}')
    print(f'円の面積は{myget_math.get_math.get_circle(10)}')