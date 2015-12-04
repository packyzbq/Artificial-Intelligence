import csv

class Classification():
    option = 0 #which method of classification
    arg_list = []   # parameter
                    # for Bayes, [0]=num of class
    all_num=[]      # all num for each class in Bayes
    parameter = {}  # save hidden parameter（中间变量）
                    # for Bayes, 'PCn' = Cn类的先验概率
                    #            'cls_n' = 类数
    term_fre_dict = {}   #贝叶斯词典，记录词项，Cn类的词频(list,默认2类),Cn类的概率

    def __init__(self,option = 0,arg_list =[2]):
        self.option = option
        self.arg_list = arg_list
        if option == 0:
            self.parameter.setdefault('cls_n',self.arg_list[0])


    #分类统计总数，计算词频以及概率
    #字典数据结构
    #用处理后的csv文件
    def build_dict(self, filename):
        init_num = 0
        temp_list_l = self.parameter['cls_n'] * 2
        temp_list = [init_num]*temp_list_l

        for i in range(len(temp_list)):
            temp_list[i] = 0
        with open(filename,newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                cls=int(row[0])      #存储每一篇文章的类别
                for i in range(1,len(row)):
                    if row[i] in self.term_fre_dict:
                        self.term_fre_dict[row[i]][cls] += 1
                    else:
                        temp_list[cls] += 1
                        self.term_fre_dict.setdefault(row,temp_list) #TODO unhashable list
                temp_list[cls] = 0
        return
    #计算词项概率
    def prob_comput(self):
        return

    #对某一对象进行分类，返回类型名
    def classify(self):
        return


    # 用于最小风险贝叶斯
    def risk_comput(self):
        return

    def print_dict(self):
        dict_list = list(self.term_fre_dict)
        print(dict_list)

cla = Classification()
cla.build_dict('out.csv')
cla.print_dict()