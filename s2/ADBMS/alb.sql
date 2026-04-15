mysql> CREATE TABLE students(rollno INT PRIMARY KEY,name VARCHAR(30),course VARCHAR(30),year INT);
Query OK, 0 rows affected (0.26 sec)

mysql> SHOW TABLES
    -> ;
+-----------------+
| Tables_in_albin |
+-----------------+
| students        |
+-----------------+
1 row in set (0.00 sec)

mysql> DESC students;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| rollno | int(11)     | NO   | PRI | NULL    |       |
| name   | varchar(30) | YES  |     | NULL    |       |
| course | varchar(30) | YES  |     | NULL    |       |
| year   | int(11)     | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
4 rows in set (0.01 sec)
mysql> ALTER TABLE students
    -> ADD place INT;
Query OK, 0 rows affected (0.46 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> DESC students;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| rollno | int(11)     | NO   | PRI | NULL    |       |
| name   | varchar(30) | YES  |     | NULL    |       |
| course | varchar(30) | YES  |     | NULL    |       |
| year   | int(11)     | YES  |     | NULL    |       |
| place  | int(11)     | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
5 rows in set (0.00 sec)

mysql> TRUNCATE TABLE students;
Query OK, 0 rows affected (0.19 sec)

mysql> desc students;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| rollno | int(11)     | NO   | PRI | NULL    |       |
| name   | varchar(30) | YES  |     | NULL    |       |
| course | varchar(30) | YES  |     | NULL    |       |
| year   | int(11)     | YES  |     | NULL    |       |
| place  | int(11)     | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
5 rows in set (0.00 sec)
mysql> ALTER TABLE students
    -> RENAME TO student;
Query OK, 0 rows affected (0.12 sec)
mysql> SHOW TABLES;
+-----------------+
| Tables_in_albin |
+-----------------+
| student         |
+-----------------+
1 row in set (0.00 sec)
mysql> ALTER TABLE student
    -> CHANGE year annual_income int;
Query OK, 0 rows affected (0.08 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> DESC student;
+---------------+-------------+------+-----+---------+-------+
| Field         | Type        | Null | Key | Default | Extra |
+---------------+-------------+------+-----+---------+-------+
| rollno        | int(11)     | NO   | PRI | NULL    |       |
| name          | varchar(30) | YES  |     | NULL    |       |
| course        | varchar(30) | YES  |     | NULL    |       |
| annual_income | int(11)     | YES  |     | NULL    |       |
| place         | int(11)     | YES  |     | NULL    |       |
+---------------+-------------+------+-----+---------+-------+
5 rows in set (0.00 sec)
mysql> INSERT INTO student
    -> (rollno,name,course,annual_income,place)
    -> VALUES (1,'alan','MCA',120000,15);
Query OK, 1 row affected (0.05 sec)

mysql> SELECT * FROM student;
+--------+------+--------+---------------+-------+
| rollno | name | course | annual_income | place |
+--------+------+--------+---------------+-------+
|      1 | alan | MCA    |        120000 |    15 |
+--------+------+--------+---------------+-------+
1 row in set (0.00 sec)
mysql> alter table student change place place varchar(30);
Query OK, 1 row affected (0.72 sec)
Records: 1  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM student;
+--------+------+--------+---------------+-------+
| rollno | name | course | annual_income | place |
+--------+------+--------+---------------+-------+
|      1 | alan | MCA    |        120000 | 15    |
+--------+------+--------+---------------+-------+
1 row in set (0.00 sec)
mysql> update student set place = 'pooyamkutty' where rollno = 1;
Query OK, 1 row affected (0.07 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM student;
+--------+------+--------+---------------+-------------+
| rollno | name | course | annual_income | place       |
+--------+------+--------+---------------+-------------+
|      1 | alan | MCA    |        120000 | pooyamkutty |
+--------+------+--------+---------------+-------------+
1 row in set (0.00 sec)

mysql> CREATE TABLE employee (emp_id INT PRIMARY KEY,name VARCHAR(30), age INT, salary INT);
Query OK, 0 rows affected (0.65 sec)

mysql> SHOW TABLEs;
+-----------------+
| Tables_in_albin |
+-----------------+
| employee        |
| student         |
+-----------------+
2 rows in set (0.01 sec)

mysql> DESC employee;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| emp_id | int(11)     | NO   | PRI | NULL    |       |
| name   | varchar(30) | YES  |     | NULL    |       |
| age    | int(11)     | YES  |     | NULL    |       |
| salary | int(11)     | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
4 rows in set (0.00 sec)

ALTER TABLE employee
    -> ADD dept VARCHAR(30);
Query OK, 0 rows affected (0.65 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> DESC employee;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| emp_id | int(11)     | NO   | PRI | NULL    |       |
| name   | varchar(30) | YES  |     | NULL    |       |
| age    | int(11)     | YES  |     | NULL    |       |
| salary | int(11)     | YES  |     | NULL    |       |
| dept   | varchar(30) | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
5 rows in set (0.00 sec)

 INSERT INTO employee VALUES (2,'alan',76,5000,'security'),(3,'albin',22,150000,'manager');
Query OK, 2 rows affected (0.04 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM employee;
+--------+-------+------+--------+-----------+
| emp_id | name  | age  | salary | dept      |
+--------+-------+------+--------+-----------+
|      1 | alby  |   21 |  50000 | designing |
|      2 | alan  |   76 |   5000 | security  |
|      3 | albin |   22 | 150000 | manager   |
+--------+-------+------+--------+-----------+
3 rows in set (0.00 sec)

mysql> create table Salesman(salesman_id int primary key,name
varchar(20),city varchar(20),commission float);
Query OK, 0 rows affected (0.29 sec)

mysql> insert into Salesman values(5001,'james hoog','New York',0.15),(5002,'Nail Knite','Paris',0.13),(5005,'Pit Alex','London',0.11),(5006,'MC Lyon','paris',0.14),(5007,'Paul Adam','Rome',0.13),(5003,'Lauson Hen','San Jose',0.12);
Query OK, 6 rows affected (0.03 sec)
Records: 6  Duplicates: 0  Warnings: 0

mysql> create table Customer(customer_id int primary key,cust_name varchar(20),city varchar(20),grade int,salesman_id int);
Query OK, 0 rows affected (0.26 sec)

mysql> alter table Customer add foreign key(salesman_id) REFERENCES Salesman(salesman_id);
Query OK, 0 rows affected (0.73 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> insert into Customer values(3002,'Nick Rimando','New York',100,5001),(3007,'Brad Davis','New York',200,5001),(3005,'Graham Zusi','California',200,5002),(3008,'Julian Green','London',300,5002),(3004,'Fabian Johnson','Paris',300,5006),(3009,'Geoff Cameron','Berlin',100,5003),(3003,'JozyAltidor','Moscow',200,5007),(3001,'Brad Guzan','London',100,5005);
Query OK, 8 rows affected (0.13 sec)
Records: 8  Duplicates: 0  Warnings: 0

mysql> select * from Salesman;
+-------------+------------+----------+------------+
| salesman_id | name       | city     | commission |
+-------------+------------+----------+------------+
|        5001 | james hoog | New York |       0.15 |
|        5002 | Nail Knite | Paris    |       0.13 |
|        5003 | Lauson Hen | San Jose |       0.12 |
|        5005 | Pit Alex   | London   |       0.11 |
|        5006 | MC Lyon    | paris    |       0.14 |
|        5007 | Paul Adam  | Rome     |       0.13 |
+-------------+------------+----------+------------+
6 rows in set (0.00 sec)

mysql> select * from Customer;
+-------------+----------------+------------+-------+-------------+
| customer_id | cust_name      | city       | grade | salesman_id |
+-------------+----------------+------------+-------+-------------+
|        3001 | Brad Guzan     | London     |   100 |        5005 |
|        3002 | Nick Rimando   | New York   |   100 |        5001 |
|        3003 | JozyAltidor    | Moscow     |   200 |        5007 |
|        3004 | Fabian Johnson | Paris      |   300 |        5006 |
|        3005 | Graham Zusi    | California |   200 |        5002 |
|        3007 | Brad Davis     | New York   |   200 |        5001 |
|        3008 | Julian Green   | London     |   300 |        5002 |
|        3009 | Geoff Cameron  | Berlin     |   100 |        5003 |
+-------------+----------------+------------+-------+-------------+
8 rows in set (0.00 sec)

 create table orders(ord_no int primary key,purch_amt float,ord_date date,customer_id int,salesman_id int);
Query OK, 0 rows affected (0.28 sec)

mysql> desc ordes;
ERROR 1146 (42S02): Table 'alb123.ordes' doesn't exist
mysql> desc orders;
+-------------+---------+------+-----+---------+-------+
| Field       | Type    | Null | Key | Default | Extra |
+-------------+---------+------+-----+---------+-------+
| ord_no      | int(11) | NO   | PRI | NULL    |       |
| purch_amt   | float   | YES  |     | NULL    |       |
| ord_date    | date    | YES  |     | NULL    |       |
| customer_id | int(11) | YES  |     | NULL    |       |
| salesman_id | int(11) | YES  |     | NULL    |       |
+-------------+---------+------+-----+---------+-------+
5 rows in set (0.00 sec)

mysql> alter table orders add foreign key(salesman_id)REFERENCES salesman(salesman_id);
Query OK, 0 rows affected (0.79 sec)




