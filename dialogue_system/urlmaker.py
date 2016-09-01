import urllib.request
import json
import numpy
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

hostip = ""
jsonData = json.load(open('item_list.json', 'r',encoding = "utf-8"))

def draw_text_at_center(string1,string2):
    text = string1
    temp = len(text)
    if temp > 15:
       text2 = text[0:15]+"\n"+text[15:len(text)]
    text2 += "\n価格: " + string2 + "円"
    img = PIL.Image.new("RGBA", (600, 200))
    draw = PIL.ImageDraw.Draw(img)
    draw.font = PIL.ImageFont.truetype("ipamjm.ttf", 40)
    img_size = numpy.array(img.size)
    txt_size = numpy.array(draw.font.getsize(text2))
    #pos = (img_size - txt_size) /2
    pos = img_size - img_size
    draw.text(pos, text2, (255, 255, 255))
    
    img.save("/home/ubuntu/robotablet/static/uploads/image2/default.png","PNG",optimize = True)

def urlmaker(string1,string2):
    ini_url = "http://"+hostip+"/q?action=show_image2"
    image1 ="&image1=" + string1
    image2 ="&image2=" + string2
    return urllib.request.urlopen(ini_url + image1 + image2)


def recommender(string1,string2):
    ini_url = "http://"+hostip+"/q?action=show_image2"
    image1 ="&image1=" + string1
    image2 ="&image2="+"default.png"
    draw_text_at_center(string2)
    return urllib.request.urlopen(ini_url + image1 + image2)

