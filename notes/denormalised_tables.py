#!/usr/bin/env python
# coding: utf-8

# # Lesson 2 Exercise 2: Creating Denormalized Tables
# 
# <img src="images/postgresSQLlogo.png" width="250" height="250">

# ## Walk through the basics of modeling data from normalized form to denormalized form. We will create tables in PostgreSQL, insert rows of data, and do simple JOIN SQL queries to show how these multiple tables can work together. 
# 
# #### Where you see ##### you will need to fill in code. This exercise will be more challenging than the last. Use the information provided to create the tables and write the insert statements.
# 
# #### Remember the examples shown are simple, but imagine these situations at scale with large datasets, many users, and the need for quick response time. 

# ### Import the library 
# Note: An error might popup after this command has exectuted. If it does read it careful before ignoring. 

# In[1]:


import psycopg2


# ### Create a connection to the database, get a cursor, and set autocommit to true

# In[2]:


try: 
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
except psycopg2.Error as e: 
    print("Error: Could not make connection to the Postgres database")
    print(e)
try: 
    cur = conn.cursor()
except psycopg2.Error as e: 
    print("Error: Could not get cursor to the Database")
    print(e)
conn.set_session(autocommit=True)


# #### Let's start with our normalized (3NF) database set of tables we had in the last exercise, but we have added a new table `sales`. 
# 
# ```
# Table Name: transactions2 
# Column 0: Transaction Id
# Column 1: Customer Name
# Column 2: Cashier Id
# Column 3: Year
# ```
# 
# ```
# Table Name: albums_sold
# Column 0: Album Id
# Column 1: Transaction Id
# Column 3: Album Name
# ```
# 
# ```
# Table Name: employees
# Column 0: Employee Id
# Column 1: Employee Name
# ```
# 
# ```
# Table Name: sales
# Column 0: Transaction Id
# Column 1: Amount Spent
# ```
# 
# <img src="images/table16.png" width="450" height="450"> <img src="images/table15.png" width="450" height="450"> <img src="images/table17.png" width="350" height="350"> <img src="images/table18.png" width="350" height="350">
# 

# In[10]:


try:
    cur.execute("drop table albums_sold")
except psycopg2.Error as e:
    print('Error dropping albums_sold table')
    print(e)


# ### TO-DO: Add all `CREATE` statements for all tables and `INSERT` data into the tables
# 

# In[11]:


# TO-DO: Add all Create statements for all tables
try: 
    cur.execute("create table if not exists transactions2    (transaction_id int,     customer_name varchar,     cashier_id int,     year int)")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

try: 
    cur.execute("create table if not exists albums_sold    (album_id int,     transaction_id int,     album_name varchar);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

try: 
    cur.execute("create table if not exists employees    (employee_id int,    employee_name varchar)")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

try: 
    cur.execute("create table if not exists sales    (transaction_id int,    amount_spent int)")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

      
# TO-DO: Insert data into the tables    
    
    
    
try: 
    cur.execute("INSERT INTO transactions2 (transaction_id, customer_name, cashier_id, year)                  VALUES (%s, %s, %s, %s)",                  (1, "Amanda", 1, 2000))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO transactions2 (transaction_id, customer_name, cashier_id, year)                  VALUES (%s, %s, %s, %s)",                  (2, "Toby", 1, 2000))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO transactions2 (transaction_id, customer_name, cashier_id, year)                  VALUES (%s, %s, %s, %s)",                  (3, "Max", 2, 2018))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name)                  VALUES (%s, %s, %s)",                  (1, 1, "Rubber Soul"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name)                  VALUES (%s, %s, %s)",                  (2, 1, "Let It Be"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name)                  VALUES (%s, %s, %s)",                  (3, 2, "My Generation"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name)                  VALUES (%s, %s, %s)",                  (4, 3, "Meet the Beatles"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name)                  VALUES (%s, %s, %s)",                  (5, 3, "Help!"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO employees (employee_id, employee_name)                  VALUES (%s, %s)",                  (1, "Sam"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO employees (employee_id, employee_name)                  VALUES (%s, %s)",                  (2, "Bob"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)    
    
try: 
    cur.execute("INSERT INTO sales (transaction_id, amount_spent)                  VALUES (%s, %s)",                  (1, 40))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)    
    
try: 
    cur.execute("INSERT INTO sales (transaction_id, amount_spent)                  VALUES (%s, %s)",                  (2, 19))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e) 

try: 
    cur.execute("INSERT INTO sales (transaction_id, amount_spent)                  VALUES (%s, %s)",                  (3, 45))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e) 


# #### TO-DO: Confirm using the Select statement the data were added correctly

# In[12]:


