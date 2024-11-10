import imageSteg
import optparse
import sys
import os


helpTxt = f"Usage: {sys.argv[0]} <command> [options]\nCommand: - \n\tencode: to encode a message\n\tdecode: to decode a message\nOptions: -\n\t-f filename\n\t-m message (only when encoding)\n\t-n new file name (only when encoding)"

asciiArt = r"""
  ____                       ____  _
 / ___|_ __ ___  ___ _ __   / ___|| |_ ___  __ _  ___
| |  _| '__/ _ \/ _ \ '_ \  \___ \| __/ _ \/ _` |/ _ \
| |_| | | |  __/  __/ | | |  ___) | ||  __/ (_| | (_) |
 \____|_|  \___|\___|_| |_| |____/ \__\___|\__, |\___/
                                           |___/
                        -----HW-------------------                                        

                                           """
print(asciiArt)

if len(sys.argv) < 2:
    print(helpTxt)
    sys.exit(1)
    
parser = optparse.OptionParser()
parser.add_option("-f","--filename",dest="fileName")
parser.add_option("-m","--message",dest="msg")
parser.add_option("-n","--newfilename",dest="newFileName")

(option, args) = parser.parse_args()

stego  = imageSteg.ImageSteg()

if(sys.argv[1].lower() == "encode"):
    if(option.fileName != None and option.msg != None and option.newFileName):
        if  os.path.exists(option.fileName) and (option.fileName.endswith(".png") or (option.fileName.endswith(".jpg"))):
            print(f"[+] Image found: {option.fileName}\n[+] If the message had encoded successfylly the encoded image will be open automatically")
            stego.encodeImage(option.fileName, option.newFileName, option.msg)
            if stego.decodeImage(option.newFileName) == option.msg:
                print(f"[+] Text encode was successful: {option.newFileName}")
            else:
                print("[+] Text encode was unsuccessful. Try a different image")

        else:
            print("[-] Check the filename again.")
    else:
        print(helpTxt)

elif  (sys.argv[1].lower() == "decode"):
    if(option.fileName != None):
        if  os.path.exists(option.fileName) and ((option.fileName.endswith(".png") or option.fileName.endswith(".jpg"))):
            print(f"[+ Image found: {option.fileName}\n[+] Decoding the image")
            decodedMsg = stego.decodeImage(option.fileName)
            if decodedMsg != None:
                print("[+] The hidded message is: ", decodedMsg)
            else:
                print("[+] Not an encoded image")
        else:
            print("[-] Check the filename again.")
    else:
        print(helpTxt)
else:
    print(helpTxt)
