from tkinter import *
from tkinter import ttk
from threading import Thread
import tkinter
from tkinter import font
import random
from PIL import Image, ImageTk
from sys import exit
from fontTools.ttLib import TTFont

class UserInterface:

    def __init__(self):
        self.initialDraw = True

        thread = Thread(target=self.GuiThread)
        thread.start()


    def GuiThread(self):
        self.gui = Tk()

        self.gui.geometry('%dx%d' % (450, 450))
        self.gui.maxsize(450, 450)
        self.gui.title('THE GUI-INATOR')
        self.gui.iconbitmap("Doofenshmirtz.ico")
        self.notebook = ttk.Notebook(self.gui)
        self.current = ()
        font_sunshine = TTFont('a-little-sunshine/sunshine.ttf')

        self.affirmationPage = ttk.Frame(self.notebook)
        self.randomReason = ttk.Frame(self.notebook)
        self.dateIdea = ttk.Frame(self.notebook)
        self.randomPic = ttk.Frame(self.notebook)
        self.reassuranceQuote = ttk.Frame(self.notebook)

        self.notebook.add(self.affirmationPage, text='Affirmations Loop')
        self.notebook.add(self.randomReason, text='Random Reason')
        self.notebook.add(self.dateIdea, text='Date Idea')
        self.notebook.add(self.randomPic, text='Random Pic')
        self.notebook.add(self.reassuranceQuote, text='Reassurance Quote')

        
        self.notebook.pack(expand=1, fill='both')
        self.Refresh()
        self.gui.protocol('WM_DELETE_WINDOW', self.OnExit)

        self.gui.mainloop()
        

    def Refresh(self):
        self.drawAffirmation()
        self.drawRandReason()
        self.drawDateIdea()
        self.drawRandomPic()
        self.drawReassuranceQuote()
        self.initialDraw = False

    def reDrawRandPic(self):
        self.initialDraw = False
        self.drawRandomPic()
        


### ***FIRST FUNCTION HERE***
    def drawAffirmation(self):
        if self.initialDraw:
            # global aff_counter
            # aff_counter = 1
            font_sunshine = TTFont('a-little-sunshine/sunshine.ttf')

            global _num_counter
            _num_counter = tkinter.IntVar()

            _label = Label(self.affirmationPage, text="Affirmations!")
            _label.config(font =(font_sunshine, 14))
            _label.place(relx=0.5, rely=0.13, anchor='s')

            _label_text = tkinter.Label(self.affirmationPage, text="test")
            _label_text.config(font=(font_sunshine, 20))
            _label_text.place(relx=0.48, rely=0.25, anchor='n')

            _label_counter = tkinter.Label(self.affirmationPage, textvariable=_num_counter)
            _label_counter.config(font=(font_sunshine, 20))
            _label_counter.place(relx=0.665, rely=0.25, anchor='n')

            _button_1 = Button(self.affirmationPage, text="Click me", command= lambda gui = self.affirmationPage: self.loop(gui))
            _button_1.pack(side=BOTTOM, padx=15, pady=150)
            _button_1.config(pady=10)

            _button_2 = Button(self.affirmationPage, text="Reset so you can start again", command=lambda gui = self.gui: self.clearFrame(gui))
            _button_2.place(relx=0.5, rely=0.80, anchor='n')
            _button_2.config(pady=10)
        
    def loop(self, gui):
        _num_counter.set(_num_counter.get() + 1)
        self.affirmationPage.update()

    def clearFrame(self, gui):
        _num_counter.set(1)  

### *** REASON FUNCTION STARTS HERE ***
    def drawRandReason(self):
        if self.initialDraw:
            global _reason_label
            _reason_label = tkinter.StringVar()

            _label = Label(self.randomReason, text="Random Reason")
            _label.config(font =("Courier", 14))

            _output_reason = tkinter.Label(self.randomReason, textvariable=_reason_label)
            _output_reason.config(font=("courier", 20))
            _output_reason.place(relx=0.50, rely=0.15, anchor='n')

            _button_1 = Button(self.randomReason, text="Random", command=lambda gui = self.randomReason: self.randReason(gui))
            _button_1.pack(side=BOTTOM, padx=15, pady=150)
            _button_1.config(pady=10)

            _button_2 = Button(self.randomReason, text="RESET SCREEN", command=lambda gui = self.randomReason: self.clearRandReason(gui))
            _button_2.place(relx=0.5, rely=0.80, anchor='n')
            _button_2.config(pady=10)

            _label.place(relx=0.5, rely=0.13, anchor='s')

    def randReason(self, gui):
        _list_reasons = ['']

        reason_lst = len(_list_reasons)-1
        rand = random.randint(0, reason_lst)#random.choice(_list_reasons)
        _reason_label.set(_list_reasons[rand])
        self.randomReason.update()

    def clearRandReason(self, gui):
        _reason_label.set('')

