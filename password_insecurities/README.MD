# Password Insecurities
Points 50

Created by: syyntax

It looks like DEADFACE is going after the password of one of De Monne's customers: Haily Poutress. She has since changed her password, but De Monne is looking for ways to improve password requirements. De Monne would like you to crack the password from the database leak to determine if Haily's password was secure enough. Submit the flag as flag{password}.

Use the MySQL database dump from Body Count.

Download MySQL database dump
SHA1: 5867eeb1466b31eb8d361061fddd99700fc5d739

Password: d34df4c3

## Import into mariadb
sed -i 's/utf8mb4_0900_ai_ci/utf8mb4_unicode_ci/g' demonne.sql

import into mysql

## Searching for ID
MariaDB [demonne]> select * from customers where last_name like '%Poutress%';
+---------+-----------+------------+----------------------------+---------------------+------------+-------+---------+--------+--------+------------+
| cust_id | last_name | first_name | email                      | street              | city       | state | country | postal | gender | dob        |
+---------+-----------+------------+----------------------------+---------------------+------------+-------+---------+--------+--------+------------+
|    7117 | Poutress  | Haily      | hpoutress5ho@booking.com   | 15212 Westport Hill | Ocala      | FL    | US      | 34479  | M      | 03/12/1995 |
|    9175 | Poutress  | Bobby      | bpoutress72u@imageshack.us | 4219 Express Circle | Saint Paul | MN    | US      | 55166  | M      | 03/15/1978 |
+---------+-----------+------------+----------------------------+---------------------+------------+-------+---------+--------+--------+------------+
2 rows in set (0.009 sec)


##Searching for Passwordhash
MariaDB [demonne]> select * from cust_passwd where cust_id = '7117';
+--------------+---------+------------------------------------+
| cust_pass_id | cust_id | passwd                             |
+--------------+---------+------------------------------------+
|         7117 |    7117 | $1$FigUPHDJ$IYWZKYxoKDdLyODRM.kQq. |
+--------------+---------+------------------------------------+
1 row in set (0.001 sec)

## Identify the hash
Take the hash and looking for the kind, you can use https://hashcat.net/wiki/doku.php?id=example_hashes or other methods.
I'll looked at hashcat and think its md5crypt.
So lets ask john ;)
```shell
john --format=md5crypt pw_hash 
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt, crypt(3) $1$ (and variants) [MD5 256/256 AVX2 8x3])
Will run 16 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst, rules:Wordlist
trustno1         (?)
1g 0:00:00:00 DONE 2/3 (2021-10-15 22:04) 20.00g/s 30720p/s 30720c/s 30720C/s 123456..keeper
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```
So there it is!
```shell
john --format=md5crypt pw_hash  --show
?:trustno1
```

The secret password is "trustno1" not really a good one ;-)
