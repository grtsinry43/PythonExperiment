"""
@author grtsinry43
@date 2024/12/31 09:34
@description 热爱可抵岁月漫长
"""

words = ["师父", "左子穆", "爹爹", "钟灵", "司空玄"]

# 使用正则表达式，从每个文件中筛选词的出现次数

import re
import io


# 读取文件
def read_file(file_path):
    with io.open(file_path, "r", encoding="utf-8") as f:
        return f.read()


# 从文件中筛选词的出现次数
def count_words(file_path, words):
    content = read_file(file_path)
    result = {}
    for word in words:
        result[word] = len(re.findall(word, content))
    return result


for i in range(1, 5):
    print(count_words("split_txt/天龙八部修订版第1章第{}部分.txt".format(i), words))
