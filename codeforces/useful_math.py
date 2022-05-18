"""
3+2+1 ===> 1+2+3
1+1+3+1+3 ===> 1+1+1+3+3
99+009+001 ===> 1+9+99
99+ --> 99
2 ===> 2
+2 ==> 2
++++++567467347++++++++++ ===> 567467347
"""


def rearrange(s: str):
    if len(s) == 1:
        return s
    if not s:
        return None
    nums = [int(c) for c in s.split('+') if c.isdigit()]
    nums.sort()
    res = ""
    for n in nums:
        res = res + str(n) + "+"

    return res[:-1]


if __name__ == "__main__":
    summ = input()
    result = rearrange(s=summ)
    print(result)
