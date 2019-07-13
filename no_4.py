def jajan(tanggal, uang):
    per_telur = 2000
    if tanggal > 1:
        for i in range(2,tanggal):
            if (tanggal % i) == 0:
                break
        else:
            normal = int(uang/per_telur)
            bonus = int(normal/12)
            total = normal+bonus
            print('Total telur tanggal prima :', total)
    if (tanggal % 2) != 0: #ganjil
        normal = int(uang/per_telur)
        plus = 3
        bonus = int(normal/20)
        bonus = bonus*plus
        total = normal+bonus
        print('Total telur tanggal ganjil :',total)
    else:
        total = int(uang/per_telur)
        print('Total telur tanggal genap :', total)
    if (tanggal % 5) == 0:
        if (bonus % 2) == 0:
            bonus = bonus*10
        else:
            bonus = bonus*5
            total = normal+bonus
        print('Total telur tanggal kelipatan 5 :',total)

print(jajan(25, 50000))