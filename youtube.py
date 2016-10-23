import Tkinter as tk
from Tkinter import *

from PIL import Image,ImageTk

import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
  
 
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    
LARGE_FONT = ("Verdana", 12)

gg=1

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
        
        rvk2 = Image.open( '/home/pi/Videos/youtube/Germany.gif' )
        rvkrender4 = ImageTk.PhotoImage( rvk2 )
        img4 = tk.Label( self, image=rvkrender4 )
        img4.image = rvkrender4
        img4.place(x=400, y=10)

        
        '''
        china = Image.open( 'home/pi/Videos/youtube/china.gif' )
        chinar = ImageTk.PhotoImage( china )
        img = tk.Label( self, image=chinar )
        img.image = chinar
        img.place(x=1100, y=600)

        uk = Image.open('home/pi/Videos/youtube/uk.gif')
        ukrend = ImageTk.PhotoImage(uk)
        img1 = tk.Label(self, image=ukrend)
        img1.image = ukrend
        img1.place(x=200, y=600)

        germany = Image.open('home/pi/Videos/youtube/germany.gif')
        germanrender = ImageTk.PhotoImage(germany)
        img2 = tk.Label(self, image=germanrender)
        img2.image = germanrender
        img2.place(x=500, y=600)

        france = Image.open('home/pi/Videos/youtube/France.gif')
        frender = ImageTk.PhotoImage(france)
        img3 = tk.Label(self, image=frender)
        img3.image = frender
        img3.place(x=800, y=600)
'''
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

        rvk1 = Image.open( '/home/pi/Videos/youtube/uk.gif' )
        rvkrender2 = ImageTk.PhotoImage( rvk1 )
        img4 = tk.Label( self, image=rvkrender2 )
        img4.image = rvkrender2
        img4.place(x=400, y=10)


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

def my_callback2(channel):
    print "falling edge detected on 16"
    gunnar(gg)
def my_callback3(channel):
    gunnar(gg)
    print"falling edge detected on 23"
    

def my_callback4(channel):  
    print "falling edge detected on 18"        
    gunnar(gg)




if __name__ == "__main__":
    app = upphaf()
    app.geometry("2200x700")
    app.mainloop()

