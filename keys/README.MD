# Keys
Points 20
sql syyntax

Created by: syyntax

One of De Monne's database engineers is having issues rebuilding the production database. He wants to know the name of one of the foreign keys on the loans database table. Submit one foreign key name as the flag: flag{foreign-key-name} (can be ANY foreign key).

Use the MySQL database dump from Body Count.

## Getting the flag

Just use `show create table loans;` on the table loans while db demonne from the body count is in use.
Now you can extract one foreign key.

fk_loans_cust_id
