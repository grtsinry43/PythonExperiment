"""
@author grtsinry43
@date 2024/12/17 17:26
@description
计算1000以内的所有水仙花数，主程序要求使用迭代器或生成器等机制打印输出结果。
"""


def narcissistic_numbers(limit: int):
    """
    生成器函数，生成limit以内的水仙花数
    :param limit: 范围上限，比如到1000，不包含1000
    :return: 生成器，生成水仙花数
    """
    for num in range(1, limit):
        digits = list(map(int, str(num)))
        power = len(digits)
        if sum(d ** power for d in digits) == num:
            yield num


# 主程序
if __name__ == "__main__":
    for number in narcissistic_numbers(1000):
        print(number)
