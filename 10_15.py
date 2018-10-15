# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 8:48
# @Author  : guobin
# @e-mail: trulymust@163.com
# @Software: PyCharm
#name = input("please input something");
#print('1024 * 768 =', 1024*768);
# print('\\\t\\');
# print('\n');
# print(r'\\\n\\');
# print('''a
# b
# c''')
# n = 123;
# f = 456.789;
# s1 = 'hello,world';
# s2 = 'hello,\'adam\''
# s3 = r'hello,"bart"';
# s4 = r'''hello,
# lisa!''';
# print(s4)
#print(ord('d'))
# print('中文'.encode('utf-8'))
# s1 = 72;
# s2 = 85;
# s3 = (s2-s1)/s1;
# #print('%.1f%%' %(s3))
# print('{0:.1f}%'.format(s3))


#list增删
# classmates = ['a','b','c'];
# print(len(classmates));
# print(classmates[len(classmates)-1]);
# print(classmates[-1]);
# classmates.append('d');
# print(classmates[-1]);
# print(classmates);
# classmates.insert(0,'f');
# print(classmates);
# print(classmates.pop());
# print(classmates);
# print(classmates.pop(0))
# print(classmates);
# classmates[1] = 'asd';
# print(classmates);

#list练习
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0]);
# print(L[1][1]);
# print(L[2][2]);

#判断练习
# height = 92;
# high = 1.75;
# bmi = height/(high*high);
# if bmi<18.5:
#     print(bmi);
#     print('过轻');
# elif bmi >= 18.5 and bmi<25:
#     print(bmi);
#     print('正常');
# elif bmi>=25 and bmi<28:
#     print(bmi);
#     print('过重')
# elif bmi>=28 and bmi<32:
#     print(bmi);
#     print('肥胖');
# else:
#     print(bmi);
#     print('严重肥胖');

# 循环练习
# names = ['q','w','e'];
# for name in names:
#     print(name);

# sum = 0;
# for x in list(range(101)):
#     sum+=x;
# print(sum);

# sum = 0;
# n = 99;
# while n>0:
#     sum +=n;
#     n -=2;
# print(sum);

# L = ['Bart', 'Lisa', 'Adam'];
# for t in L:
#     print('Hello', t);

# 字典
# d = {'Michael':95,'Bob':75,'Tracy':85};
# d['Michael'] = 80;
# print(d['Michael']);
# print('Bob' in d);
# print(d.get('Michae','没有找到该值'));

# 字典删除操作
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85};
# d.pop('Tracy');
# print(d);

# set
# s = set([1,2,3]);
# print(s);
# s.add(4);
# print(s);
# s.remove(4);
# print(s);
# s.remove(100);

# s1 = set([1,2,3]);
# s2 = set([2,3,4]);
# print(s1 & s2);
# print(s1 | s2);

# 函数练习
# n1 = 255;
# n2 = 1000;
# print(hex(n1));

# redis学习
import redis
r = redis.StrictRedis(host='127.0.0.1',port=6379,db=0,decode_responses=True);
# r.set('德莱文','打飞机');
print(r.get('德莱文'));
print('饭店门口');