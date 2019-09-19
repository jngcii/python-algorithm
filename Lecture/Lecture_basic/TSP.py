def next_permutation(a): # 다음 순열 찾는 함수

    # 맨 뒤부터 자기보다 자기 바로앞이 작은 놈을 찾는다.
    i = len(a) - 1
    if i > 0 and a[i] <= a[i-1]: i -= 1

    # 끝까지 갔는데도 자기보다 작은놈을 못찾았다. ======>  e.g) 987654321
    if i <= 0: False

    # 이제 i-1은  무조건 i 보다 크다.

    # i부터 마지막중에  i-1보단 큰것중에 제일 작은거 찾기
    # i-1 이후로는 내림차순(87654)으로 정렬되어있어서 맨뒤부터 보다가 i-1번째보다 큰거 나오면 그놈 저장
    j = len(a) - 1
    if a[i-1] > a[j]: j -= 1

    # 저장된 j 랑 i-1 번째 교체
    a[i-1], a[j] = a[j], a[i-1]

    # 교체래도 i부터 마지막까지는 내림차순 정렬되어있음
    # 오름차순으로 다시 정렬해버리기

    j = len(a) - 1
    for j > i:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    # 더이상 정렬된 놈을 못찾지 않고
    # 정렬을 완료했다.
    return True


n = int(input())    # 도시의 갯수 입력받음

d = list(range(n))  # 각 도시 0 ~ n-1로 이름 지어줌

w = [list(map(int, input().split())) for _ in range(n)] # 도시에서 도시로 가는 요금 입력받음

s = 0

res = 1000000000000


while True: # 파이썬에서 일단 반복 시작하는 방법은 일단 True로 해놓고 루프 안에서 if, break 로 탈출시키기
    ok = True

    # 현재 행렬의 가는길들을 모두 보면서 못가는 막힌길 있으면 ok=False로 하고 현재 루프 취소함 (마지막에서처음으로 가는 것부터)
    for k in range(-1, n-1):
        if w[d[k]][d[k+1]] == 0:
            ok = False
            break
        else:
            s += w[d[k]][d[k+1]]
    
    # 앞에서 돈 루프가 무사히 돌아서 s에 다 더했고 res 와 비교해서 작은걸 res에 넣는다.
    if ok: res = min(s, res)


    # d 다음 순열을 구한다. 없으면 마무리
    if not next_permutation(d): break

    # d첫번째가 0인것만 할거다. 1로 넘어가면 바로 마무리
    if d[0] != 0: break

print(res)
