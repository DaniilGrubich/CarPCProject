import cloudscraper
from PIL import Image
import io
import math

def circleCoords(x, y, r):
    return x-r, y-r, x+r, y+r


def mmap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class roundGauge:
    xc = 0
    yc = 0
    r = 0
    R = 0

    As = 0
    Ae = 0

    range = []
    lastVal = 0
    lastAng = 0

    color = ''

    knobR = 10
    nDivisions = 0
    divisionColors = []

    name = ''
    font = ''

    id = 0
    niddleId = ''
    txtId = ''

    def __init__(self,name, id, font, xc, yc, r, R, As, Ae, range, color, nDivisions, divisionColors):
        self.xc = xc
        self.yc = yc
        self.r = r
        self.R = R
        self.As = As
        self.Ae = Ae
        self.range = range

        self.lastAng = Ae
        self.color = color
        self.nDivisions = nDivisions
        self.divisionColors = divisionColors

        self.name = name
        self.font = font

        if(id == 0):
            self.niddleId = 'nid0'
            self.txtId = 'txt0'
        elif(id == 1):
            self.niddleId = 'nid1'
            self.txtId = 'txt1'
        elif(id == 2):
            self.niddleId = 'nid2'
            self.txtId = 'txt2'
        elif (id == 3):
            self.niddleId = 'nid3'
            self.txtId = 'txt3'


    def set(self, val, canvas):
        tkcanvas = canvas.tk_canvas

        frac = mmap(val, self.range[0], self.range[1], 0, 1)
        if(frac < 0):
            frac = 0
        elif frac > 1:
            frac = 1

        # tkcanvas.create_line(self.xc, self.yc, self.r * math.cos(math.radians(self.lastAng)) + self.xc, self.r * math.sin(math.radians(self.lastAng)) + self.yc, fill='black')
        # newAngle = self.Ae - (self.Ae - self.As) * frac

        # lastPoligonPoints = ((self.r-2) * math.cos(math.radians(self.lastAng)) + self.xc, (self.r-2) * math.sin(math.radians(self.lastAng)) + self.yc,
        #                  (self.knobR) * math.cos(math.radians(self.lastAng+90)) + self.xc, self.knobR * math.sin(math.radians(self.lastAng+90)) + self.yc,
        #                  (self.knobR + 10) * math.cos(math.radians(self.lastAng+180)) + self.xc, (self.knobR + 10) * math.sin(math.radians(self.lastAng+180)) + self.yc,
        #                  self.knobR * math.cos(math.radians(self.lastAng+270)) + self.xc, self.knobR * math.sin(math.radians(self.lastAng+270)) + self.yc)
        #
        # tkcanvas.create_polygon(lastPoligonPoints, fill='black')

        newAngle = self.As + (self.Ae - self.As) * frac


        newPoligonPoints = ((self.r - 2) * math.cos(math.radians(newAngle)) + self.xc,
                             (self.r - 2) * math.sin(math.radians(newAngle)) + self.yc,
                             (self.knobR) * math.cos(math.radians(newAngle + 90)) + self.xc,
                             self.knobR * math.sin(math.radians(newAngle + 90)) + self.yc,
                             (self.knobR + 10) * math.cos(math.radians(newAngle + 180)) + self.xc,
                             (self.knobR + 10) * math.sin(math.radians(newAngle + 180)) + self.yc,
                             self.knobR * math.cos(math.radians(newAngle + 270)) + self.xc,
                             self.knobR * math.sin(math.radians(newAngle + 270)) + self.yc)

        tkcanvas.delete(self.niddleId)
        tkcanvas.create_polygon(newPoligonPoints, fill=self.color, tag=self.niddleId)

        tkcanvas.delete(self.txtId)
        tkcanvas.create_text(self.xc, self.yc + self.r - 25, text="{:.2f}".format(val), justify='center', font=self.font, fill='white',tag=self.txtId)

        # lastFrac = mmap(self.lastVal, self.range[0], self.range[1], 0, 1)
        # changeFillFrac = frac - lastFrac
        #
        #
        # # (self.Ae - self.As) * changeFillFrac/
        # if(changeFillFrac > 0):
        #     tkcanvas.create_arc(circleCoords(self.xc, self.yc, (self.R+self.r)/2), start=self.lastAng, extent = -(self.Ae - self.As) * changeFillFrac, outline=self.color, width=self.R-self.r-2, style='arc')
        # elif(changeFillFrac < 0):
        #     tkcanvas.create_arc(circleCoords(self.xc, self.yc, (self.R+self.r)/2), start=self.lastAng, extent = -(self.Ae - self.As) * changeFillFrac, outline='white', width=self.R-self.r-2, style='arc')
        #
        # self.lastAng = self.lastAng - (self.Ae - self.As) * changeFillFrac
        # print((self.Ae - self.As) * changeFillFrac)
        #
        #
        # self.lastVal = val
        # print(self.lastAng)

        self.lastAng = newAngle

    def drawOutline(self, canvas):
        tkcanvas = canvas.tk_canvas

        oulineColor = 'gray'
        outlineWidth = 3

        #######################################---GENERAL OUTLINE---############################################
        tkcanvas.create_arc(circleCoords(self.xc, self.yc, self.R), start=-self.As, extent=-(self.Ae - self.As), outline=oulineColor, style='arc', width=outlineWidth)
        tkcanvas.create_arc(circleCoords(self.xc, self.yc, self.r), start=-self.As, extent=-(self.Ae - self.As), outline=oulineColor, style='arc', width=outlineWidth)

        #######################################---DIVISIONS---############################################

        step = (self.Ae - self.As)/self.nDivisions
        for i in range(0, self.nDivisions+1):
            a = step * i + self.As

            if(i < self.nDivisions):
                tkcanvas.create_arc(circleCoords(self.xc, self.yc, (self.r+self.R)/2),  start=-a, extent=-step, width= (self.R-self.r)-1,outline=self.divisionColors[i], style='arc')

            points = (self.r * math.cos(math.radians(a)) + self.xc,
                      self.r * math.sin(math.radians(a)) + self.yc,
                      self.R * math.cos(math.radians(a)) + self.xc,
                      self.R * math.sin(math.radians(a)) + self.yc)

            tkcanvas.create_line(points, fill=oulineColor, width=outlineWidth)

        #######################################---LABEL---############################################
        tkcanvas.create_text(self.xc, self.yc+self.r - 25, text = 'XX', justify='center', font = self.font, fill='white', tag=self.txtId)
        tkcanvas.create_text(self.xc, self.yc+self.r, text = self.name, justify='center', font = self.font, fill='white')


        #######################################---NIDDLE---############################################
        newPoligonPoints = ((self.r - 2) * math.cos(math.radians(self.As)) + self.xc,
                             (self.r - 2) * math.sin(math.radians(self.As)) + self.yc,
                             (self.knobR) * math.cos(math.radians(self.As + 90)) + self.xc,
                             self.knobR * math.sin(math.radians(self.As + 90)) + self.yc,
                             (self.knobR + 10) * math.cos(math.radians(self.As + 180)) + self.xc,
                             (self.knobR + 10) * math.sin(math.radians(self.As + 180)) + self.yc,
                             self.knobR * math.cos(math.radians(self.As + 270)) + self.xc,
                             self.knobR * math.sin(math.radians(self.As + 270)) + self.yc)

        tkcanvas.create_polygon(newPoligonPoints, fill=self.color, tag=self.niddleId)


def getImagefromURL(url):
    if(url != ""):
        jpg_data = (
            cloudscraper.create_scraper(
                browser={"browser": "firefox", "platform": "windows", "mobile": False}
            )
                .get(url)
                .content
        )

        image = Image.open(io.BytesIO(jpg_data))
        print(image)
        return image
    else:
         return ""



