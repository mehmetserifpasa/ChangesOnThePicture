## Algorithm
Kullanıcıdan bazı kordinatlar alınır ve bu kordinatlar üzerinde bir çerçeve oluşturulur. Aslında bunu birçok modül
yapıyor fakat ben bir şeyin mantığını kavramaya çalışmanın daha doğru olduğunu düşünüyorum. O yüzden böyle bir 
kod parçası yayınladım. 
* Çerçeve çizmek için bazı kordinatlar verdiğimizi düşünelim. x1=80, x2=5, y1=400. Bu kordinatlar bir çerçeve çizmek için yeterli değişkenlerdir. Aşşağıdaki
kod: X ekseni üzerinde 80, Y ekseni üzerinde 5 noktasına giderek bir nokta belirler. Sonra Y'nin kordinatını arttırarak 400 birim aşşağı kaydırır. Bu kaydırdığı
yerlerin RGB renklerini ise verilen renge göre değişir. Varsayılan kırmızı renktir. px[x1,x2] = COLOR kodu şu demektir: resim üzerindeki x1,x2 yani 80 ve 5 
kordinatına git ve kordinatın RGB rengini kırmızı yap. x2 += 1 ile de x2'nin kordinat düzleminde aşşağı kaydırarak çerçevenin bir kısmını oluşturmuş oluyoruz.
```
    while int(x2) <= int(y1):
        px[x1,x2] = COLOR
        x2 += 1
```
![Ekran Resmi 2020-12-24 23 53 55](https://user-images.githubusercontent.com/25556230/103106527-59e90d80-4647-11eb-9fac-7812256ed8d8.png) 
* Bu kod ise, soldan sağa doğru bir çerçeve çizer.
```
    while int(x1) <= int(y1):
        px[x1,y1] = COLOR
        x1 += 1
```
![Ekran Resmi 2020-12-24 23 54 14](https://user-images.githubusercontent.com/25556230/103106528-5c4b6780-4647-11eb-8e36-1f5731d7f6df.png)

Kodları incelerseniz bu yöntemi diğer bölgelerde de kullandık. 
