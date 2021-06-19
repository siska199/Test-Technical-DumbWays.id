data = [['Keren'], ['D','W','B','T','A','S','U','D','M','O','Y','T','I','D'], ['Sekali']]

hasil = []
for i in "DUMBWAYSDOTID":
    for k in data[1]:
        if i==k:
            hasil.append(k)
            break

print(''.join(data[0])+' '+''.join(hasil)+' '+''.join(data[0]))
