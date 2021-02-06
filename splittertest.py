f= open("zout.txt")
c = f.read()
start = c.find("Page count:")
end = start + 60
z = c[start:end]
print(z)
last_close = z.rfind(">") +1
last_open = z.rfind("<")
z = z[last_close:last_open]
# print(start)
print(z)
