# El Paso
250
sql syyntax

Created by: syyntax

The regional manager for the El Paso branch of De Monne Financial is afraid his customers might be targeted for further attacks. He would like you to find out the dollar value of all outstanding loan balances issued by employees who live in El Paso. Submit the flag as flag{$#,###.##}.

Use the MySQL database dump from Body Count.

## Get the flag

We'll use the same db as before. But now we need an inner join - okay my sql is not quite good, but we'll go through this.
First we need to look at the tables we need. Therefor we could use the `describe` statement.

I think we need the employees city from the employees table (to look for el paso) and the balance rows from the loans table.

So here is, what i made up:
```sql
select employees.city, loans.balance from loans inner join 
	employees on loans.employee_id = employees.employee_id WHERE employees.city like '%Paso%'
```

For sure you can calc that in sql too, but im struggle with that, so i use libre calc -,^ 

There is the flag :)
