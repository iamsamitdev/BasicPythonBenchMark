# วิธีการตรวจสอบข้อผิดพลาดในโปรแกรม
try:
    num1 = float(input("Enter number 1:"))
    num2 = float(input("Enter number 2:"))

    # หาผลการหาร
    result = num1 / num2
    print("Result num1 / num2 = ", result)
except ValueError:
    print("มีข้อผิดพลาด ข้อมูลที่ป้อนไม่ใช่ตัวเลข")
except ZeroDivisionError:
    print("มีข้อผิดพลาด ไม่สามารถหารด้วย 0 ได้")
