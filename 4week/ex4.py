num = int(input("임의의 정수를 입력해주세요: "))


def sumfunc(num):
    total = 0  
    
    for i in range(1, num + 1):  
        total += i  
    return total  

if num > 0:
    result = sumfunc(num)
    print(f"결과는 {result} 입니다.") 
    
else:
    print("정수를 입력해주세요.")