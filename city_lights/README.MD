# City Lights
40
sql syyntax

Created by: syyntax

De Monne wants to know how many branch offices were included in the database leak. This can be found by figuring out how many unique cities the employees live in. Submit the flag as flag{#}.

Use the MySQL database dump from Body Count.

## Get the flag
To get this flag use this statement:

select count(distinct(city)) from employees;

MariaDB [demonne]> select count(distinct(city)) from employees;
+-----------------------+
| count(distinct(city)) |
+-----------------------+
|                   444 |
+-----------------------+
1 row in set (0.028 sec)

