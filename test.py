"""
a,b=0,1
print(b)
while b<100:
  a,b=b,a+b
  print(b)
  

c,d,e,f,g=5.5,4+5j,True,"test",100
print(type(a),type(b),type(c),type(d),type(e),type(f),type(g))
"""

"""
b=17//3
print(b)
"""
"""print("avv""ddda")

print("avv"*3+"123")



print("aasd\
      123")

print("aasd""..."







      
      "123")"""


"""tup=(1,2,3,[1,2,3])
print(tup)


list1=[1,1,1,1,1,1,1,1]
print(list1)"""


'''a={"123","wee","232131sadad"}
print(a)


b=set('123wee32131sadad')
print(b)

tel={}
tel1={'a':123,'b':233}
print(tel,tel1)
print(tel1['a'])
tel1['c']=23123123
print(tel1['c'])
del tel1['b']
# print(tel1[])
print(tel1.keys())
print(tel1['b'])'''

'''a,b=0,1

if(a and b):
  print('a,b都是真')
else:
  print('a,b里有假')'''


'''A=12**2
a=A+1
c=a/3
b=c*3
print(A,a,b,c)'''

'''word='123'
print('<'+word*5+'>')
print(word[2])'''

'''a=[1,2,3,4,5,6,7]

a.append(1000)

print(a)

tul=('test','test1')
dict={tul[0]:25,a[0]:30}
print(dict)'''

'''guess,number=-1,7

while guess!=number:
  guess=int(input("I guess the number is..."))

  if guess==number:
    print('你他妈真是天才！')
  elif guess<number:
    print('小了，你真蠢！')
  else:
    print('大了，你真蠢！')'''

'''for x in range(5,100,5):
  print(x)

list=['football','basketball','handball','tennis','netball']
for x in list:
  print(x)'''


    


'''for n in range(2,200):
  for x in range(2,n):
    if n%x==0:
      print(n,'不是质数！！！！')
      break
  else:
    print(n,'质数，没跑了')'''

import sys

list=[1,2,3,4,5,6]
it=iter(list)

'''while True:
  try:
    print(next(it),end=' ')
  except StopIteration:
    sys.exit()
for x in it:
  print(x)'''


import sys

'''def fibonacci(n):
  a,b,counter=0,1,0
  while counter<=n:
    yield a
    a,b=b,a+b
    counter+=1
f=fibonacci(10)

while True:
  try:
    print(next(f),end=' ')
  except StopIteration:
    sys.exit()'''

'''import sys

def test(a,b,c,*tul):
  print(a,b,c)
  n=0
  for x in tul:
    n=n+x
  return n


t=test(100,500,600)
# t=test(100,b=100)
# t=test(a=100,500,600)
t=test(c=100,a=500,b=600)
t=test(2,4,5,6,4,1)
N=t
print(N)'''

'''for x in range(1,11):
  print('{0:3d}''{1:4d}''{2:5d}'.format(x,x*x,x*x*x))

print('The Story is {1} and {0},{other} like!'.format('WW','LJ',other='God'))'''

'''f=open('/Users/WUWEI/Desktop/test.txt','r+',encoding='utf-8')
f.write('加一句看下！')
value=('the answer',42)
s=str(value)
f.write(s)
for line in f.readlines():
  print(line)'''


class TestClass:
  na=''
  __ag=0
  he=0
  '''def __init__(self,name,age,height):
    self.na,self.ag,self.he=name,age,height
  def introduce(self):
    print('MY name is {}, I am {} years olds, {}cm'.format(self.na,self.ag,self.he))

# i=TestClass(1,2,3)
# i.introduce()
i=TestClass()
print(i.na)
print(i.he)
print(i.__ag)'''