### *** DATE FUNCTION STARTS HERE ***
    def drawDateIdea(self):
        if self.initialDraw:
            global _date_label
            _date_label = tkinter.StringVar()

            _label = Label(self.dateIdea, text="DATE IDEAS!!!")
            _label.config(font =("Courier", 14))

            _output_date = tkinter.Label(self.dateIdea, textvariable=_date_label)
            _output_date.config(font=("courier", 20))
            _output_date.place(relx=0.50, rely=0.25, anchor='n')

            _button_1 = Button(self.dateIdea, text="Conjure Up A Date", command=lambda gui = self.gui: self.randDate(gui))
            _button_1.pack(side=BOTTOM, padx=15, pady=150)
            _button_1.config(pady=10)

            _button_2 = Button(self.dateIdea, text="Don't Like It? Try Again", command=lambda gui = self.gui: self.clearDateIdea(gui))
            _button_2.place(relx=0.5, rely=0.80, anchor='n')
            _button_2.config(pady=10)

            _label.place(relx=0.5, rely=0.13, anchor='s')

    def randDate(self, gui):
        _list_dates = ['Netflix & Fort Date',
                       'Walk in the Park', 
                       'Bike Ride', 
                       'Bookstore Date', 
                       'Iceskating/Rollerskating',
                       'Movie Marathon',
                       'Art Museum',
                       'Science Museum',
                       'Arcade Date',
                       'Game & Wine Night',
                       'Zoo/Aquarium',
                       'Laser Tag',
                       'Dancing',
                       'Amusement Park',
                       'Wine & Paint',
                       'Picnic',
                       'Kayaking',
                       'Rock Climbing',
                       'Pottery Class',
                       'Art Class',
                       "Fancy Date Night (Dress Up)",
                       'Dog Park',
                       'Drive Thru Movies',
                       'Cooking Night',
                       'Thrift Store',
                       'Plant Nursery',
                       'Brunch',
                       'Food Truck Date',
                       'Goat Yoga',
                       'Watch Airplanes',
                       'Watch Sunset',
                       'Karaoke Night',
                       'Go karts',
                       'Sports']

        _date_len = len(_list_dates)-1

        rand = random.randint(0, _date_len)#random.choice(_list_reasons)
        _date_label.set(_list_dates[rand])

    def clearDateIdea(self, gui):
        _date_label.set('')

### *** PIC FUNCTION STARTS HERE ***
    def drawRandomPic(self):
        if self.initialDraw:
            #_img = ImageTk.PhotoImage(Image.open("Photos/pics_1.jpg"))
            global _pic_selector
            global _img_size
            _pic_selector = self.randNumGen(self.gui)
            _img_path = "Photos/pics_" + str(_pic_selector) + ".jpg"#_img_generator
            _img = Image.open(_img_path)

            _label = Label(self.randomPic, text="SOME OF MY FAV PICS")
            _label.config(font =("Courier", 14))
            _label.place(relx=0.5, rely=0.13, anchor='s')

            ### TEST CODE 1
            global _bar 
            _bar = Frame(self.randomPic, relief=RIDGE, borderwidth=5)
            _bar.pack(side=BOTTOM, pady=90)

            _resized = _img.resize((250, 250), Image.ANTIALIAS)
            _new_image = ImageTk.PhotoImage(_resized)

            _img_size = Label(self.randomPic)
            _img_size.image = _new_image
            _img_size.config(image=_new_image, pady=50)
            #_img_size.pack(side=TOP, pady=0)
            _img_size.place(anchor='center', x=225, y=185)


            _button_1 = Button(self.randomPic, text="Randomizer", command= lambda gui = self.gui: self.erasePic(gui))
            _button_1.place(anchor='s', relx=0.5, rely=0.90, width=200, height=55)
            ### TEST CODE END
            
    def randNumGen(self, gui):
        _pic_selector = random.randrange(1, 232)
        return _pic_selector
        pass

    def erasePic(self, gui):
        _img_size.place_forget()
        _new_img_path = self.changePic(gui)
        _img = Image.open(_new_img_path)
        _new_img_resized = _img.resize((170, 250), Image.ANTIALIAS)
        _updated_photo = ImageTk.PhotoImage(_new_img_resized)

        _img_update = Label(self.randomPic)
        _img_update.image = _updated_photo
        _img_update.config(image=_updated_photo, pady=50)
        _img_update.place(anchor='center', x=225, y=185)
        #self.changePic(gui)

    def changePic(self, gui):
        _new_num = self.randNumGen(gui)
        _new_path = "Photos/pics_" + str(_new_num) + ".jpg"#_img_generator
        return _new_path


### *** REASSURANCE FUNCTION STARTS HERE ***
    def drawReassuranceQuote(self):
        if self.initialDraw:
            global _reassure_quote
            _reassure_quote = tkinter.StringVar()

            _label = Label(self.reassuranceQuote, text="Reassurance")
            _label.config(font =("Courier", 14))

            _output_quote = tkinter.Label(self.reassuranceQuote, textvariable=_reassure_quote)
            _output_quote.config(font=("courier", 10))
            _output_quote.place(relx=0.50, rely=0.25, anchor='n')

            _button_1 = Button(self.reassuranceQuote, text="REASSURE", command= lambda gui = self.gui: self.reassureUrself(gui))
            _button_1.pack(side=BOTTOM, padx=15, pady=150)
            _button_1.config(pady=10)

            _button_2 = Button(self.reassuranceQuote, text="Fresh Slate", command=lambda gui = self.gui: self.clearQuote(gui))
            _button_2.place(relx=0.5, rely=0.80, anchor='n')
            _button_2.config(pady=10)


            #_textBox.place(height=95 , relx=0.5, rely=0.35, anchor='s')
            _label.place(relx=0.5, rely=0.13, anchor='s')

    def reassureUrself(self, gui):
        _list_reassurances = ['']
        
        
        lst_len = len(_list_reassurances)-1
        rand = random.randint(0, lst_len)
        _reassure_quote.set(_list_reassurances[rand])

    def clearQuote(self, gui):
        _reassure_quote.set('')
    
    def OnExit(self):
        exit(1)    


if __name__ == "__main__":
    root = UserInterface()
    root


