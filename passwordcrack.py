import sys
import hashlib

count=0

pass_hash = input("Enter the md5 hash : ")

wordlist = input("Enter the file name : ")

try:
  pass_file = open (wordlist, "r")
except:
  print("No file found")
  quit()

for word in pass_file:
  enc_word= word.encode('utf-8') 
  digest= hashlib.md5(enc_word.strip()).hexdigest()

  if digest == pass_hash:
    print("Yaayy!! Password found. ")
    print("Password is : "+ word)
    count=1
    break
  
if count==0:
  print("Password is not in the list :(")