# import pymysql
# import im
'''db=pymysql.connect('localhost','admin','admin','TESTDB')
cursor=db.cursor()'''
'''cursor.execute('select version()')
data=cursor.fetchone()
print('database version:{}'.format(data))
sql ='select * from employee'
for i in range(2,6):
  sqldelete='delete from employee  where id={}'.format(i)
  #print(sqldelete)
  cursor.execute(sqldelete)
sqlinsert="insert into employee(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) values('Mac','Angel','20','M','2000')"
cursor.execute(sqlinsert)
cursor.execute(sql)
db.commit()
rs=cursor.fetchall()
print(rs)
im.printA()'''

'''sql='CREATE TABLE card (id int,name varchar(100),type int,num int)'
cursor.execute(sql)
db.commit()'''

# import xlrd

'''data = xlrd.open_workbook('/Users/WUWEI/Desktop/card.xlsx')
table = data.sheet_by_name('card')
# rs=table.row_values(0)
#  print(rs)

for i in  range(0,table.nrows):
  for n in range(0,table.ncols):
    print(table.cell(i,n).value,end=' ')
  sql='insert into card(name,type,num) values({},{},{})'.format(repr(table.cell(i,0).value),table.cell(i,1).value,table.cell(i,2).value)
  cursor.execute(sql)
  db.commit()
  # print('\n')'''

import random

'''list=[0 for i in range(54)]
for i in range(0,54):
  list[i]=i+1
print(list)
random.shuffle(list)
print(list)

listA=[0 for i in range(17)]
listB=[0 for i in range(17)]
listC=[0 for i in range(17)]

for n in range(0,17):
  sqlA='select name from card where num= {}'.format(list[n*3+0])
  sqlB='select name from card where num= {}'.format(list[n*3+1])
  sqlC='select name from card where num= {}'.format(list[n*3+2])
  cursor.execute(sqlA)
  rs=cursor.fetchone()
  listA[n]=rs[0]
  cursor.execute(sqlB)
  rs=cursor.fetchone()
  listB[n]=rs[0]
  cursor.execute(sqlC)
  rs=cursor.fetchone()
  listC[n]=rs[0]
  # listA[n]=list[n*3+0]
  # listB[n]=list[n*3+1]
  # listC[n]=list[n*3+2]

print(listA)
print(listB)
print(listC)

card=[0 for i in range(54)]
for n in range(0,54):
  # print(list[n],end=' ')
  sql='select name from card where num= {}'.format(list[n])
  # print(sql)
  cursor.execute(sql)
  rs=cursor.fetchone()
  card[n]=rs[0]
print(card)  '''

'''import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host='smtp.qq.com'
mail_user='952291779@qq.com'
mail_pass='tdcasxrixjavbbig'

sender="952291779@qq.com"
receivers=["952291779@qq.com"]

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("952291779@qq.com", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465) 
    # smtpObj.connect(mail_host, 465)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")'''
  
  
  
'''print('Content-type:text')
 
print('<html>')
 
print('<head>')
 
print('<title>I like python CGI</title>')
 
print('</head>')
 
print('<body>')
 
print('<h2>Hello Word! This is my first CGI program, 哈哈哈</h2>')
 
print('</body>')
 
print('</html>')'''

# -*- coding=utf-8 -*-

from bs4 import BeautifulSoup
import requests
import sys

'''if __name__=='__main__':
  target='http://www.sina.com/'
  req=requests.get(url=target)
  req.encoding='utf-8'
  html=req.text
  bf=BeautifulSoup(html)
  div=bf.find_all('div',class_='newslist')
  print(div[0])
  a_bf=BeautifulSoup(str(div[0]))
  a=a_bf.find_all('a')
  for each in a:
    print(each.string,each.get('href'))
else:
  print('fuck!')'''

target='https://news.sina.com.cn/c/2019-04-09/doc-ihvhiewr4441548.shtml'
req=requests.get(url=target)
req.encoding='utf-8'
html=req.text
bf=BeautifulSoup(html)
# 获取标题
title=bf.find_all('h1',class_='main-title')
for each in title:
  print("文章标题："+each.string)
content=bf.find_all('div',class_='article')
p_bf=BeautifulSoup(str(content[0]))
p=p_bf.find_all('p')
print("文章内容：\n")
for each in p:
  print(each)










