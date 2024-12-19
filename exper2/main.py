"""
@author grtsinry43
@date 2024/12/17 17:31
@description
m(m>16并且为偶数)个海盗在一条船上，中途遇上风浪，食物短缺，需要扔 m/2名海盗下海。
于是海盗们排成一队，排队的位置即为他们的编号。报数，从 1 开始，数到 n(n分别为5或7)的海盗下海。
如此循环，直到船上仅剩 m/2名海盗为止。请编程求解上述问题，打印输出留在船上的海盗最初排序的序号。
"""


def remaining_pirates(m: int, n: int):
    """
    根据传入的海盗数量和报数规则，计算最终留在船上的海盗编号
    :param m: 海盗的数量
    :param n: 对应的n的值
    :return:
    """
    if m <= 16 or m % 2 != 0:
        raise ValueError("m的值必须大于16且为偶数")

    pirates = list(range(1, m + 1))
    index = 0

    while len(pirates) > m // 2:
        index = (index + n - 1) % len(pirates)
        pirates.pop(index)

    return pirates


if __name__ == "__main__":
    total = 18
    num = 5
    print(remaining_pirates(total, num))
