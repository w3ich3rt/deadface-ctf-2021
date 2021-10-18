# Boom
100
sql syyntax

Created by: syyntax

DEADFACE actors will be targeting customers they consider low-hanging fruit. Check out Ghost Town and see who they are targeting. Submit the number of target candidates as the flag: flag{#}

Use the MySQL database dump from Body Count.

Hint: Link to discussion DEADFACE Member
https://ghosttown.deadface.io/t/who-are-we-hitting-first/60/10

They are targeting boomer generation (1946-1964)

Now lets dig in the database and count.

`select * from customers WHERE dob like '%1950';`

I counted year for year and do the math on my own.


