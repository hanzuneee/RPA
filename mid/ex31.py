# if 조건문을 작성하여 리스트에서 가장 큰 값을 반환하는 함수를 정의하는 코드를 완성하시오

def max_list(a) :
    j = 0
    for i in a :
        if i > j :
            j = i
    return j