import time
print("---------------")
print("[             ]")
print("[    0   0    ]")
print("[      i      ]")
print("[    -------  ]")
print(" --------------")
print("ยินดีต้อนรับสู่ร้าน roblox shop")
print("ยินดีต้อนรับ")
print("ผมขอโหลดของก่อนนะครับ")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
print("โหลดของเสร็จเเล้ว")
print("เลือกสินค้าที่ต้องการได้เลยครับ")
time.sleep(1)
print("normal pass, vip pass, god pass, game pass")
piece=input("รับอะไรดีครับ")
print("คุณได้เลือก", piece)
peice_price = 0
price = int(input("กรุณาระบุจำนวนที่ต้องการ: "))
if piece == "god pass":
    piece_price = 1500
elif piece == "vip pass":
    piece_price = 1350
elif piece == "normal pass":
    piece_price = 1000
else:
    piece_price = 1000
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
total_price = piece_price * price
print("ราคารวมทั้งหมด:", total_price, "robux")
time.sleep(2)
print("ขอบคุณที่ใช่บริการครับ")
