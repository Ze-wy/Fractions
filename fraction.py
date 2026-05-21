import math

class fraction: #creating class

    def __init__(self,whole_part:int, numerator:int, denominator:int): #start
        self.numerator = numerator
        self.denominator = denominator
        self.whole_part = whole_part

    def simplify(self):
            gcd = math.gcd(self.numerator, self.denominator)
            self.numerator = self.numerator // gcd
            self.denominator = self.denominator // gcd
            if self.numerator > self.denominator:
                self.whole_part = self.whole_part + (self.numerator // self.denominator)
                self.numerator = self.numerator % self.denominator
                self.denominator = self.denominator
            return self

    def display(self, objFr2, objFrRes, symbol):
        if self.whole_part == 0 and objFr2.whole_part == 0:
            print(f' {self.numerator}     {objFr2.numerator}     {objFrRes.numerator}')
            print(f'--- {symbol} --- = ---')
            print(f' {self.denominator}     {objFr2.denominator}     {objFrRes.denominator}')

        elif self.whole_part != 0 and objFr2.whole_part != 0:
            print(f'  {self.numerator}      {objFr2.numerator}      {objFrRes.numerator}')
            print(f'{self.whole_part}--- {symbol} {objFr2.whole_part}--- = {objFrRes.whole_part}---')
            print(f'  {self.denominator}      {objFr2.denominator}      {objFrRes.denominator}')
        elif self.whole_part != 0 and objFr2.whole_part == 0:
            print(f'  {self.numerator}      {objFr2.numerator}      {objFrRes.numerator}')
            print(f'{self.whole_part}--- {symbol} {objFr2.whole_part}--- = {objFrRes.whole_part}---')
            print(f'  {self.denominator}      {objFr2.denominator}      {objFrRes.denominator}')
        elif self.whole_part == 0 and objFr2.whole_part != 0:
            print(f'  {self.numerator}      {objFr2.numerator}      {objFrRes.numerator}')
            print(f'{self.whole_part}--- {symbol} {objFr2.whole_part}--- = {objFrRes.whole_part}---')
            print(f'  {self.denominator}      {objFr2.denominator}      {objFrRes.denominator}')


    def summ(self,objFr2): #adding up the numerators
        symbol = '+'
        objFrRes = fraction(0,0,0) #creating var-collector

        if self.denominator == objFr2.denominator: #if den
            objFrRes.numerator = ((self.whole_part * self.denominator + self.numerator)
                                  +objFr2.whole_part * objFr2.denominator + objFr2.numerator)
            objFrRes.denominator = self.denominator
            objFrRes.whole_part = 0

        elif self.denominator != objFr2.denominator:
            objFrRes.whole_part = self.whole_part + objFr2.whole_part
            objFrRes.numerator = self.numerator * objFr2.denominator + objFr2.numerator * self.denominator
            objFrRes.denominator = self.denominator * objFr2.denominator

        objFrRes = objFrRes.simplify()

        self.display(objFr2,objFrRes,symbol)

    def diff(self,objFr2): #subtract the numerators
        symbol = '-'
        objFrRes = fraction(0, 0, 0)  # creating var-collector

        if self.denominator == objFr2.denominator:  # если знаменатели равны
            objFrRes.numerator = ((self.whole_part * self.denominator + self.numerator)
                                  - (objFr2.whole_part * objFr2.denominator + objFr2.numerator))
            objFrRes.denominator = self.denominator
            objFrRes.whole_part = 0

        elif self.denominator != objFr2.denominator:
            self_imp = self.whole_part * self.denominator + self.numerator
            obj2_imp = objFr2.whole_part * objFr2.denominator + objFr2.numerator

            common_den = self.denominator * objFr2.denominator
            res_num = self_imp * objFr2.denominator - obj2_imp * self.denominator

            objFrRes.numerator = res_num
            objFrRes.denominator = common_den
            objFrRes.whole_part = 0

        objFrRes = objFrRes.simplify()

        self.display(objFr2, objFrRes, symbol)

    def mult(self, objFr2):
        symbol = '*'
        objFrRes = fraction(0, 0, 0)

        self_imp = self.whole_part * self.denominator + self.numerator
        obj2_imp = objFr2.whole_part * objFr2.denominator + objFr2.numerator

        objFrRes.numerator = self_imp * obj2_imp
        objFrRes.denominator = self.denominator * objFr2.denominator

        objFrRes = objFrRes.simplify()


        self.display(objFr2, objFrRes, symbol)

    def priv(self,objFr2): #dividing the numerators and denominators

        symbol = '*'
        objFrRes = fraction(0, 0, 0)

        self_imp = self.whole_part * self.denominator + self.numerator
        obj2_imp = objFr2.whole_part * objFr2.denominator + objFr2.numerator

        obj2_new1 = objFr2.denominator
        obj2_new2 = obj2_imp

        objFrRes.numerator = self_imp * obj2_new1
        objFrRes.denominator = self.denominator * obj2_new2

        objFrRes = objFrRes.simplify()

        self.display(objFr2, objFrRes, symbol)



obj1 = fraction(1,1,2)
obj2 = fraction(1,2,2)
obj1.priv(obj2)

