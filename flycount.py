txt=open("datall.csv","r").read()
databank=list(txt.split("\n"))
n=len(databank)-1
counts={}
for i in databank:
    if i == "白焦小":
        types="A1"
    elif i=="红直长":
        types="A2"
    elif i=="白直长":
        types="B1"
    elif i=="红焦小":
        types="B2"
    elif i=="红焦长":
        types="C1"
    elif i=="白直小":
        types="C2"
    elif i=="红直小":
        types="D1"
    elif i=="白焦长":
        types="D2"
    else:
        types="others"
    counts[types]=counts.get(types,0)+1
s1=counts.get("C1")+counts.get("C2")+counts.get("D1")+counts.get("D2")
s2=counts.get("C1")+counts.get("C2")+counts.get("B1")+counts.get("B2")
s3=counts.get("B1")+counts.get("B2")+counts.get("D1")+counts.get("D2")
print("m-sn3间的重组值是{:.1f}%".format(s1*100/n))
print("m-w  间的重组值是{:.1f}%".format(s3*100/n))
print("w-sn3间的重组值是{:.1f}%".format(s2*100/n))
x=counts.get("C1")+counts.get("C2")
import turtle as tt
tt.penup()
tt.fd(-(s1+s2+40)/2)
tt.pendown()
tt.pensize(10)
tt.pencolor("violet")
tt.fd(s1+s2+40)
tt.penup()
tt.fd(-10)
tt.pencolor("darkgreen")
tt.pensize(15)
tt.pendown()
tt.fd(-5)
tt.pencolor("black")
tt.write("w",font=(100))
tt.penup()
tt.fd(-s2/2)
tt.pendown()
tt.write("{:.1f}".format(s2*100/n),font=(100))
tt.penup()
tt.fd(-s2/2)
tt.pencolor("darkgreen")
tt.pendown()
tt.fd(-5)
tt.pencolor("black")
tt.write("sn3",font=(100))
tt.penup()
tt.fd(-s1/2)
tt.pendown()
tt.write("{:.1f}".format(s1*100/n),font=(100))
tt.penup()
tt.fd(-s1/2)
tt.pencolor("darkgreen")
tt.pendown()
tt.fd(-5)
tt.pencolor("black")
tt.write("m",font=(100))
tt.penup()
tt.seth(-90)
tt.fd(40)
tt.pensize(3)
tt.pendown()
tt.fd(10)
tt.fd(-5)
tt.seth(0)
tt.fd((s1+s2+15)/2)
tt.write("{0:.1f}+{1:.1f}={2:.1f}".format(s3*100/n,x*200/n,(s1+s2)*100/n),font=(100))
tt.fd((s1+s2+15)/2)
tt.seth(90)
tt.fd(5)
tt.fd(-10)
tt.fd(5)
tt.seth(0)
print("校正值：{}%".format(x*200/n))
print("并发率：{:.2f}".format(x*1000/(s1*s2)))
print("干涉： {:.2f}".format(1-x*1000/(s1*s2)))



