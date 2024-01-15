from itertools import zip_longest

class Upa():
    name = "Upa"
    def __init__(self):
        self.salary = 0
    
    def take_salary(self, int):
        self.salary += int

    def __str__(self):
        return self.__class__.__name__
    
    def do_work(self,list1,list2):
        return [self.work(l) for l in zip_longest(list1, list2, fillvalue=0)]

class Pupa(Upa):
    def work(self, l):
        return l[1] + l[0]
class Lupa(Upa):
    def work(self, l):
        return l[1] - l[0]

class Accountant():
    def give_salary(self, worker):
        worker.take_salary(int(input("Введите з/п " + str(worker) + " ")))

if __name__=="__main__":
    pupa, lupa = Pupa(), Lupa()
    acc = Accountant()
    acc.give_salary(pupa)
    acc.give_salary(lupa)
    print(pupa, pupa.salary, lupa, lupa.salary)
    list1 = [1,2,3,4,5,6]
    list2 = [5,6,7,8,9]
    print(pupa.do_work(list1, list2))
    print(lupa.do_work(list1, list2))