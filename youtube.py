import Tkinter as tk
from Tkinter import *
import os

from PIL import Image,ImageTk

import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
  
 
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    
LARGE_FONT = ("Verdana", 12)

gg=1
cc= "ggg"
coin=0
lang="none"
nrplay=0

class upphaf(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
       # print('bt 1')

        for F in (StartPage, PageLang, Pageuk, PageGermany, PageFrance, PageFrance, Pageplay, PageChina, PageCoin):
            frame = F(container, self)
            #print('flettari 2')
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        print(cont)
        global cc
        cc= cont
        #print(cont)
        frame = self.frames[cont]
        #print(frame)
        frame.tkraise()
        #print('synir ramma 4')


    

    
            
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        #print('start page 5')
        button = tk.Button(self, text="Visit Page 1",
                           command=lambda: controller.show_frame(PageLang))
        button.place(x=20, y=80)

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(Pageuk))
        button2.place(x=20, y=50)
        
        GPIO.add_event_detect(5, GPIO.FALLING, callback=my_callback, bouncetime=300)
        GPIO.add_event_detect(6, GPIO.FALLING, callback=my_callback2, bouncetime=300)
        GPIO.add_event_detect(13, GPIO.FALLING, callback=my_callback3, bouncetime=300)
        GPIO.add_event_detect(19, GPIO.FALLING, callback=my_callback4, bouncetime=300)
        GPIO.add_event_detect(21, GPIO.FALLING, callback=coin_callback, bouncetime=300)

    
       

        tungumal = Image.open( '/home/pi/Videos/youtube/startpage.jpg')
        tungumal = tungumal.resize((1195,560), Image.ANTIALIAS)
        tungrender= ImageTk.PhotoImage( tungumal )
        imgtung = tk.Label( self, image=tungrender )
        imgtung.image = tungrender
        imgtung.place(x=0, y=0)

    



class PageLang(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
      
        tungumal = Image.open( '/home/pi/Videos/youtube/tungumal.jpg')
        tungumal = tungumal.resize((1195,560), Image.ANTIALIAS)
        tungrender= ImageTk.PhotoImage( tungumal )
        imgtung = tk.Label( self, image=tungrender )
        imgtung.image = tungrender
        imgtung.place(x=0, y=0)

      

class Pageuk(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       

        val = Image.open( '/home/pi/Videos/youtube/valkostir.jpg')
        val = val.resize((1195,560), Image.ANTIALIAS)
        valrender= ImageTk.PhotoImage( val )
        imgval = tk.Label( self, image=valrender )
        imgval.image = valrender
        imgval.place(x=0, y=0)
        
class PageGermany(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       

        val = Image.open( '/home/pi/Videos/youtube/valgerm.jpg')
        val = val.resize((1195,560), Image.ANTIALIAS)
        valrender= ImageTk.PhotoImage( val )
        imgval = tk.Label( self, image=valrender )
        imgval.image = valrender
        imgval.place(x=0, y=0)

class PageFrance(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       

        val = Image.open( '/home/pi/Videos/youtube/valfran.jpg')
        val = val.resize((1195,560), Image.ANTIALIAS)
        valrender= ImageTk.PhotoImage( val )
        imgval = tk.Label( self, image=valrender )
        imgval.image = valrender
        imgval.place(x=0, y=0)

class PageChina(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       

        val = Image.open( '/home/pi/Videos/youtube/valchi.jpg')
        val = val.resize((1195,560), Image.ANTIALIAS)
        valrender= ImageTk.PhotoImage( val )
        imgval = tk.Label( self, image=valrender )
        imgval.image = valrender
        imgval.place(x=0, y=0)

class PageCoin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       

        val = Image.open( '/home/pi/Videos/youtube/coin.jpg')
        val = val.resize((1195,560), Image.ANTIALIAS)
        valrender= ImageTk.PhotoImage( val )
        imgval = tk.Label( self, image=valrender )
        imgval.image = valrender
        imgval.place(x=0, y=0)

class Pageplay(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       

        val = Image.open( '/home/pi/Videos/youtube/play.jpg')
        val = val.resize((1195,560), Image.ANTIALIAS)
        valrender= ImageTk.PhotoImage( val )
        imgval = tk.Label( self, image=valrender )
        imgval.image = valrender
        imgval.place(x=0, y=0)        

def gunnar(ggg):
    if ggg == 1:
        app.show_frame(PageLang)
        global gg
        gg=2
    print(lang)
    if ggg == 2:
        gg=3
        print(lang)
        if lang=="eng":
            print(lang)
            app.show_frame(Pageuk)
            global gg
            
        elif lang=="ger":
            print(lang)
            app.show_frame(PageGermany)
            global gg
            
        elif lang=="fra":
            print(lang)
            app.show_frame(PageFrance)
            global lang    
            
        elif lang=="chi":
            print(lang)
            app.show_frame(PageChina)
            global gg
            
    elif ggg==3:
        app.show_frame(PageCoin)
        global gg
        gg=4
        
    elif ggg == 4 and coin == True:
        app.show_frame(Pageplay)
        global gg
        global coin
        global lang
        coin = False
        gg=5
        
        if nrplay == 1:
            os.system("omxplayer /home/pi/Videos/youtube/video/althing.avi")
                
        elif nrplay ==2:
            os.system("omxplayer /home/pi/Videos/youtube/video/dom.avi")
                
        elif nrplay ==3:
            os.system("omxplayer /home/pi/Videos/youtube/video/jon.avi")
                
        elif nrplay ==4:
            os.system("omxplayer /home/pi/Videos/youtube/video/austur.avi")
          
        lang = "none"
        

    elif ggg==5:
        app.show_frame(StartPage)
        global gg
        gg=1



def my_callback(channel):  
    print "falling edge detected on 5"
    print(lang)   
    print (gg)
    if gg == 2:
        global lang
        lang="eng"
    elif gg==3:
        global nrplay
        nrplay=1
    gunnar(gg)

def my_callback2(channel):
    print "falling edge detected on 6"
    print (cc)
    if gg== 2:
        global lang
        lang="ger"
    elif gg==3:
        global nrplay
        nrplay=2
    gunnar(gg)
        
def my_callback3(channel):
    print"falling edge detected on 13"
    print (cc)
    if gg==2:
        global lang
        lang="fra"
    elif gg==3:
        global nrplay
        nrplay=3
    gunnar(gg)

def my_callback4(channel):  
    print "falling edge detected on 19"        
    if gg==2:
        global lang
        lang="chi"
    elif gg==3:
        global nrplay
        nrplay=4
        
    gunnar(gg)

def coin_callback(channel):  
    print "coin"
    global coin
    coin=True


if __name__ == "__main__":
    app = upphaf()
    app.geometry("2200x700")
    app.mainloop()

