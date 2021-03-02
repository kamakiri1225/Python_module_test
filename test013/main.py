import myget_math as mg

math_dic = {
    'small': [10, 100 ,1000],
    'medium' :  [100, 1000 , 10000],
    'big' : [1000, 10000, 10000]
} 
if __name__ == '__main__':
    
    for key, val in math_dic.items():
        print(f'======{key}==========')
        calc = mg.CalcMath(val[0], val[1], val[2]) #インスタンス化(初期状態)

        print(f'三角形の面積は{calc.get_trialgle()}')
        print(f'四角形の面積は{calc.get_trialgle2times()}')
        print(f'円の面積は{calc.get_circle()}')
