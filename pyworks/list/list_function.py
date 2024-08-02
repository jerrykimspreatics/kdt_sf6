# 리스트 함수

# 추가 - 리스트.append(), 리스트.insert()
# 삭제 - 리스트.pop(), 리스트.remove()
# 정렬 - 리스트.sort(),  뒤집기 - reverse()

lower = ['b', 'd', 'a', 'c']
# 정렬(오름차순)
lower.sort()
print(lower)  #아스키 코드값이 작은 순서 부터 정렬
# 거꾸로
lower.reverse()
print(lower)



'''
# 'e' 추가
lower.append('e')  #맨 뒤 인덱스에 추가
print(lower)

# 'e'삭제
lower.pop()  # 맨 뒤 삭제
print(lower)

# 'b'와 'c' 사이에 'e' 추가
lower.insert(2, 'e')
print(lower)

# 'c' 삭제
lower.remove('c')
print(lower)
'''