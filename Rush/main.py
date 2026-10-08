#!/usr/bin/env python3
# โค้ดนี้ใช้สำหรับการนำเข้าฟังก์ชัน checkmate จากไฟล์ checkmate.py
from checkmate import checkmate

def main():
    # กำหนดผืนกระดานหมากรุกจำลอง (String) แบบ N x N
    # \ หน้าข้อความช่วยตัดบรรทัดใหม่แรกสุดออก เพื่อให้อยู่ในรูปแบบบรรทัดที่ถูกต้อง
    board = """\
R...
.K..
..P.
....\
"""
    # เรียกใช้ฟังก์ชัน checkmate เพื่อส่งกระดานเข้าไปประมวลผล
    checkmate(board)

# ตรวจสอบว่าสคริปต์นี้ถูกรันโดยตรง (ไม่ได้ถูก import ไปใช้ที่อื่น)
if __name__ == "__main__":
    main()