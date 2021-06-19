def drawImage(panjang):
    if panjang%2 == 0:
        print("nilai parameter n harus ganjil")
    else:
        for i in range(1,panjang+1):
            if i == ((panjang-1)/2)+1:
                print('*'*panjang)
            elif i == 1:
                print('*'+'='*int((panjang-3)/2)+'*'+'='*int((panjang-3)/2)+'*')
            elif i == panjang:
                print('*'+'='*int((panjang-3)/2)+'*'+'='*int((panjang-3)/2)+'*')
            else:
                print('='*int((panjang-1)/2)+'*'+'='*int((panjang-1)/2))

drawImage(5)