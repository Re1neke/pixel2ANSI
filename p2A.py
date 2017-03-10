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
            [(0,0,0,255), 0],         #Black
            [(128,0,0,255), 1],       #Maroon
            [(0,128,0,255), 2],       #Green
            [(128,128,0,255), 3],     #Olive
            [(0,0,128,255), 4],       #Navy
            [(128,0,128,255), 5],     #Purple
            [(0,128,128,255), 6],     #Teal
            [(192,192,192,255), 7],   #Silver
            [(128,128,128,255), 8],   #Grey
            [(255,0,0,255), 9],       #Red
            [(0,255,0,255), 10],      #Lime
            [(255,255,0,255), 11],    #Yellow
            [(0,0,255,255), 12],      #Blue
            [(255,0,255,255), 13],    #Fuchia
            [(0,255,255,255), 14],    #Aqua
            [(255,255,255,255), 15],  #White
        ]
        if rgb == (0,0,0,0):
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
                if symb[0]==symb[1] and symb[0]!=(0,0,0,0):
                    row_r += add_escapes(self.trans_col(symb[0]), 1) + "█" + rst
                elif symb[1]==(0,0,0,0) and symb[0]!=(0,0,0,0):
                    row_r += add_escapes(self.trans_col(symb[0]), 1) + "▀" + rst
                elif symb[0]==0:
                    row_r += rst
                elif symb[0]==(0,0,0,0) and symb[1]!=(0,0,0,0):
                    row_r += (
                        add_escapes(self.trans_col(symb[0]), 0) + 
                        add_escapes(self.trans_col(symb[1]), 1) + "▄" + rst
                        )
                elif symb[0]!=(0,0,0,0) and symb[1]!=(0,0,0,0):
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
