class Query:

    def __init__(self, is_overview, dept=None,
                 num=None, area=None,
                 title=None, classid=None):
        self.is_overview = is_overview
        self.dept = dept
        self.num = num
        self.area = area
        self.title = title
        self.classid = classid

    def __str__(self):
        output = str(self.is_overview) + " " + str(self.dept)
        output += " "+str(self.num)+" "+str(self.area)
        output += " "+str(self.title) + " "+str(self.classid)
        return output

    def get_dept(self):
        return self.dept

    def get_num(self):
        return self.num

    def get_area(self):
        return self.area

    def get_title(self):
        return self.title

    def get_classid(self):
        return self.classid
