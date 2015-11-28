import jieba

filename = 'C:\\Users\\宝琦\\Documents\\EXP_Data\\Artificial Intelligence project\\sample.csv'
print(filename)
flag = True
try:
    with open(filename) as f:
        line = f.readline()
        line = f.readline()
except IOError:
    print('can not find the file')
    flag = False
if flag:
    i = line.find(',')
    seq = jieba.cut(line[i + 1:-1], cut_all=False)
    for item in seq:
        print(item,'  ')


