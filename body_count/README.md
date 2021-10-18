# Body Count
Points 10
sql syyntax
Created by: syyntax

One of our employees, Jimmie Castora, kept database backups on his computer. DEADFACE compromised his computer and leaked a portion of the database. Can you figure out how many customers are in the database? We want to get ahead of this and inform our customers of the breach.

Submit the flag as flag{#}. For example, flag{12345}.

Download MySQL database dump
SHA1: 5867eeb1466b31eb8d361061fddd99700fc5d739
Password: d34df4c3

## Getting Flag
First of all, change format for import into mariadb
`sed -i 's/utf8mb4_0900_ai_ci/utf8mb4_unicode_ci/g' demonne.sql`
After that, just count:
`select count(cust_id) as NumberOfCustomer from customers;`

Of course you can also just look via less into the dump ;-)


