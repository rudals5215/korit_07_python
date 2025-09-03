str_example = 'hello, python!'
print(str_example[0])
print(str_example[1])
print(str_example[2])
print(str_example[3])
print(str_example[4])
print(str_example[5])
print(str_example[6])
print(str_example[7])

for alphabet in str_example:        # enhanced-for 생각하시면 편합니다.
    print(alphabet, end=' ')

print(str_example[-1])
print(str_example[-2])
print(str_example[-3])
print(str_example[-4])
print(str_example[-5])
print(str_example[-6])
'''
마이너스 인덱스 : 문자열 뒤에서부터 부여하는 번호. 맨 마지막 데이터의 인덱스 넘버는 -1

문자열 슬라이싱(slicing) : 문자열 인덱스를 활용하여 한 문자 이상으로 구성된 단어나 문장을 추출할 때 사용하는 방법
    추출하고자 하는 단어나 문장의 시작 인덱스와 종료 인덱스를 통해 그 사이 문자들을 추출할 수 있ㅇ므.

형식 : 
a [ 시작 인덱스 : 종료 인덱스 : 증감값 ]
시작 인덱스 : 생략하면 처음부터 추출
종료 인덱스 : 생략하면 끝까지 추출
증감값 : 생략하면 1씩 증가함(인덱스 넘버가 0부터 1씩 증가한다는 뜻입니다.)
'''
print(str_example[:3:])     #0번지 부터 순서대로 3번 인덱스 미만까지만 출력한다는 의미 '-'도 사용 가능
'''
기본 예제
네 자리 숫자를 입력 받아 그 숫자의 맨 마지막 자리 숫자를 출력하시오

실행 예
네 자리 숫자를 입력하세요 >>> 02025
맨 마지막 숫자는 5 입니다.
맨 마지막 숫자는 5이며, 홀수입니다. -> 조건문 써야 합니다.
'''

number = input('숫자를 입력하세요 >>> ')
last_number = number[-1]
result = ''
if int(number) % 2 != 0 :
    result = '홀수'
else :
    result = '짝수'

print(f'맨 마지막 숫자는 {last_number}입니다.')
print(f'맨 마지막 숫자는 {last_number}이며, {result}입니다.')