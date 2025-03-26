from PIL import Image
import random
import sys

def compare(img1, img2, pixels1, pixels2):
    compimg = Image.new("RGB", img2.size)
    compimgPx = compimg.load()

    for row in range(img1.size[1]):
        for col in range(img1.size[0]):
            compimgPx[col, row] = (
                (pixels1[col, row][0] + pixels2[col, row][0]) % 256,
                (pixels1[col, row][1] + pixels2[col, row][1]) % 256,
                (pixels1[col, row][2] + pixels2[col, row][2]) % 256,
            )

    compimg.save("flag.png")
    print("Decode Edildi:flag.png")

def randomFill(Rimg, rPixel):
    randomimage = Image.new("RGB", Rimg.size)
    randompix = randomimage.load()
    randomimage2 = Image.new("RGB", Rimg.size)
    random2pix = randomimage2.load()

    for row in range(Rimg.size[1]):
        for col in range(Rimg.size[0]):
            a = random.randint(0, 255)
            b = random.randint(0, 255)
            c = random.randint(0, 255)

            randompix[col, row] = (
                (a + rPixel[col, row][0]) % 256,
                (b + rPixel[col, row][1]) % 256,
                (c + rPixel[col, row][2]) % 256,
            )
            random2pix[col, row] = (
                ((rPixel[col, row][0] - a) + 256) % 256,
                ((rPixel[col, row][1] - b) + 256) % 256,
                ((rPixel[col, row][2] - c) + 256) % 256,
            )

    randomimage.save("rand.png")
    randomimage2.save("rand2.png")

if __name__ == '__main__':
    print("usage: visCrypt.py e img.png\n", "visCrypt.py -d enc1.png enc2.png")

    if len(sys.argv) < 3:
        print("Eksik argüman!")
        sys.exit(1)

    if sys.argv[1] == "e":
        rimg = sys.argv[2]
        Rimg = Image.open(rimg)
        rPixel = Rimg.load()
        randomFill(Rimg, rPixel)

    elif sys.argv[1] == "d":
        if len(sys.argv) < 4:
            print("Eksik argüman! İki şifreli dosya belirtmelisiniz.")
            sys.exit(1)

        enc1png = sys.argv[2]
        enc2png = sys.argv[3]
        img1 = Image.open(enc1png)
        pixels1 = img1.load()
        img2 = Image.open(enc2png)
        pixels2 = img2.load()
        compare(img1, img2, pixels1, pixels2)

    else:
        print("Yanlış giriş!")
