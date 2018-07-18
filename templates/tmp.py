# from jinja2 import Environment, FileSystemLoader

# loader = FileSystemLoader('/')
# env = Environment(loader, trim_blocks=True, lstrip_blocks=True)
# template = env.get_template('html_template')
# import time
# import math
# print("1")
# #time.sleep(5)
# print("31")
# print(math.erf(4))
# print(8000*0.99)
# print(7404.00+320.00+1090.00+3536.50)

# print(330*2.87)
# print(2000/6)

def conditions(data):
	print('lendth=',len(data))
	print('isdigit',data.isdigit())
	print('islower',data.islower())
	print('isupper',data.isupper())
	print('isalpha',data.isalpha())


def checkio(data):
    	return True if  (not( len(data)<10 or  data.isdigit() or  data.islower() or  data.isupper() or  data.isalpha())) else False

	
if __name__ == '__main__':
	print(10138/3600)
    #These "asserts" using only for self-checking and not necessary for auto-testing
	conditions('ULFFunH8ni') 
	assert checkio('ULFFunH8ni') == True, "0st example"
	assert checkio('A1213pokl') == False, "1st example"
	assert checkio('bAse730onE4') == True, "2nd example"
	assert checkio('asasasasasasasaas') == False, "3rd example"
	assert checkio('QWERTYqwerty') == False, "4th example"
	assert checkio('123456123456') == False, "5th example"
	assert checkio('QwErTy911poqqqq') == True, "6th example"



# print("test")
# x="aaa1"
# print(x.isdigit())
# print(x.isalpha())
# print(x.islower())
# print(x.isupper())

# html_links = {'Main Page':'http://xgu.ru', 
# 			'Jinja':'http://xgu.ru/wiki/Jinja2'
# }

# data = {'title':'Site information',
# 		'header_1':'Popular pages',
# 		'links':html_links}

# with open("new.html", "w") as f:
#     f.write(template.render(data))
