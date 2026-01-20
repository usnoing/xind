class Student:
    def __init__(self,name,ID):
        self.name=name
        self.ID=ID
        self.chengjis={"语文":0,"数学":0,"英语":0}

    def print_cg(self):
        print(f"Chinese: {self.chengjis['语文']}, Math: {self.chengjis['数学']}, English: {self.chengjis['英语']}")
    
    def dengji(self,yu,shu,ying):
        self.chengjis["语文"]=yu
        self.chengjis["数学"]=shu
        self.chengjis["英语"]=ying

    def grade(self,cores,chengji):
        if cores in self.chengjis:
            self.chengjis[cores]=chengji

stu1=Student("张三","251718101")
stu1.dengji(85,90,88)
stu1.grade("数学",95)
stu1.print_cg()