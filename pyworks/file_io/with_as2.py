# with open() as 구문
team = ['서울', '인천', '부산', '광주', '대전', '대구']
with open('source/city.txt', 'w') as f:
    for i in team:
        f.write(i + '\n')

with open('source/city.txt', 'r') as f:
    team = f.read()
    print(team)