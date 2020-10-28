#file handling - persistent data storage

#operations - read, write


fp = open("hello.txt")

str1 = fp.read() # reads full content from the file
print(str1)

fp.close()

fp = open("hello.txt",'r')
fp.readline() #reads one line at a time


fp.close()


fp = open("hello.txt",'r')
fp.readlines()[-1]
fp.close()

fp = open("hello.txt",'w')
fp.writelines(['Kamesh Mishra\n','Rakesh'])
fp.close()

fp = open("hello.txt",'a')
fp.write("Yogendra")
fp.flush()

#binary files
#image, audio, video exanples

with open('hello.txt', mode='rt') as fp :
   str1 = fp.read()
   print(type(str1))
   print (str1)
   
   
'''How to read and write non text files'''

with open ("data/a.jpg", "rb") as rf :
  with open ("data/b.jpg", "wb") as wf :
    for line in rf :
      wf.write ( line)
