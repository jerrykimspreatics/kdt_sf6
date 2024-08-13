# readlines() - 데이터를 리스트로 반환

try:
    f = open("./source/season0.txt", 'r')

    seasons = f.readlines()  #데이터가 seaseons 리스트에 저장됨
    print(seasons)
    print(seasons[1])  #여름
    print(seasons[-1]) #겨울
    print(seasons[1:3]) #[여름, 가을]

    # 전체 출력
    for season in seasons:
        print(season.strip())

    f.close()
except FileNotFoundError as msg:
    # print("파일을 찾을 수 없습니다.")
    # 내부의 에러 메시지 보고 싶을때
    print(msg)

