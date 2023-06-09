import mysql.connector as sql conn=sql.connect(host='localhost',user='root',passwd='root',charset='utf8 ')
c1=conn.cursor()
c1.execute('create database marriage_service_management') c1.execute('create table marriage_service_management.male_details(name varchar (200),address varchar(20),appearance varchar(100),age bigint(55),profession varchar (255),phone_no	bigint(200))') c1.execute('create table marriage_service_management.female_details(name varchar(100),address varchar(100),appearance varchar(25),age int(4),profession varchar(65),phone_no varchar(15))')
conn.commit()

if conn.is_connected(): c1=conn.cursor()

print('	WE
LCOME	TO	BTS	MATRIMONIAL	SERVICE
 	')
c='y'
while c.lower()=='y': print('=======================')
print("1.provide details") print('2. in search of bridegroom')
choice=int(input('enter the choice:')) if choice==1:
print('==========================')
print('5.Male customer details') print('6.Female customer details') choice=int(input('enter the choice:-'))
if choice==2:
print('========================')
print('3. Handsome Bride ') print('4. Beautiful Groom ')
choice=int(input('enter the choice-')) if choice == 5 :
a=(input('enter the name:')) b=(input('enter the address:')) d=(input('enter the appearance:')) e=(input('enter the age:')) f=(input('enter the profession:')) g=(input('enter the phone_no:')) c1=conn.cursor() sql_insert="insert into
marriage_service_management.male_details values( '{}','{}','{}','{}','{}','{}')".format(a,b,d,e,f,g)
c1.execute(sql_insert) conn.commit()
print ('Details are successfully inserted') c=input('do you want to continue (y/[n]:)') if c =='y' :
continue
 
else:

)
 

print('THANK	YOU	FOR	VISITING	OUR	WEBSITE' print('VISIT	AGAIN')
 
if choice==6:
h=(input('enter the name:')) i=(input('enter the adderss:')) k=(input('enter the appearance:')) l=(input('enter the age:')) m=(input('enter the profession:')) n=(input('enter the phone_no:')) c1=conn.cursor() sql_insert="insert into
marriage_service_management.female_details values( '{}','{}','{}','{}','{}','{}')".format(h,i,k,l,m,n)
c1.execute(sql_insert) conn.commit()
print("Details are successfully inserted") c=input('do you want to continue (y/[n]:)') if c =='y' :
continue
 
else:

)

if choice==3:
 