print("Table: transactions2\n")
try: 
    cur.execute("SELECT * FROM transactions2;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()

print("\nTable: albums_sold\n")
try: 
    cur.execute("SELECT * FROM albums_sold;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()

print("\nTable: employees\n")
try: 
    cur.execute("SELECT * FROM employees;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()
    
print("\nTable: sales\n")
try: 
    cur.execute("SELECT * FROM sales;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()


# ### Let's say you need to do a query that gives:
# 
# ```
# transaction_id
# customer_name
# employee_name
# year
# album_name
# amount_spent
# ```
# 
# 
# ### TO-DO: Complete the statement below to perform a 3 way `JOIN` on the 4 tables you have created. 

# In[20]:


try: 
    cur.execute("select transactions2.transaction_id,customer_name,employee_name,year,album_name,amount_spent     from (transactions2 join albums_sold on transactions2.transaction_id=albums_sold.transaction_id) join     sales on transactions2.transaction_id=sales.transaction_id     join employees on transactions2.cashier_id=employees.employee_id")
    
    
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()


# #### Great we were able to get the data we wanted.
# 
# ### But, we had to perform a 3 way `JOIN` to get there. While it's great we had that flexibility, we need to remember that `JOINS` are slow and if we have a read heavy workload that required low latency queries we want to reduce the number of `JOINS`.  Let's think about denormalizing our normalized tables.

# ### With denormalization you want to think about the queries you are running and how to reduce the number of JOINS even if that means duplicating data. The following are the queries you need to run.

# #### Query 1: `SELECT transaction_id, customer_name, amount_sent FROM <min number of tables>`
# It should generate the amount spent on each transaction 
# #### Query 2: `SELECT cashier_name, SUM(amount_spent) FROM <min number of tables> GROUP BY cashier_name`
# It should generate the total sales by cashier 

# ###  Query 1: `SELECT transaction_id, customer_name, amount_spent FROM <min number of tables>`
# 
# One way to do this would be to do a JOIN on the `sales` and `transactions2` table but we want to minimize the use of `JOINS`.  
# 
# To reduce the number of tables, first add `amount_spent` to the `transactions` table so that you will not need to do a JOIN at all. 
# 
# ```
# Table Name: transactions 
# Column 0: Transaction Id
# Column 1: Customer Name
# Column 2: Cashier Id
# Column 3: Year
# Column 4: Amount Spent
# ```
# 
# 
# <img src="images/table19.png" width="450" height="450">
# 

# ### TO-DO: Add the tables as part of the denormalization process

# In[23]:


# TO-DO: Create all tables
try: 
    cur.execute("create table if not exists transactions     (transaction_id int,     customer_name varchar,     cashier_id int,     year int,     amount_spend int)")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)



#Insert data into all tables 
    
try: 
    cur.execute("INSERT INTO transactions (transaction_id,customer_name,cashier_id,year,amount_spend)                  VALUES (%s, %s, %s, %s, %s)",                  (1,"Amanda",1,2000,40))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO transactions (transaction_id,customer_name,cashier_id,year,amount_spend)                  VALUES (%s, %s, %s, %s, %s)",                  (2,"Toby",1,2000,19))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO transactions (transaction_id,customer_name,cashier_id,year,amount_spend)                  VALUES (%s, %s, %s, %s, %s)",                  (3,"Max",2,2018,45))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)


# ### Now you should be able to do a simplifed query to get the information you need. No  `JOIN` is needed.

# In[26]:


try: 
    cur.execute("select transaction_id,customer_name,amount_spend from transactions")
        
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()


# #### Your output for the above cell should be the following:
# (1, 'Amanda', 40)<br>
# (2, 'Toby', 19)<br>
# (3, 'Max', 45)

# ### Query 2: `select cashier_name, SUM(amount_spent) FROM <min number of tables> GROUP BY cashier_name` 
# 
# To avoid using any `JOINS`, first create a new table with just the information we need. 
# 
# `Table Name: cashier_sales
# col: Transaction Id
# Col: Cashier Name
# Col: Cashier Id
# col: Amount_Spent
# `
# 
# <img src="images/table20.png" width="350" height="350">
# 
# ### TO-DO: Create a new table with just the information you need.

# In[28]:


# Create the tables

try: 
    cur.execute("create table if not exists cashier_sales(transaction_id int,    cashier_name varchar,     cashier_id int,     amunt_spent int)")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)


#Insert into all tables 
    
try: 
    cur.execute("INSERT INTO cashier_sales                   VALUES (%s, %s, %s, %s)",                  (1,'Sam',1,40 ))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO cashier_sales                   VALUES (%s, %s, %s, %s)",                  (2,'Sam',1,19 ))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO cashier_sales                   VALUES (%s, %s, %s, %s)",                  (3,"Bob",2,45))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)


# ### Run the query

# In[30]:


try: 
    cur.execute("select cashier_name, SUM(amunt_spent) FROM cashier_sales GROUP BY cashier_name")
        
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()


# #### Your output for the above cell should be the following:
# ('Sam', 59)<br>
# ('Bob', 45)
# 

# #### We have successfully taken normalized table and denormalized them inorder to speed up our performance and allow for simplier queries to be executed. 

# ### Drop the tables

# In[ ]:


try: 
    cur.execute("DROP table ####")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
try: 
    cur.execute("DROP table #####")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
try: 
    cur.execute("DROP table #####")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
try: 
    cur.execute("DROP table #####")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
try: 
    cur.execute("DROP table #####")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
try: 
    cur.execute("DROP table #####")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)


# ### And finally close your cursor and connection. 

# In[31]:


cur.close()
conn.close()


# In[ ]:




