import Tkinter as tk
from Tkinter import *

from PIL import Image,ImageTk

import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
  
 
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    
LARGE_FONT = ("Verdana", 12)

gg=1
cc= "ggg"
class upphaf(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
       # print('bt 1')

        for F in (StartPage, PageOne, PageTwo):
            #print('f')
            #print(F)
            
            frame = F(container, self)
            #print('flettari 2')
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(StartPage)
        
        #print('eftir flettara3')
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
                           command=lambda: controller.show_frame(PageOne))
        button.place(x=20, y=80)

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.place(x=20, y=50)
        
        GPIO.add_event_detect(13, GPIO.FALLING, callback=my_callback, bouncetime=300)
        GPIO.add_event_detect(16, GPIO.FALLING, callback=my_callback2, bouncetime=300)
        GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback3, bouncetime=300)
        GPIO.add_event_detect(18, GPIO.FALLING, callback=my_callback4, bouncetime=300)
        GPIO.add_event_detect(24, GPIO.FALLING, callback=coin_callback, bouncetime=300)

    
       

        rvk = Image.open( '/home/pi/Videos/youtube/rvk.jpeg' )
        rvkrender = ImageTk.PhotoImage( rvk )
        img4 = tk.Label( self, image=rvkrender )
        img4.image = rvkrender
        img4.place(x=400, y=10)

    



class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        #print('sida 1  ')
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        
        tungumal = Image.open( '/home/pi/Videos/youtube/tungumal.jpg')
        tungumal = tungumal.resize((1185,560), Image.ANTIALIAS)
        tungrender= ImageTk.PhotoImage( tungumal )
        imgtung = tk.Label( self, image=tungrender )
        imgtung.image = tungrender
        imgtung.place(x=0, y=0)

      

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Frame = Frame(width=768, height=576, bg="black", colormap="new")
        #print('sida2 7')
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

        val = Image.open( '/home/pi/Videos/youtube/valkostir.jpg')
        val = val.resize((1185,560), Image.ANTIALIAS)
        valrender= ImageTk.PhotoImage( val )
        imgval = tk.Label( self, image=valrender )
        imgval.image = valrender
        imgval.place(x=0, y=0)


def gunnar(ggg):
    if ggg == 1:
        app.show_frame(PageOne)
        global gg
        gg=2
    elif ggg==2:
        app.show_frame(PageTwo)
        global gg
        gg=3
    elif ggg==3:
        app.show_frame(StartPage)
        global gg
        gg=1  
    

def my_callback(channel):  
    print "falling edge detected on 13"
    print(gg)   
    gunnar(gg)
    print (cc)

def my_callback2(channel):
    print "falling edge detected on 16"
    gunnar(gg)
    print (cc)
def my_callback3(channel):
    gunnar(gg)
    print"falling edge detected on 23"
    print (cc)

def my_callback4(channel):  
    print "falling edge detected on 18"        
    gunnar(gg)


def coin_callback(channel):  
    print "coin"


if __name__ == "__main__":
    app = upphaf()
    app.geometry("2200x700")
    app.mainloop()

