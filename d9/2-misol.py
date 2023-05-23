def tanga_qaytar(summa):
    tangalar = [100, 25, 10, 5, 1]
    qaytarilgan_tangalar = []
    for tanga in tangalar:
        while summa >= tanga:
            summa -= tanga
            qaytarilgan_tangalar.append(tanga)
    return qaytarilgan_tangalar

print(tanga_qaytar(15))
print(tanga_qaytar(40))
print(tanga_qaytar(16))

input()