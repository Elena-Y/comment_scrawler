import glob
files = glob.glob('.\comments\*.txt')
# print(len(files))

for file in files:
    filename = file.split('_')[-1].strip('.txt')
    cat = file.split('_')[-2].strip('.\comments\\')
    # print(filename, cat)
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        if 'dushi' in file:
            with open('.\cat_comments\comments_dushi.txt', 'a', encoding='utf-8') as f1:
                f1.write(content)
        elif 'uanhuan' in file:
            with open('.\cat_comments\comments_xuanhuan.txt', 'a', encoding='utf-8') as f2:
                f2.write(content)
        elif 'youxi' in file:
            with open('.\cat_comments\comments_youxi.txt', 'a', encoding='utf-8') as f3:
                f3.write(content)
        elif 'lishi' in file:
            with open('.\cat_comments\comments_lishi.txt', 'a', encoding='utf-8') as f4:
                f4.write(content)
        elif 'qihuan' in file:
            with open('.\cat_comments\comments_qihuan.txt', 'a', encoding='utf-8') as f5:
                f5.write(content)