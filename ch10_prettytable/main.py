'''
외부 패키지의 설치 # 1 : settings를 통한 방법
project : 프로젝트명 으로 되어있는 부분 클릭
-> python interpreter 클릭
-> 패키지 검색 및 설치

외부 패키지의 설치 # 2 : 터미널을 이용하는 방법
pip install prettytable
'''
from prettytable import PrettyTable
from pokemon_data import pokemon_data

# PrettyTable의 객체 생성
table = PrettyTable()

table.field_names = ['이름','나이','주소']
print(table)

pokemon_table = PrettyTable()
pokemon_table.field_names =['번호','이름','타입']
# # 1
for pokemon in range(len(pokemon_data)):
    pokemon_table.add_row(pokemon_data[pokemon])
print(pokemon_table)

# # 2
for pokemon in pokemon_data:
    pokemon_table.add_row(pokemon)
    print(pokemon)

# # 3
pokemon_table.add_rows(pokemon_data)
print(pokemon_table)

# ch11_exception / main