
class Solution:        
    def permutations(iterable, r=None):
        # 입력된 데이터를 튜플 형태로 변환
        pool = tuple(iterable)
        n = len(pool)

        # r이 주어지지 않았다면, 입력 데이터의 전체 길이로 설정
        r = n if r is None else r
        if r > n:
            return

        # 초기 인덱스와 순환 횟수를 설정
        indices = list(range(n))
        cycles = list(range(n, n-r, -1))

        # 첫 번째 순열을 반환
        yield tuple(pool[i] for i in indices[:r])

        while n:
            # 순열의 각 위치에 대해
            for i in reversed(range(r)):
                # 순환 횟수를 감소
                cycles[i] -= 1

                # 만약 해당 위치의 순환 횟수가 0이면
                if cycles[i] == 0:
                    # 해당 원소를 맨 끝으로 이동
                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    # 순환 횟수 재설정
                    cycles[i] = n - i
                else:
                    # 해당 위치의 원소와 순환 횟수만큼 뒤에 있는 원소를 교환
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    # 교환 후 순열을 반환
                    yield tuple(pool[i] for i in indices[:r])
                    break
            else:
                # 모든 순열이 생성된 경우 종료
                return
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(nums)