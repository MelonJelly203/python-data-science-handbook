def sum_of_lists(N):
    total = 0
    for i in range(5):
        L = [j^(j>>i) for j in range(N)]
        total += sum(L)
        del L # L 참조 삭제
    return total

# 메모리에 대한 라인 단위의 설명을 보려면 %mprun 매직을 사용하면 됨
# %mprun 매직을 사용하기 위해서는 별도의 모듈에 정의된 함수에만 동작하기 때문에
# 먼저 %%file 매직을 이용해 sum_of_lists 함수를 포함하는 mprun_demo.py라는 모듈을 생성
# %%file이 무조건 첫번째 줄에 단독으로 있어야 함