print('THANK	YOU	FOR	VISITING	OUR	WEBSITE' print('VISIT	AGAIN')
 
prof=(input('Enter the profession:')) c1.execute("select * from
marriage_service_management.male_details where profession='{}'". format(prof))
data= c1.fetchall()
print("name\t\t address\t\t	appearance\t\t	age\t\t profession\t\t phone_no \t\t ")
for i in data: print (data
[0][0],'\t\t',data[0][1],'\t\t',data[0][2],'\t\t',data
[0][3],'\t\t',data[0][4],'\t\t',data[0][5],'\t\t')
c=input('do you want to continue (y/[n]:)') if c =='y' :
continue
 
else:

)
 
print('THANK	YOU	FOR	VISITING	OUR	WEBSITE' print('VISIT	AGAIN')
 
print('=========================')
if choice==4:
appearance=(input('Enter the appearance:')) c1.execute("select* from
marriage_service_management.female_details where appearance='{}'". format(appearance))
data= c1.fetchall()
print("name\t\t address\t\t caste\t\t	appreance\t\t age\t\t	profession\t\t phone_no \t\t ")
for i in data: print (data
[0][0],'\t\t',data[0][1],'\t\t',data[0][2],'\t\t',data
[0][3],'\t\t',data[0][4],'\t\t',data[0][5],'\t\t')
c=input('do you want to continue (y/[n]:)') if c =='y' :
continue
 
else:

)
 

print('THANK	YOU	FOR	VISITING	OUR	WEBSITE' print('VISIT	AGAIN')
import mysql.connector as sql conn=sql.connect(host='localhost',user='root',passwd='root',charset='utf8 ')
c1=conn.cursor()
c1.execute('create database marriage_service_management') c1.execute('create table marriage_service_management.male_details(name varchar (200),address varchar(20),appearance varchar(100),age bigint(55),profession varchar (255),phone_no	bigint(200))') c1.execute('create table marriage_service_management.female_details(name varchar(100),address varchar(100),appearance varchar(25),age int(4),profession varchar(65),phone_no varchar(15))')
conn.commit()

if conn.is_connected(): c1=conn.cursor()

print('	WE
LCOME	TO	BTS	MATRIMONIAL	SERVICE
 	')
c='y'
while c.lower()=='y': print('=======================')
print("1.provide details") print('2. in search of bridegroom')
choice=int(input('enter the choice:')) if choice==1:
print('==========================')
print('5.Male customer details') print('6.Female customer details') choice=int(input('enter the choice:-'))
if choice==2:
print('========================')
print('3. Handsome Bride ') print('4. Beautiful Groom ')
choice=int(input('enter the choice-')) if choice == 5 :
a=(input('enter the name:')) b=(input('enter the address:')) d=(input('enter the appearance:')) e=(input('enter the age:')) f=(input('enter the profession:')) g=(input('enter the phone_no:')) c1=conn.cursor() sql_insert="insert into
marriage_service_management.male_details values( '{}','{}','{}','{}','{}','{}')".format(a,b,d,e,f,g)
c1.execute(sql_insert) conn.commit()
print ('Details are successfully inserted') c=input('do you want to continue (y/[n]:)') if c =='y' :
continue
 
else:

)
 

print('THANK	YOU	FOR	VISITING	OUR	WEBSITE' print('VISIT	AGAIN')
 
if choice==6:
h=(input('enter the name:')) i=(input('enter the adderss:')) k=(input('enter the appearance:')) l=(input('enter the age:')) m=(input('enter the profession:')) n=(input('enter the phone_no:')) c1=conn.cursor() sql_insert="insert into
marriage_service_management.female_details values( '{}','{}','{}','{}','{}','{}')".format(h,i,k,l,m,n)
c1.execute(sql_insert) conn.commit()
print("Details are successfully inserted") c=input('do you want to continue (y/[n]:)') if c =='y' :
continue
 
else:

)

if choice==3:
 

print('THANK	YOU	FOR	VISITING	OUR	WEBSITE' print('VISIT	AGAIN')
 
prof=(input('Enter the profession:')) c1.execute("select * from
marriage_service_management.male_details where profession='{}'". format(prof))
data= c1.fetchall()
print("name\t\t address\t\t	appearance\t\t	age\t\t profession\t\t phone_no \t\t ")
for i in data: print (data
[0][0],'\t\t',data[0][1],'\t\t',data[0][2],'\t\t',data
[0][3],'\t\t',data[0][4],'\t\t',data[0][5],'\t\t')
c=input('do you want to continue (y/[n]:)') if c =='y' :
continue
 
else:

)
 
print('THANK	YOU	FOR	VISITING	OUR	WEBSITE' print('VISIT	AGAIN')
 
print('=========================')
if choice==4:
appearance=(input('Enter the appearance:')) c1.execute("select* from
marriage_service_management.female_details where appearance='{}'". format(appearance))
data= c1.fetchall()
print("name\t\t address\t\t caste\t\t	appreance\t\t age\t\t	profession\t\t phone_no \t\t ")
for i in data: print (data
[0][0],'\t\t',data[0][1],'\t\t',data[0][2],'\t\t',data
[0][3],'\t\t',data[0][4],'\t\t',data[0][5],'\t\t')
c=input('do you want to continue (y/[n]:)') if c =='y' :
continue
 
else:

)
 

print('THANK	YOU	FOR	VISITING	OUR	WEBSITE' print('VISIT	AGAIN')
