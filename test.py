import classify as classify
import jieba
import csv

file_train_name = r'C:\Users\宝琦\\Documents\EXP_Data\Artificial Intelligence project\training_80w.txt'
file_test_name = r'C:\\Users\\宝琦\\Documents\\EXP_Data\\Artificial Intelligence project\\test_20w.txt'
file_stop_dict = r'C:\Users\宝琦\\Documents\EXP_Data\Artificial Intelligence project\stop_dict.txt'

global stop_list
stop_list=[]

def is_num(word):
    for i in range(len(word)):
        if word[i] <= '9' and word[i] >= '0':
           continue
        else:
            return False
    return True


def delete_item(sentence):
    result = ''
    for i in range(len(sentence)):
        # delete 'x' space
        if sentence[i] == 'x' or seq[2][i] == ' ' or sentence[i] == '' or sentence[i] == '' or sentence[i] == '':
            continue
        result += sentence[i]
    return result

# sentence is a list of word
# parameter --generator
def delete_stop_word(sentence):
    result = []
    #copy = []
    if len(stop_list) == 0:
        get_stop_list()
        #print(stop_list)
    for row in sentence:
       # copy.append(row)
        if row in stop_list or is_num(row):
            continue
        result.append(row)
    return  result

def get_stop_list():
    with open(file_stop_dict) as stop_file:
        while True:
            row = stop_file.readline()
            if row == '':
                break
            stop_list.append(row[0:-1])
        print('reading stop_word file finished!')
        return


jieba.initialize()
output = open('out.csv','w+',newline='')
writer = csv.writer(output)
with open(file_train_name,encoding='utf-8') as train_file:
    for i in range(5):#TODO change scale
        row = train_file.readline()
        seq = row.split("	",maxsplit=2)
        result = delete_item(seq[2])
        cut = jieba.cut(result)
        cons = delete_stop_word(cut)
        cons.insert(0,int(seq[1]))
        writer.writerow(cons)
output.close()
print('output to out.csv.....done')


