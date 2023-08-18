# [문제]
# 문자열 배열 intStrs와 정수 k, s, l가 주어집니다. intStrs의 원소는 숫자로 이루어져 있습니다.

# 배열 intStrs의 각 원소마다 s번 인덱스에서 시작하는 길이 l짜리 부분 문자열을 잘라내 정수로 변환합니다. 
# 이때 변환한 정수값이 k보다 큰 값들을 담은 배열을 return 하는 solution 함수를 완성해 주세요

# [입출력 예]
# |                   intStrs                        |   k   |  s  |  l  |      result      |
# |--------------------------------------------------|-------|-----|-----|------------------|
# |    ["0123456789","9876543210","9999999999999"]   | 50000 |  5  |  5  |  [56789, 99999]  |

def solution(intStrs, k, s, l):
    answer = []

    # inStrs 리스트 순회 num[s:s+l] 범위의 숫자 추출
    # 추출한 수가 k보다 클 경우 answer에 그 수를 추가
    for num in intStrs:
        if int(num[s: s + l]) > k:
            answer.append(int(num[s: s + l]))
        
    return answer