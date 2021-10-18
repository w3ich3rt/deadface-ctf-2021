#!/usr/bin/python3
"""
Ansatz von mir - leider nicht geklappt

from pwn import *
from string import ascii_lowercase

io = remote('code.deadface.io', 50000)


test = io.recvuntil(": ",)
print(test)
test = io.recvline()
print(test[:-1])
test = io.recvuntil(": ")
print(test)
word = list(io.recvline().strip().decode("utf-8"))
print(word)

numbers = []
for letter in word:
    #print(letter)
    number = ord(letter)-97
    numbers.append(number)
    #print(numbers)

print(numbers)
result=sum(numbers)
print("Result: ", result)
io.sendline(str(result))

test = io.recvlines()
print(test)
test = io.recvlines()
print(test)
test = io.recvlines()
print(test)
"""

# https://ctftime.org/writeup/30950
# Funktionierende Lösung von 0x33c

from pwn import *
from string import ascii_lowercase

alphabet = list(ascii_lowercase)
total = 0

r = remote("code.deadface.io", 50000)
r.recvuntil("Your word is: ")
word = r.recvline().decode("UTF-8")
for i in list(word):
    if i in alphabet:
        total += alphabet.index(i)
r.sendline(str(total))
print(r.recvline_contains("flag{".encode()))
