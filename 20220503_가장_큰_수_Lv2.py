# Wrong Ans
import itertools
def solution1(numbers):
    numbers = list(map(str, numbers))
    idxs = list(itertools.permutations(numbers, len(numbers)))
    idx = list(map(lambda x:"".join(x), idxs))
    result = max(idx)
    return result

# Wrong Ans2
def solution1(numbers):
    if max(numbers) == 0:
        result = "0"
    else:
        numbers = list(map(str, numbers))
        ori_len = list(map(len, numbers))
        max_len = max(ori_len)

        numb = list(map(lambda x : int(x+(max_len-len(x))*x[0]), numbers))
        numb_dict = list(zip(numbers, numb))
        sorted_dict = sorted(numb_dict, key = lambda item: item[1], reverse = True)
        result = ''.join(list(map(lambda x : x[0], sorted_dict)))
    return result

# Top1 Ans
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))
