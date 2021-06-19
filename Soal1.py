import random as rd

def cetakNilaiAcak(n):
    j_acak = []
    for i in range(n):
        list_huruf_angka = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','g','r','s','t','u','v','w','x','y','z']
        nilai_acak = []
        for k in range(28):
            nilai_acak.append(rd.choice(list_huruf_angka))
        print(''.join(nilai_acak))

cetakNilaiAcak(3)
