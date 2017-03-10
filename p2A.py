#!/usr/bin/python3

from PIL import Image
from io import open
from sys import argv

if argv[1:]:
    image_name = argv[1]    #get script's paramets
else: 
    print("Picture is not specified.")
    exit()

if argv[2:]:
    script_name = argv[2]
else:
    script_name = image_name+'_result'
                
class pixel2ANSI:
    def __init__(self, image_name):
        print("********************")
        self.path = image_name
        self.create_obj(self.path)
        self.create_list(self.img_obj)
        self.fill_list()
        self.write2file()
        print("********************")

    def create_obj(self, path):
        image = Image.open(path)
        size = image.size
        self.img_obj = image.load()
        self.width = size[0]
        self.height = size[1]
        print((
            "#Image object created.\n\t-Size of picture is: " +
            str(self.width) +
            "x"+str(self.height)+"px"
            ))

    def create_list(self, obj):
        if self.height%2==1:
            list_len = self.height//2 + 1
        else:
            list_len = self.height//2
        self.image_list = (
            [[[(0,0,0,0)] * 2 for e in range(self.width)] for i in range(list_len)]
            )
        print((
            "#Array created.\n\t-Width: " +
            str(len(self.image_list[0])) +
            "\n\t-Height:" +
            str(len(self.image_list))
            ))

    def fill_list(self):
        height = 0  #height of image
        l_height = 0#height of result list
        while height < self.height:
            width = 0
            if height%2==0  or height == 0:
                while width < self.width:
                    color1 = self.img_obj[width, height]
                    if len(color1) == 3:
                        color1 += (255,)
                    self.image_list[l_height][width][0] = color1
                    width += 1
                height += 1
            else:
                while width < self.width:
                    color2 = self.img_obj[width, height]
                    if len(color2) == 3:
                        color2 += (255,)
                    self.image_list[l_height][width][1] = color2
                    width += 1
                height += 1
                l_height += 1
        print("#Array filled.")

    def trans_col(self, rgb):
        colors = [
            [(0,0,0,255), 0],      #Black
            [(128,0,0,255), 1],      #Maroon
            [(0,128,0,255), 2],      #Green
            [(128,128,0,255), 3],      #Olive
            [(0,0,128,255), 4],      #Navy
            [(128,0,128,255), 5],      #Purple
            [(0,128,128,255), 6],      #Teal
            [(192,192,192,255), 7],      #Silver
            [(128,128,128,255), 8],      #Grey
            [(255,0,0,255), 9],      #Red
            [(0,255,0,255), 10],      #Lime
            [(255,255,0,255), 11],      #Yellow
            [(0,0,255,255), 12],      #Blue
            [(255,0,255,255), 13],      #Fuchsia
            [(0,255,255,255), 14],      #Aqua
            [(255,255,255,255), 15],      #White
            [(0,0,0,255), 16],      #Grey0
            [(0,0,95,255), 17],      #NavyBlue
            [(0,0,135,255), 18],      #DarkBlue
            [(0,0,175,255), 19],      #Blue3
            [(0,0,215,255), 20],      #Blue3
            [(0,0,255,255), 21],      #Blue1
            [(0,95,0,255), 22],      #DarkGreen
            [(0,95,95,255), 23],      #DeepSkyBlue4
            [(0,95,135,255), 24],      #DeepSkyBlue4
            [(0,95,175,255), 25],      #DeepSkyBlue4
            [(0,95,215,255), 26],      #DodgerBlue3
            [(0,95,255,255), 27],      #DodgerBlue2
            [(0,135,0,255), 28],      #Green4
            [(0,135,95,255), 29],      #SpringGreen4
            [(0,135,135,255), 30],      #Turquoise4
            [(0,135,175,255), 31],      #DeepSkyBlue3
            [(0,135,215,255), 32],      #DeepSkyBlue3
            [(0,135,255,255), 33],      #DodgerBlue1
            [(0,175,0,255), 34],      #Green3
            [(0,175,95,255), 35],      #SpringGreen3
            [(0,175,135,255), 36],      #DarkCyan
            [(0,175,175,255), 37],      #LightSeaGreen
            [(0,175,215,255), 38],      #DeepSkyBlue2
            [(0,175,255,255), 39],      #DeepSkyBlue1
            [(0,215,0,255), 40],      #Green3
            [(0,215,95,255), 41],      #SpringGreen3
            [(0,215,135,255), 42],      #SpringGreen2
            [(0,215,175,255), 43],      #Cyan3
            [(0,215,215,255), 44],      #DarkTurquoise
            [(0,215,255,255), 45],      #Turquoise2
            [(0,255,0,255), 46],      #Green1
            [(0,255,95,255), 47],      #SpringGreen2
            [(0,255,135,255), 48],      #SpringGreen1
            [(0,255,175,255), 49],      #MediumSpringGreen
            [(0,255,215,255), 50],      #Cyan2
            [(0,255,255,255), 51],      #Cyan1
            [(95,0,0,255), 52],      #DarkRed
            [(95,0,95,255), 53],      #DeepPink4
            [(95,0,135,255), 54],      #Purple4
            [(95,0,175,255), 55],      #Purple4
            [(95,0,215,255), 56],      #Purple3
            [(95,0,255,255), 57],      #BlueViolet
            [(95,95,0,255), 58],      #Orange4
            [(95,95,95,255), 59],      #Grey37
            [(95,95,135,255), 60],      #MediumPurple4
            [(95,95,175,255), 61],      #SlateBlue3
            [(95,95,215,255), 62],      #SlateBlue3
            [(95,95,255,255), 63],      #RoyalBlue1
            [(95,135,0,255), 64],      #Chartreuse4
            [(95,135,95,255), 65],      #DarkSeaGreen4
            [(95,135,135,255), 66],      #PaleTurquoise4
            [(95,135,175,255), 67],      #SteelBlue
            [(95,135,215,255), 68],      #SteelBlue3
            [(95,135,255,255), 69],      #CornflowerBlue
            [(95,175,0,255), 70],      #Chartreuse3
            [(95,175,95,255), 71],      #DarkSeaGreen4
            [(95,175,135,255), 72],      #CadetBlue
            [(95,175,175,255), 73],      #CadetBlue
            [(95,175,215,255), 74],      #SkyBlue3
            [(95,175,255,255), 75],      #SteelBlue1
            [(95,215,0,255), 76],      #Chartreuse3
            [(95,215,95,255), 77],      #PaleGreen3
            [(95,215,135,255), 78],      #SeaGreen3
            [(95,215,175,255), 79],      #Aquamarine3
            [(95,215,215,255), 80],      #MediumTurquoise
            [(95,215,255,255), 81],      #SteelBlue1
            [(95,255,0,255), 82],      #Chartreuse2
            [(95,255,95,255), 83],      #SeaGreen2
            [(95,255,135,255), 84],      #SeaGreen1
            [(95,255,175,255), 85],      #SeaGreen1
            [(95,255,215,255), 86],      #Aquamarine1
            [(95,255,255,255), 87],      #DarkSlateGray2
            [(135,0,0,255), 88],      #DarkRed
            [(135,0,95,255), 89],      #DeepPink4
            [(135,0,135,255), 90],      #DarkMagenta
            [(135,0,175,255), 91],      #DarkMagenta
            [(135,0,215,255), 92],      #DarkViolet
            [(135,0,255,255), 93],      #Purple
            [(135,95,0,255), 94],      #Orange4
            [(135,95,95,255), 95],      #LightPink4
            [(135,95,135,255), 96],      #Plum4
            [(135,95,175,255), 97],      #MediumPurple3
            [(135,95,215,255), 98],      #MediumPurple3
            [(135,95,255,255), 99],      #SlateBlue1
            [(135,135,0,255), 100],      #Yellow4
            [(135,135,95,255), 101],      #Wheat4
            [(135,135,135,255), 102],      #Grey53
            [(135,135,175,255), 103],      #LightSlateGrey
            [(135,135,215,255), 104],      #MediumPurple
            [(135,135,255,255), 105],      #LightSlateBlue
            [(135,175,0,255), 106],      #Yellow4
            [(135,175,95,255), 107],      #DarkOliveGreen3
            [(135,175,135,255), 108],      #DarkSeaGreen
            [(135,175,175,255), 109],      #LightSkyBlue3
            [(135,175,215,255), 110],      #LightSkyBlue3
            [(135,175,255,255), 111],      #SkyBlue2
            [(135,215,0,255), 112],      #Chartreuse2
            [(135,215,95,255), 113],      #DarkOliveGreen3
            [(135,215,135,255), 114],      #PaleGreen3
            [(135,215,175,255), 115],      #DarkSeaGreen3
            [(135,215,215,255), 116],      #DarkSlateGray3
            [(135,215,255,255), 117],      #SkyBlue1
            [(135,255,0,255), 118],      #Chartreuse1
            [(135,255,95,255), 119],      #LightGreen
            [(135,255,135,255), 120],      #LightGreen
            [(135,255,175,255), 121],      #PaleGreen1
            [(135,255,215,255), 122],      #Aquamarine1
            [(135,255,255,255), 123],      #DarkSlateGray1
            [(175,0,0,255), 124],      #Red3
            [(175,0,95,255), 125],      #DeepPink4
            [(175,0,135,255), 126],      #MediumVioletRed
            [(175,0,175,255), 127],      #Magenta3
            [(175,0,215,255), 128],      #DarkViolet
            [(175,0,255,255), 129],      #Purple
            [(175,95,0,255), 130],      #DarkOrange3
            [(175,95,95,255), 131],      #IndianRed
            [(175,95,135,255), 132],      #HotPink3
            [(175,95,175,255), 133],      #MediumOrchid3
            [(175,95,215,255), 134],      #MediumOrchid
            [(175,95,255,255), 135],      #MediumPurple2
            [(175,135,0,255), 136],      #DarkGoldenrod
            [(175,135,95,255), 137],      #LightSalmon3
            [(175,135,135,255), 138],      #RosyBrown
            [(175,135,175,255), 139],      #Grey63
            [(175,135,215,255), 140],      #MediumPurple2
            [(175,135,255,255), 141],      #MediumPurple1
            [(175,175,0,255), 142],      #Gold3
            [(175,175,95,255), 143],      #DarkKhaki
            [(175,175,135,255), 144],      #NavajoWhite3
            [(175,175,175,255), 145],      #Grey69
            [(175,175,215,255), 146],      #LightSteelBlue3
            [(175,175,255,255), 147],      #LightSteelBlue
            [(175,215,0,255), 148],      #Yellow3
            [(175,215,95,255), 149],      #DarkOliveGreen3
            [(175,215,135,255), 150],      #DarkSeaGreen3
            [(175,215,175,255), 151],      #DarkSeaGreen2
            [(175,215,215,255), 152],      #LightCyan3
            [(175,215,255,255), 153],      #LightSkyBlue1
            [(175,255,0,255), 154],      #GreenYellow
            [(175,255,95,255), 155],      #DarkOliveGreen2
            [(175,255,135,255), 156],      #PaleGreen1
            [(175,255,175,255), 157],      #DarkSeaGreen2
            [(175,255,215,255), 158],      #DarkSeaGreen1
            [(175,255,255,255), 159],      #PaleTurquoise1
            [(215,0,0,255), 160],      #Red3
            [(215,0,95,255), 161],      #DeepPink3
            [(215,0,135,255), 162],      #DeepPink3
            [(215,0,175,255), 163],      #Magenta3
            [(215,0,215,255), 164],      #Magenta3
            [(215,0,255,255), 165],      #Magenta2
            [(215,95,0,255), 166],      #DarkOrange3
            [(215,95,95,255), 167],      #IndianRed
            [(215,95,135,255), 168],      #HotPink3
            [(215,95,175,255), 169],      #HotPink2
            [(215,95,215,255), 170],      #Orchid
            [(215,95,255,255), 171],      #MediumOrchid1
            [(215,135,0,255), 172],      #Orange3
            [(215,135,95,255), 173],      #LightSalmon3
            [(215,135,135,255), 174],      #LightPink3
            [(215,135,175,255), 175],      #Pink3
            [(215,135,215,255), 176],      #Plum3
            [(215,135,255,255), 177],      #Violet
            [(215,175,0,255), 178],      #Gold3
            [(215,175,95,255), 179],      #LightGoldenrod3
            [(215,175,135,255), 180],      #Tan
            [(215,175,175,255), 181],      #MistyRose3
            [(215,175,215,255), 182],      #Thistle3
            [(215,175,255,255), 183],      #Plum2
            [(215,215,0,255), 184],      #Yellow3
            [(215,215,95,255), 185],      #Khaki3
            [(215,215,135,255), 186],      #LightGoldenrod2
            [(215,215,175,255), 187],      #LightYellow3
            [(215,215,215,255), 188],      #Grey84
            [(215,215,255,255), 189],      #LightSteelBlue1
            [(215,255,0,255), 190],      #Yellow2
            [(215,255,95,255), 191],      #DarkOliveGreen1
            [(215,255,135,255), 192],      #DarkOliveGreen1
            [(215,255,175,255), 193],      #DarkSeaGreen1
            [(215,255,215,255), 194],      #Honeydew2
            [(215,255,255,255), 195],      #LightCyan1
            [(255,0,0,255), 196],      #Red1
            [(255,0,95,255), 197],      #DeepPink2
            [(255,0,135,255), 198],      #DeepPink1
            [(255,0,175,255), 199],      #DeepPink1
            [(255,0,215,255), 200],      #Magenta2
            [(255,0,255,255), 201],      #Magenta1
            [(255,95,0,255), 202],      #OrangeRed1
            [(255,95,95,255), 203],      #IndianRed1
            [(255,95,135,255), 204],      #IndianRed1
            [(255,95,175,255), 205],      #HotPink
            [(255,95,215,255), 206],      #HotPink
            [(255,95,255,255), 207],      #MediumOrchid1
            [(255,135,0,255), 208],      #DarkOrange
            [(255,135,95,255), 209],      #Salmon1
            [(255,135,135,255), 210],      #LightCoral
            [(255,135,175,255), 211],      #PaleVioletRed1
            [(255,135,215,255), 212],      #Orchid2
            [(255,135,255,255), 213],      #Orchid1
            [(255,175,0,255), 214],      #Orange1
            [(255,175,95,255), 215],      #SandyBrown
            [(255,175,135,255), 216],      #LightSalmon1
            [(255,175,175,255), 217],      #LightPink1
            [(255,175,215,255), 218],      #Pink1
            [(255,175,255,255), 219],      #Plum1
            [(255,215,0,255), 220],      #Gold1
            [(255,215,95,255), 221],      #LightGoldenrod2
            [(255,215,135,255), 222],      #LightGoldenrod2
            [(255,215,175,255), 223],      #NavajoWhite1
            [(255,215,215,255), 224],      #MistyRose1
            [(255,215,255,255), 225],      #Thistle1
            [(255,255,0,255), 226],      #Yellow1
            [(255,255,95,255), 227],      #LightGoldenrod1
            [(255,255,135,255), 228],      #Khaki1
            [(255,255,175,255), 229],      #Wheat1
            [(255,255,215,255), 230],      #Cornsilk1
            [(255,255,255,255), 231],      #Grey10
            [(8,8,8,255), 232],      #Grey3
            [(18,18,18,255), 233],      #Grey7
            [(28,28,28,255), 234],      #Grey11
            [(38,38,38,255), 235],      #Grey15
            [(48,48,48,255), 236],      #Grey19
            [(58,58,58,255), 237],      #Grey23
            [(68,68,68,255), 238],      #Grey27
            [(78,78,78,255), 239],      #Grey30
            [(88,88,88,255), 240],      #Grey35
            [(98,98,98,255), 241],      #Grey39
            [(108,108,108,255), 242],      #Grey42
            [(118,118,118,255), 243],      #Grey46
            [(128,128,128,255), 244],      #Grey50
            [(138,138,138,255), 245],      #Grey54
            [(148,148,148,255), 246],      #Grey58
            [(158,158,158,255), 247],      #Grey62
            [(168,168,168,255), 248],      #Grey66
            [(178,178,178,255), 249],      #Grey70
            [(188,188,188,255), 250],      #Grey74
            [(198,198,198,255), 251],      #Grey78
            [(208,208,208,255), 252],      #Grey82
            [(218,218,218,255), 253],      #Grey85
            [(228,228,228,255), 254],      #Grey89
            [(238,238,238,255), 255],      #Grey93
        ]
        if rgb[3] == 0:
            return None

        for color in colors:
            if color[0] == rgb:
                code = color[1]
                break
            else:
                code = colors[2][1]
                
        return str(code)

    def write2file(self):
        esc="\033"
        rst = esc+"[0;00m" 

        def add_escapes(color_f, bf):
            fgr="[38;5;" #for foreground color
            bgr="[48;5;" #for background color
    
            if color_f==None:
                return "" #error blyat

            if bf == 0:
                color = esc+bgr+str(color_f)+"m"
            else:
                color = esc+fgr+str(color_f)+"m"
            return color

        script = open(script_name, "w", encoding='utf-8', newline='')

        for row in self.image_list:
            row_r = ""
            for symb in row:
                if symb[0]==symb[1] and symb[0][3]!=0:
                    row_r += add_escapes(self.trans_col(symb[0]), 1) + "█" + rst
                elif symb[1][3]==0 and symb[0][3]!=0:
                    row_r += add_escapes(self.trans_col(symb[0]), 1) + "▀" + rst
                elif symb[0]==0:
                    row_r += rst
                elif symb[0][3]==0 and symb[1][3]!=0:
                    row_r += (
                        add_escapes(self.trans_col(symb[0]), 0) + 
                        add_escapes(self.trans_col(symb[1]), 1) + "▄" + rst
                        )
                elif symb[0][3]!=0 and symb[1][3]!=0:
                    row_r += (
                        add_escapes(self.trans_col(symb[0]), 0) + 
                        add_escapes(self.trans_col(symb[1]), 1) + "▄" + rst
                        )
                else:
                    row_r +=" "
            script.write(row_r+"\n")
        script.close()
        print("#Writen to file \""+script_name+"\"")

####################


lol = pixel2ANSI(image_name)
