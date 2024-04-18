def read_single_digit(digit):
    digits_korean = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    return digits_korean[digit]

def read_number(num): #세자리 10진 정수 한글반환(나머지이용)(if/elif else사용 실패-> 질문)
    hundred = num // 100
    ten = (num % 100) // 10
    one = (num % 100) % 10

    result = ''
    if hundred != 0:
        result += read_single_digit(hundred) + '백'
    if ten != 0:
        result += read_single_digit(ten) + '십'
    if one != 0:
        result += read_single_digit(one)
    return result

#주 프로그램부
num = int(input("세 자리 정수 입력: "))
result = read_number(num)
print(result)
