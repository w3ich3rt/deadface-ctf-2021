# All A-Loan
Points 375
sql syyntax

Created by: syyntax

De Monne has reason to believe that DEADFACE will target loans issued by employees in California. It only makes sense that they'll then target the city with the highest dollar value of loans issued. Which city in California has the most money in outstanding Small Business loans? Submit the city and dollar value as the flag in this format: flag{City_$#,###.##}

Use the MySQL database dump from Body Count

To get the balances of the cities from the employees from california:

`select loans.amt, loans.balance, employees.city, employees.state, loan_types.description from loans  inner join employees on loans.employee_id = employees.employee_id  inner join loan_types on loans.loan_type_id = loan_types.loan_type_id  where employees.state = 'CA' and loans.loan_type_id = 3 ORDER BY loans.balance DESC`

Also look at the xlsx.


