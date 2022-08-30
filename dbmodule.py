import pymysql as p

def connect():
    con = p.connect(user="root", password="", host="localhost", database="blog")
    cur=con.cursor()
    return con,cur

def insert_data(t):
    con,cur=connect()
    q="insert into author (username,password,emailid,city) values (%s,%s,%s,%s);"
    cur.execute(q,t)
    con.commit()
    con.close()

def check_data(t):
    con,cur=connect()
    q="select * from author where username=%s and password=%s;"
    cur.execute(q,t)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def check_data2(t):
    con,cur=connect()
    q="select username from author where aid=%s;"
    cur.execute(q,t)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data[0][0]

def insert_post(t):
    con,cur=connect()
    q="insert into author_post (username,title,post) values (%s,%s,%s);"
    cur.execute(q,t)
    con.commit()
    con.close()

def insert_userdata(t):
    con,cur=connect()
    q="insert into user (username,password,emailid,city) values (%s,%s,%s,%s);"
    cur.execute(q,t)
    con.commit()
    con.close()

def check_userdata(t):
    con,cur=connect()
    q="select * from user where username=%s and password=%s;"
    cur.execute(q,t)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def display_authorposdata(t):
    con,cur=connect()
    #step3: write down query to fetchall records from table
    q="select * from author_post where username=%s;"
    #step4: execute a query
    cur.execute(q,t)
    data=cur.fetchall()
    return data



def display_userdata():
    con,cur=connect()
    #step3: write down query to fetchall records from table
    q="select * from author_post;"
    #step4: execute a query
    cur.execute(q)
    data=cur.fetchall()
    return data

def display_authornames():
    con,cur=connect()
    #step3: write down query to fetchall records from table
    q="select username from author_post;"
    #step4: execute a query
    cur.execute(q)
    data=cur.fetchall()
    lst=[]
    for i in data:
        for j in i:
            if j not in lst:
                lst.append(j)

    return lst

def display_editposdata(t):
    con,cur=connect()
    #step3: write down query to fetchall records from table
    q="select * from author_post where pid=%s;"
    #step4: execute a query
    cur.execute(q,t)
    data=cur.fetchall()
    return data

def update_post(t):
    con,cur=connect()
    q="update author_post set username=%s,title=%s,post=%s where pid=%s"
    cur.execute(q,t)
    con.commit()
    con.close()

def delete_data(t):
    con,cur=connect()
    q="delete from author_post where pid=%s"
    cur.execute(q,t)
    con.commit()
    con.close()



    