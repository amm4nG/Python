import math
angka = [68, 84, 75, 82, 68, 90, 62, 88, 76, 93,
         73, 79, 88, 73, 60, 93, 71, 59, 85, 75,
         61, 65, 75, 87, 74, 62, 95, 78, 63, 72,
         66, 78, 82, 75, 94, 77, 69, 74, 68, 60,
         96, 78, 89, 61, 75, 95, 60, 79, 83, 71,
         79, 62, 67, 97, 78, 85, 76, 65, 71, 75,
         65, 80, 73, 57, 88, 78, 62, 76, 53, 74,
         86, 67, 73, 81, 72, 63, 76, 75, 85, 77]
nilai_max = max(angka)
nilai_min = min(angka)
#fungsi menghitung jumlah kelas
def jumlah_kelas():
  return round(1 + 3.32 * math.log10(len(angka)))
#fungsi menghitung interval kelas
def interval_kelas():
  return round((nilai_max - nilai_min)/jumlah_kelas())
#fungsi mencari nilai kategori
def kategori():
  list = []
  for i in range(nilai_min, nilai_max, interval_kelas()):
    list.append(i)
  for i in range(0, len(list)-1): 
    if list[len(list)-1] != nilai_max:
      selisih = nilai_max - list[len(list)-1]
      list[len(list)-1] = list[len(list)-1]+selisih
  return list

def mean():
    k = kategori()
    #perhitungan frekuensi
    frekuensi = [0]*(len(k)-1)
    for i in range(len(k)-2):
        for j in angka:
            if j >= k[i] and j <= k[i+1]-1:
                frekuensi[i]+=1
    for j in angka:
        if j >= k[len(k)-2] and j <= k[len(k)-1]:
            frekuensi[len(k)-2]+=1 
    #perhitungan mid point
    mid_point = [0]*(len(k)-1)
    for i in range(len(k)-2):
        mid_point[i] = (k[i]+k[i+1]-1)/2*frekuensi[i]
    mid_point[len(k)-2] = (k[len(k)-2]+k[len(k)-1])/2*frekuensi[len(k)-2]
    #tampilkan hasil
    print("-"*42)
    print("Kelas \t\t Frekuensi \t Mid Point")
    print("-"*42)
    for i in range(len(k)-2):
        print(k[i],"-",k[i+1]-1,"\t",frekuensi[i],"\t\t",mid_point[i])
    print(k[len(k)-2],"-",k[len(k)-1],"\t",frekuensi[len(frekuensi)-1],"\t\t",mid_point[len(mid_point)-1])
    print("-"*42)
    print("Mean : ",sum(mid_point)/len(angka))
    print("-"*42)
mean()
    
