#루프의 else 절

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # 루프에서 인수를 발견하지 못하고 떨어집니다
        print(n, 'is a prime number')


#range(2, 10) : 2,3,4,5,6,7,8,9
#n = 2
#n = 3
#n = 4
#...
#n = 9
#"n=2" 라면 range(2,2) 이므로 반복할 숫자가 없음. for문이 실행할 수 없음.
