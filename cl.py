import numpy

Vect1= [0,1,2,3,4,5,6,7]
numpy.random.shuffle(Vect1)

def checker(V):
	for i in range(1, len(V) ):
		print(i)
		if V[i-1]>V[i]:
			print('O, Shut')

		
		
	

checker(Vect1)

print(1200000/0.8)
print(61*4)
print(255/4)
print(30*56)




'''
 def my_shiny_new_decorator(function_to_decorate):
...     # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
...     # получая возможность исполнять произвольный код до и после неё.
...     def the_wrapper_around_the_original_function():
...         print("Я - код, который отработает до вызова функции")
...         function_to_decorate() # Сама функция
...         print("А я - код, срабатывающий после")
...     # Вернём эту функцию
...     return the_wrapper_around_the_original_function
...
 # Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
def stand_alone_function():
...     print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")
...
 stand_alone_function()
Я простая одинокая функция, ты ведь не посмеешь меня изменять?
 # Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору,
 # который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую,
 # готовую к использованию функцию:
 stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
 stand_alone_function_decorated()
Я - код, который отработает до вызова функции
Я простая одинокая функция, ты ведь не посмеешь меня изменять?
А я - код, срабатывающий после
'''
