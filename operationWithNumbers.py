while True:
	
	operation = input("Введите операцию: ")
	if operation == '+', '-', '*', '/':
		break
	else: print('Такой операции не существует. Попробуйте еще раз.')
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if operation == "+":
	print(a, "+", b, "=", a + b)
elif operation == "-":
	print(a, "-", b, "=", a - b)
elif operation == "*":
	print(a, "*", b, "=", a * b)
elif operation == "/":
	print(a, "/", b, "=", a / b)