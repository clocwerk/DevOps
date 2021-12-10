#2.i

print("Перша константа", False)
print("Друга константа", True)
print("Третя константа", None)


#2.ii
print(round(3,7))
print(bin(5))
print(all([1,2,3]))


#2.iii
words=["glek","abobus","shkila","impreze"]
for word in words:
    print(word)


for number in range(10):
    if number % 2 == 0:
        print(number)

print("  ")

a=4
while a<24:
    print(a)
    a=a+6

#2.iv


firstNum = 0
secondNum=10
try:
    print("Поділимо 10 на 0, у результаті отримаємо: ",secondNum/firstNum)
except ZeroDivisionError:
    print("Помилка")
finally:
    print("На нуль не ділиться")


#2.v


with open("README.md", "r") as reader:
    for x in reader:
        print(x)


#2.vi

x=lambda a,b : a/b
print(x(20, 10))