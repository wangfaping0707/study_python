# 字符串的find方法是一个基本的子字符串查找的操作(它将返回一个传入子字符串的偏移量，或者在没有找到的情况下返回-1)

S = 'spapapam'

print(S.find('pa'))
print(S.find('ap'))
print(S.find('pap'))
print(S.find('GGGG'))

print('-----------------------------------------------------------------')

# 字符串的replace方法会对全局进行搜索和替换
print(S.replace('p','H'))
print('验证S是否被改变:', S)

line = 'aaa,bbb,ccccc,dd'
print(line.split(','))

print('判断S是否是大写：',S.isupper())

print('-----------------------------------------------------------------')

print(S.upper())

print('判断S是否是大写：',S.upper().isupper())

print('判断字符串是否·只有由字母组成：', S.isalpha())
print('判断字符串是否由数字和字母组成：',S.isalnum())



help(S.replace)



str1 = 'A\nB\nC'
print('str的长度：',len(str1))

print(str1)
print('--------------------------------------------')

str2 = 'A\tB\tC'

print(str2)

print('\xc4')

print('spam'.encode('utf-8'))

print('spam'.encode('utf-16'))


















