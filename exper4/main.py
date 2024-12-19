"""
@author grtsinry43
@date 2024/12/19 08:13
@description 热爱可抵岁月漫长
"""
import jieba
import wordcloud
import pandas as pd


def count_paragraphs(file_path: str) -> int:
    """
    计算文件中的段落数量
    :param file_path: 文件路径
    :return: 段落数量
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return len(file.read().split("\n\n"))


def get_file_content(file_path: str) -> str:
    """
    读取文件内容
    :param file_path: 文件路径
    :return: 文件内容
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def spilt_in_parts(file_path: str, parts: int):
    """
    将文件划分为几个部分
    :param file_path: 文件路径
    :param parts: 划分的部分数
    :return: 得到的数组
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        length = len(content)
        part_length = length // parts
        return [content[i * part_length:(i + 1) * part_length] for i in range(parts)]


def save_file(content_str, title_str):
    """
    保存文件
    :param content_str: 文件内容
    :param title_str: 文件名
    :return: None
    """
    file_name = str(title_str) + '.txt'
    file = open(file_name, 'w')
    file.writelines(content_str)
    file.close()


count = count_paragraphs("天龙八部修订版第1章.txt")
print(count)
parts = spilt_in_parts("天龙八部修订版第1章.txt", 5)
for i in range(len(parts)):
    save_file(parts[i], "split_txt/天龙八部修订版第1章第" + str(i + 1) + "部分")

# 定义没有意义的语气词连接词作为停用词
stop_words = {'的', '是', '在', '了', '和', '与', '或', '等', '有', '就', '不', '也', '这', '那', '但', '还', '只',
              '或者', '不是', '不会', '不要', '不了', '不会', '不用', '不到', '不了', '不去', '不想', '不让', '不同',
              '不同于', '不同的', '不同意', "我", "你", "他", "她", "它", "我们", "你们", "他们", "她们", "它们",
              "这个", "那个", "这些", "那些", "这里", "那里", "这儿", "那儿", "这样", "那样", "这么", "那么",
              "说", "说道", "说着", "说出"}

# markdown语法符号作为停用词
stop_words.update(
    {'#', '##', '###', '####', '#####', '######', '*', '**', '***', '~~', '```', '```', '>', '---', '>>',
     '\n', '\t',
     ' ', '  ', '!', '[', ']', '(', ')', '{', '}', '<', '>', '/', '\\', '|', '&', '^', '%', '$', '@', '`',
     '~', '_',
     '-', ':', ';', '.', ',', '?', '!', '"', '\'', '=', '，', '。', '？', '！', '“', '”', '‘', '’', '；', '：',
     '、', '——'})


def cut_words(content: str) -> list:
    """
    对文本内容进行分词
    :param content: 文本内容
    :return: 分词结果
    """
    return [word for word in jieba.cut(content) if word not in stop_words]


print(cut_words(get_file_content("天龙八部修订版第1章.txt")))

# 分别生成词云
for i in range(5):
    wc = wordcloud.WordCloud(font_path="./NotoSansCJK-Regular.ttc", width=800, height=600, background_color="white")
    wc.generate(" ".join(cut_words(parts[i])))
    wc.to_file("wordcloud/天龙八部修订版第1章第" + str(i + 1) + "部分词云.png")
    # 将每个词云图中排名前五的热词内容和出现次数存储在不同Excel表格中，额用pandas吧
    words = wc.words_
    df = pd.DataFrame(words.items(), columns=["word", "frequency"])
    df.to_excel("word_excel/天龙八部修订版第1章第" + str(i + 1) + "部分热词.xlsx")
