# เซตสำหรับตรวจสอบหมากฝ่ายตรงข้ามที่มีความสามารถในการรุก
PIECES = {'P', 'B', 'R', 'Q'}

def checkmate(board):
    # 1. แปลงข้อความกระดานเป็นลิสต์ของแต่ละแถว พร้อมตัดช่องว่างต้น-ท้ายแถวออก
    rows = [r.strip() for r in board.splitlines()]
    n = len(rows)

    # ตรวจสอบความถูกต้อง: กระดานต้องไม่ว่างเปล่า และต้องเป็นสี่เหลี่ยมจัตุรัส N x N
    if not rows or any(len(r) != n for r in rows):
        print("Error")
        return

    # 2. ค้นหาตำแหน่งของ King ('K') ทั้งหมดบนกระดาน
    kings = []
    for r in range(n): 
        for c in range(n):
            if rows[r][c] == 'K':
                kings.append((r, c))

    # กฎของเกม: บนกระดานต้องมี King เพียงตัวเดียวเท่านั้น
    if len(kings) != 1:
        print("Error")
        return

    kr, kc = kings[0]  # ตำแหน่งแถว (kr) และคอลัมน์ (kc) ของ King

    # 3. ตรวจสอบการรุกจาก Pawn ('P')
    # เนื่องจาก Pawn เดินกินเฉียงขึ้นข้างบน ตัว Pawn ที่จะรุก King ได้จึงต้องอยู่ "ล่างซ้าย" หรือ "ล่างขวา" ถัดไป 1 ช่อง
    for pr, pc in [(kr + 1, kc - 1), (kr + 1, kc + 1)]:
        if 0 <= pr < n and 0 <= pc < n and rows[pr][pc] == 'P':
            print("Success")  # King ถูกรุก[cite: 13, 21]
            return

    # 4. ตรวจสอบการรุกระยะไกลทั้ง 8 ทิศทาง (Rook, Bishop, Queen)
    # ลิสต์ของทิศทาง: (แนวตั้ง/แนวนอน 4 ทิศ) และ (แนวเฉียง 4 ทิศ)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for dr, dc in directions:
        r, c = kr + dr, kc + dc

        # วนลูปสแกนไปตามทิศทางนั้นๆ จนกว่าจะสุดขอบกระดาน
        while 0 <= r < n and 0 <= c < n:
            ch = rows[r][c]

            # ถ้าพบหมากฝั่งตรงข้าม หรือพบ King
            if ch in PIECES or ch == 'K':
                is_straight = (dr == 0 or dc == 0)  # เป็นทิศแนวตั้ง/แนวนอนหรือไม่

                # กรณีทิศแนวตรง: Rook หรือ Queen สามารถรุกได้
                if is_straight and ch in ('R', 'Q'):
                    print("Success")[cite: 13, 21]
                    return

                # กรณีทิศแนวเฉียง: Bishop หรือ Queen สามารถรุกได้
                if not is_straight and ch in ('B', 'Q'):
                    print("Success")[cite: 13, 21]
                    return

                # หากเจอหมากตัวอื่นบังเส้นทางไว้ (ไม่สามารถรุกได้ในทิศนี้) ให้หยุดสแกนทิศนี้ทันที
                break

            # ขยับไปสแกนช่องถัดไปในทิศทางเดิม
            r += dr
            c += dc

    # 5. หากสแกนครบทุกทิศทางแล้วไม่พบการรุก ให้แสดงผลว่าปลอดภัย
    print("Fail")