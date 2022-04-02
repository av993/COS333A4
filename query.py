class Query:

    def __init__(self, is_overview, query=None, classid=None):
        self.is_overview = is_overview
        if query is None:
            self.dept = None
            self.num = None
            self.area = None
            self.title = None
        else:
            self.dept = query[0]
            self.num = query[1]
            self.area = query[2]
            self.title = query[3]
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
