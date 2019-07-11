"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
print(sum(score.values())/len(score.values()))





# 2. 반 평균을 구하시오. -> 전체 평균
print('==== Q2 ====')
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print(list(scores.keys())[0], ": ", sum(scores['a'].values())/3, list(scores.keys())[1],': ', sum(scores['b'].values())/3)
print('total average: ', (sum(scores['a'].values())+sum(scores['b'].values()))/6)




# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
for key in city:
    print(f'{key}:', '%.2f'%(sum(city[key])/3))
# f strings 에서 {value:.2f} << 자리수 지정 가능


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
city_min = []
city_max = []
for i in city.values():
    city_min.append(min(i))
    city_max.append(max(i))
print('cold: ',list(city.keys())[city_min.index(min(city_min))])
print('hot: ',list(city.keys())[city_max.index(max(city_max))])

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')

# for i in city['서울']:
#     if 2 in i:
#         A = 'yes'
#         break
#     print(A)

if 2 in city['서울']:
    print('yes')
else: print('no')
