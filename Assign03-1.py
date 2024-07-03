bnum = int(input("ใส่ค่าเลขฐานสิบ (1-15) : "))
bnum1 = bnum 
bnum2 = (bnum // 2)
bnum3 = (bnum2 // 2)
bnum4 = (bnum3 // 2)
print("เป็นเลขฐานสอง : ",(bnum4 % 2),(bnum3 % 2),(bnum2 % 2),(bnum1 % 2))
