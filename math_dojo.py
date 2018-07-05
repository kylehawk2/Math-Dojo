class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result += k
            else:
                self.result += i
        return self
    def subtract(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result -= k
            else:
                self.result -= i
        return self
md = MathDojo().add(2).add(2,5).subtract(3,2).result
print md
md2 = MathDojo().add(0).add(1).add(3).add(4).add(3,5,7,8).add(2,4.3,1.25).subtract(2).add(2,3).subtract(1.1,2.3).result
print md2