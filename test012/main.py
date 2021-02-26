import myget_math

if __name__ == '__main__':
    calc = myget_math.get_math_multi.CalcMath(10, 100, 1000)

    print('-'*10 + f'{__name__}' + '-'*10)
    print(f'__name__ は{__name__}となっている。')
    print(f'三角形の面積は{calc.get_trialgle()}')
    print(f'四角形の面積は{calc.get_trialgle2times()}')
    print(f'円の面積は{calc.get_circle()}')
