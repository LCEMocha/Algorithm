class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = []
        common_i = []

        if len(list1) == len(list2):
            a, b = list1, list2
        else:
            a, b = max(list1, list2, key=len), min(list1, list2, key=len)

        for i in list(b):
            if i in a and i in b:
                common.append(i)
                common_i.append([list1.index(i) + list2.index(i), list1.index(i)])
            else:
                continue
        i = sorted(common_i)[0][1]

        result = []
        for i in sorted(common_i):
            if sorted(common_i)[0][0] == i[0]:
                a = i[1]
                result.append(list1[a])
        return result