from PIL import Image

class ImageSteg():

    def getRGBVlaues(self,name):
        image = Image.open(name).convert("RGB")
        rgb_values = list(image.getdata())
    
        r = []
        g = []
        b = []

        for i in rgb_values:
            r.append(format(i[0], '08b'))
            g.append(format(i[1], '08b'))
            b.append(format(i[2], '08b'))
    
        return r,g,b

    def getBinOfMsg(self,msg):
        return ''.join([format(ord(char), '08b') for char in (msg+"@#$").replace(' ','|')])

    def encodeImage(self, imageName, newImageName, msg):
        r, g, b = self.getRGBVlaues(imageName)
        rcopy = r.copy()

        for index,i in enumerate(self.getBinOfMsg(msg)):
            rcopy[index] = f'{rcopy[index][:-1]}{i}'

        imageData = []
        for index,data in enumerate(rcopy):
            imageData.append((int(rcopy[index],2),int(g[index],2),int(b[index],2)))


        image = Image.open(imageName).convert("RGB")
        width, height = image.size
        new_image = Image.new("RGB", (width, height))
        new_image.putdata(imageData)
        new_image.save(newImageName)
        new_image.show()


    def decodeImage(self, imageName):
        r,g,b = self.getRGBVlaues(imageName)

        binTxt = ""

        isMsgFound = False

        for i in r:
            if binTxt[-24:] != '010000000010001100100100':
                binTxt += i[-1]
            else:
                isMsgFound = True
                break


        binArr = [binTxt[i:i+8] for i in range(0, len(binTxt), 8)]
        decodedTxt = ""

        for char in binArr:
            decodedTxt += chr(int(char,2))

        return (decodedTxt.replace("|"," "))[:-3] if isMsgFound else None

