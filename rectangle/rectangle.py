from PIL import Image

""" 
PIL modülü bize resim üzerinde işlemler yapmamıza yarar. Benim bu kodlar da yaptığım işlem ise, 
kullanıcıdan bazı kordinatlar alınır ve bu kordinatlar üzerinde bir çerçeve oluşturulur. Aslında bunu birçok modül
yapıyor fakat ben bir şeyin mantığını kavramaya çalışmanın daha doğru olduğunu düşünüyorum. O yüzden böyle bir 
kod parçası yayınladım. 
"""


""" Resim dosyamızı açıyoruz """
image = Image.open('face.jpg')

""" Kordinat ile eriştiğimiz noktaların RGB değerlerini değiştirmek için bunu kullanıyoruz. Bu kod pixel değerlerini 
yükleyecektir 
"""
px = image.load()

def Rectangle(x1, x2, y1, color):
    global image
    global px

    assert x1
    assert x2
    assert y1
    assert color in ('blue', 'red', 'black', 'white', 'yellow', 'green', 'grey')

    """ assert python'da çok kullanılan if gibi çalışır. Mutlaka olması gerekir yoksa programı durdurur ve
     AssertionError diye bir çıktı gönderir.
     x1:    Kordinat 1
     x2:    Kordinat 2
     y1:    Kordinat 3
     color: Çerçeve renkleri
     """

    def COLOR_CHECK(clr):

        """:arg
        Bu özellik Rectangle fonksiyonundan aldığımız renk seçeneğini RGB formatında geri döndürür.
        """

        BLUE = (0, 0, 255)
        RED = (255, 0, 0)
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        YELLOW = (255, 255, 0)
        GREEN = (127, 255, 0)
        GREY = (105, 105, 105)

        if clr == "blue":
            return BLUE
        if clr == "red":
            return RED
        if clr == "black":
            return BLACK
        if clr == "white":
            return WHITE
        if clr == "yellow":
            return YELLOW
        if clr == "green":
            return GREEN
        if clr == "grey":
            return GREY

    COLOR = COLOR_CHECK(color)


    while int(x2) <= int(y1):
        px[x1,x2] = COLOR
        x2 += 1

    y1 = 400
    x2 = 5
    x1 = 80
    while int(x1) <= int(y1):
        px[x1,y1] = COLOR
        x1 += 1

    y2 = y1
    y1 = 400
    x2 = 5
    x1 = 80
    while int(y1) > int(x2):
        px[y2, y1] = COLOR
        y1 -= 1

    y1 = 400
    x2 = 5
    x1 = 80
    while int(y1) > int(x1):
        px[y1, x2] = COLOR
        y1 -= 1


""" Hangi kordinatlarımı çerçeve içine alacağımı gösteriyor. Blue ise çerçevenin rengi """
Rectangle(80, 5, 400, 'blue')
image.show()






