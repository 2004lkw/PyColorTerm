import colortxt

print(colortxt.colorstr("none","yellow","green","TESTING!"))
vv="Hello %s.  We were wondering if you would %s%s today!" % (colortxt.colortxt("yellow","black","player"),colortxt.colorstr("italic","green","black","join"),colortxt.colorstr("underline","yellow","black","us"))
print(vv)
print(colortxt.colorstr("dark","cyan","black","Hello!  This is cyan on black!"))
print(colortxt.colortxt("red","blue","test"))
c=colortxt
l=c.foretxt("red","This is the way to go!")
print(l)
