import screen_ocr
import pyvista

def to_pixel_coordinates(x,y):
    return x*2560+y

ocr_reader = screen_ocr.Reader.create_fast_reader()
ocr_reader.BoundingBox = (to_pixel_coordinates(0,1362),to_pixel_coordinates(0,1401),to_pixel_coordinates(2560,1362),to_pixel_coordinates(2560,1401))
def sanitize_pos(stri: str):
    #print(stri)
    stri.strip()
    #print(stri)
    split = stri.find("km")
    stri = stri[split+2:split+24]
    #print(stri)
    try:
        N = [int(stri[0:3]),int(stri[3:6]),int(stri[7:9])]
        E = [int(stri[12:14]),int(stri[15:17]),int(stri[18:20])]
    except:
        return (0,0)
    #print(N)
    #print(E)
    x = N[0]+N[1]/60+N[2]/60/60
    #print(x)
    y = E[0]+E[1]/60+E[2]/60/60
    #print(y)
    return (x,y)

def sanitize_date(stri:str):
    #print(stri)
    key = stri.find("Datenzuordnung")
    stri = stri[key+len("Datenzuordnung"):-1]
    #print(stri)
    split = stri.split("\n")
    #print(split)
    try:
        return int(split[0][-2]+split[0][-1])
    except:
        return 0

#while True:
while True:
    lastx = 0
    lasty = 0
    lastdate =0
    coords = ocr_reader.read_nearby((2400,1340))
    date = ocr_reader.read_nearby((1600,1380))
    (x,y) = sanitize_pos(coords.as_string())
    date = sanitize_date(date.as_string())
    if x!=0 and y!= 0 and date != 0 and lastx != x and lasty !=y and lastdate!=date:
        print("[",x,",",y,",",float(date),"],")
        lastx = x
        lasty = y
        lastdate = date

