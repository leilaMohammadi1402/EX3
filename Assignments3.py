a=float(input("Enter a number for zele aval:"))
b=float(input("Enter a number for zele dovom:"))
c=float(input("Enter a number for zele sevom:"))

if a==0 or b==0 or c==0 :
    print("mosalasi ba in azla vojod nadarad")
elif a<b+c and c<a+b and b<a+c:
    print(" yes mosalas ast")
else:
    print("mosalasi ba in azla vojod nadarad2")