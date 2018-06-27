#Question 1
print("Question 1")
import pymysql
try:
    connection = pymysql.connect(host='localhost', database='demo', user='helpme')
    print(connection)
finally:
    connection.close()
    print('Done!!')
import pymysql as pm
try:
    cursor=''
    con=''
    con=pm.connect(host='localhost', database='demo', user='helpme', password='helpme')
    cursor=con.cursor()
    query  = 'create table Books(BookID int(5) primary key, TitleID varchar(10), FOREIGN KEY (TitleID) REFERENCES Titles(TitleID), Location varchar(10), Genre varchar(10))'
    query2 ='create table Titles(TitleID varchar(10) primary key, Title varchar(10), PublisherID varchar(5), FOREIGN KEY (PublisherID) REFERENCES Publish(PublisherID), PublicationYear int(4))'
    query3 = 'create table ZipCodes(ZipCodeID int(5) primary key, City varchar(5), State varchar(5), ZipCode int(5))'
    query4 = 'create table Publishers(PublisherID varchar(5) primary key, Name varchar(10), StreetAddress varchar(4), SuiteNumber int(3), ZipCodeID int(5), FOREIGN KEY (ZipCodeID) REFERENCES ZipCodes(ZipCodeID))'
    cursor.execute(query)
    cursor.execute(query2)
    cursor.execute(query3)
    cursor.execute(query4)
    print('Table created successfully!!')
except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
finally:
    if cursor :
        cursor.close()
    if con:
        con.close()
        print('Done!!')
#Question 2
print("Question 2")
try:
    con = pm.connect(host='localhost', database='demo', user='helpme')
    cursor = con.cursor()
    query = "insert into Books(BookID, TitleID, Location, Genre) \
        values(%s, %s, %s, %s)"
    records = [(1, 'IIS', '412B', 'Love'),
               (2, 'GG', '201B', 'Crime')]
    cursor.executemany(query,records)
    query2 = "insert into Titles(TitleID, Title, PublisherID, PublicationYear) \
        values(%s, %s, %s, %s)"
    records2 = [('IIS', 'If I Stay', 'HH', 2014),
                ('GG', 'Gone Girl', 'HM', 2002)]
    cursor.executemany(query2, records2)
    query4 = "insert into Publishers(PublisherID, Name, StreetAddress, SuiteNumber, ZipCodeID) \
        values(%s, %s, %s, %s, %s)"
    records3 = [('HH', 'Penguin', '22St', 102, 2),
                ('HM', 'Paper Boat', '15St', 45, 4)]
    cursor.executemany(query4, records3)
    query3 = "insert into ZipCodes(ZipCodeID, City, State, ZipCode) \
            values(%s, %s, %s, %s)"
    records4 = [(2, 'Delhi', 'NCR', 250001),
                (4, 'Goa', 'MH', 248001)]
    cursor.executemany(query3, records4)
    con.commit()
except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
        print('Done!!')
#Question 3
print("Question 3")
try: 
    con = pm.connect(host='localhost', database='demo', user='helpme')
    cursor = con.cursor() 
    query = "update ZipCodes set ZipCode =104001 where ZipCodeID =2" 
    cursor.execute(query) 
    con.commit() 
except pm.DatabaseError as e: 
    if con: 
        con.rollback() 
        print('Problem occured: ', e) 
finally: 
    if cursor: 
        cursor.close() 
    if con: 
        con.close() 
        print('Done!!') 
