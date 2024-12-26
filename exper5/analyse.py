import io
import json
from snownlp import SnowNLP
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# 读取数据(json)
with io.open('result.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 准备数据
comments = [movie['comment'] for movie in data if movie['comment']]
labels = [1 if SnowNLP(comment).sentiments > 0.5 else 0 for comment in comments]

# 将数据分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(comments, labels, test_size=0.2, random_state=42)

# 创建用于文本处理和分类的管道
text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB()),
])

# 训练分类器
text_clf.fit(X_train, y_train)

# 预测情感
y_pred = text_clf.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f'准确率: {accuracy}')

# 将情感得分添加到原始数据中
for movie in data:
    if movie['comment']:
        sentiment_score = text_clf.predict_proba([movie['comment']])[0][1]
        movie['sentiment'] = sentiment_score
    else:
        movie['sentiment'] = None

with io.open('result_with_sentiment.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, ensure_ascii=False, indent=4))

# 统计分析
movies = [
    {"name": movie['name'], "types": movie['types'], "actors": movie['actors']}
    for movie in data
]

# 转换为DataFrame
df = pd.DataFrame(movies)

# 统计类型
type_counts = df.explode('types')['types'].value_counts()
print(type_counts)

# 统计演员
actor_counts = df.explode('actors')['actors'].value_counts()
print(actor_counts)

# 绘制相关图形
# 设置中文字体
font_path = './NotoSansCJK-Regular.ttc'
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()
# 绘制类型分布图
type_counts.plot(kind='bar', title='电影类型分布')
plt.show()

# 绘制演员分布图（只显示前15名，太多了我嘞个天）
top_actors = actor_counts.head(15)
top_actors.plot(kind='bar', title='电影演员分布（前15名）')
plt.show()