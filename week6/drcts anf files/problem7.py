f = open("text","r")
txt = f.read()
f.close()

p = open("text",'w')
p.write(txt)
p.close()