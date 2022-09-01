f1 = open("BOM.csv","r")
a = f1.readlines()
f1.close()
f2 = open("BOM_1.csv","w")
a[0] = '"Id";"Designator";"Footprint";"Quantity";"Comment";"Supplier and ref";\n'
for l in a :
    l = l.replace(";",",")
    f2.write(l)
f2.close()

f1 = open("POS.csv","r")
a = f1.readlines()
a[0] = '"Designator","Val","Footprint","Mid X","Mid Y","Rotation","Layer"\n'
f2 = open("POS_1.csv", "w")
for l in a:
    l = l.replace("\n",",,")
    l = l + "\n"
    f2.write(l)
f1.close()
f2.close()
