#check installation of Pillow:

def install_Pillow(package):
    import importlib
    try:
        from PIL import Image
        print("PIL already installed \n")

    except ImportError:
        print("Pillow not installed, Installing Pillow, make sure you have an active internet connections.")
        import pip
        pip.main(['install', package])
        from PIL import Image
        
install_Pillow('Pillow')

#importing required files

from PIL import ImageFont
from PIL import ImageDraw


file = open("candidate_list.txt")


#Adjust you y-coordinate here
y_coordinate = 656

try:
    for name in file:
        name = name.rstrip()
        img = Image.open("Your-Blank-Certificate/certificate.png")
        width, height = img.size
        draw = ImageDraw.Draw(img)
        #Change Font size here, currently its set to 90
        font = ImageFont.truetype("Font/j.ttf", 90)
        offset = 10
        x_coordinate = int(width / 2 - font.getsize(name)[0] / 2) + offset
        draw.text((x_coordinate, y_coordinate), name, (255, 0, 0), font=font)
        img.save("Your-Certificates/" + str(name) + ".png", "PNG")
        print(f"Done For {name}")
except:
    print("Woah.... Try Again")