# extract keywords
# keywords = ale.extract_tags(content, topK=100, withWeight=True, allowPOS=('nr', 'ns', 'n', 'vn', 'v')) # TF-IDF
import jieba.analyse as ale
import pickle as p
import re
import glob

def get_keyword(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    keywords = ale.extract_tags(content, topK=100, withWeight=True, allowPOS=('nr', 'ns', 'n', 'vn', 'v')) # TF-IDF

    d = {}
    for k, w in keywords:
        print(k, w)
        d[k] = w
    with open(f'./data/keyword_{cat}.data', 'wb') as f:
        p.dump(d, f)

# # 单个文件测试
# file = './comments/dushi_变成血族是什么体验.txt'
# filename = file.split('_')[-1].strip('.txt')
# print(filename)
# get_keyword(file)


# 批量处理
files = glob.glob('./cat_comments/*.txt')
print(len(files))

for file in files:
    print(file)
    cat = file.split('_')[-1].strip('.txt')
    get_keyword(file)
