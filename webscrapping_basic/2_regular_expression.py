import re # 정규식 import

# ca?e
# care, cafe, case, cave ....add()

# 정규식을 컴파일
p = re.compile("ca.e") 
# . (ca.e) : 하나의 문자를 의미 > care, cage, case...
# ^ (^de) : 문자열의 시작 > desk, destination ...
# $ (se&) : 문자열의 끝 > case, base ... 

def print_match(m):
    if m:
        print("m.group() : ", m.group()) # 일치하는 문자열을 반환
        print("m.string() : ", m.string) # 입력받은 문자열을 반환
        print("m.start() : ", m.start()) # 일치하는 문자열의 시작 index
        print("m.end() : ", m.end())  # 일치하는 문자열의 끝 index
        print("m.span() : ", m.span())  # 일치하는 문자열의 시작과 끝 index
    else:
        print("Not matching")

#m = p.match("case") # 주어진 문자열의 처음부터 일치하는지 확인 so, careless인 경우 되는 것임
#print_match(m)
#print(m.group()) # 매치되지 않으면 에러가 발생

# m = p.search("careless") # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("careless cafe") # findall : 일치하는 모든것을 리스트 형태로 반환
# print(lst)

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 처음부터 일치하는지 확인
# 3. m = p.serach("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, cage, case...
# ^ (^de) : 문자열의 시작 > desk, destination ...
# $ (se&) : 문자열의 끝 > case, base ...

