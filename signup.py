import hashlib
from random import randint
from random_word import RandomWords

r = RandomWords()

user = input("What is your username?: ")
password = input("What is your password?: ")
funInteger = int(randint(0, 100))
funIntStr = str(funInteger)
salt = str(r.get_random_word()+funIntStr+r.get_random_word())

beforeOrAfter = int(randint(0,10))

if (beforeOrAfter % 2) == 0:
    saltedPass = str(password+salt)
else:
    saltedPass = str(salt+password)

hash = hashlib.sha256(saltedPass.encode()).hexdigest()

filehandle = open('hashes.txt', 'a')
filehandle.write(user+':'+salt+':'+hash+"\n")
filehandle.close()