# get wordcloud
from wordcloud import WordCloud,ImageColorGenerator
from imageio.v2 import imread
import pickle as p
import glob

def get_wordcloud(d, cat):
    # 绘制词云
    font_path = './resources/simsun.ttf'  # 指定汉字字体位置，否则中文无法显示
    try:
        pic_path = pictures[i] # 指定词云背景图片
        pic = imread(pic_path)      # 读取背景图片
        pic_color = ImageColorGenerator(pic)
        wc = WordCloud(font_path=font_path, mask=pic, color_func=pic_color, background_color='white')
    # wc = WordCloud(font_path=font_path, background_color='white')

        wc.fit_words(d)
        wc.to_file(f'./data/wordcloud_{cat}.png')
    except:
        print(f'No picture for {cat}')
        wc = WordCloud(font_path=font_path, background_color='white')
        wc.fit_words(d)
        wc.to_file(f'./data/wordcloud_{cat}.png')

# # 单个文件测试
# file_path = './data/wordcloud_lishi.data'
# cat = file_path.split('/')[-1].split('.')[0]
# with open(file_path, 'rb') as file:
#     d = p.load(file)
#     get_wordcloud(d, 'dushi')

# 批量处理
files = glob.glob('./data/*.data')
print(len(files))
pictures = glob.glob('./resources/*.png')
i = 0

for file in files:
    with open(file, 'rb') as file:
        d = p.load(file)
        # print(file)
        cat = str(file).split('_')[-1].strip(".data>'")
        # print(cat)
        get_wordcloud(d, cat)
        i += 1
