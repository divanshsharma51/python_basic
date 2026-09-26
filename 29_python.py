#File I/O
#Write and append in file
f = open("demo2.txt","w")# w for write / a for append to write at the end

f.write("Hello this is for testing (write nd append) \n File I/O")
f.write("\n hello")

f.close()