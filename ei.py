from matplotlib import pyplot as pi
us=[12,332,16,45]
la=["asus","dell","lenovo","hp"]
e=[0,0,0,0.04]
c=["g","c","blue","red","pink"]
pi.pie(us,labels=la,startangle=270,explode=e,colors=c,autopct='%1.2f%%')
pi.show()