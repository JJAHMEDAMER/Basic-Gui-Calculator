import tkinter as tk

BUTTON_WIDTH = 20
BUTTON_HEIGHT = 17.5

RESULT = ""

BUTTON_COLOR = "#1c2e4a"
TEXT_COLOR = "#FAF9F9"
CLEAR_BUTTON_COLOR ="#F96900"
BG_COLOR = "#152238"
EQUAL_COLOR = "#CA2E55"


class Button:
    def __init__(self, number = "1", x_grid = 1, y_grid = 1, span = 1) -> None:
        self.number = number
        
        if self.number == "=":
            command = self.evaluate
            button_color = EQUAL_COLOR
        elif self.number == "C":
            command = self.clear
            button_color = CLEAR_BUTTON_COLOR
        else:
            command = self.func
            button_color = BUTTON_COLOR
        
        self.button = tk.Button(
            frame_button, 
            text = number,
            font = ("Consolas", 14),
            padx=BUTTON_WIDTH,
            pady=BUTTON_HEIGHT,
            bg = button_color,
            fg = TEXT_COLOR,
            bd = 0,
            command=command
            )
        self.button.grid(row=x_grid, column=y_grid, columnspan=span, padx = 1, pady = 1)
        
    def func(self):
        global RESULT
        RESULT += self.number
        display.display_config()
        
    def evaluate(self):
        global RESULT
        RESULT = str(eval(RESULT))
        display.display_config()
        
    def clear(self):
        display.display_clear()
            
        
        
        
class Display:
    def __init__(self) -> None:
        self.text_box = tk.Text(
            dispaly_frame, 
            font = ("Consolas", 24),
            width=1,
            height = 2,
            bg = BG_COLOR,
            fg = TEXT_COLOR,
            bd = 0,
            )
        self.text_box.pack(fill=tk.BOTH)
    
    def display_config(self):
        global RESULT
        self.text_box.delete(1.0, "end")
        self.text_box.insert(1.0, RESULT)
        
    def display_clear(self):
        global RESULT
        RESULT = ""
        self.text_box.delete(1.0, "end")
        
    


win = tk.Tk()
win.title("Calculator")
win.iconbitmap("D:\\004-Programing\\Python\\calculators\\Basic Gui Calculator\\imgs\\icon.ico")

dispaly_frame = tk.LabelFrame(win, bg = BG_COLOR)
dispaly_frame.pack(fill=tk.BOTH)

display = Display()

frame_button = tk.LabelFrame(win, bg = BG_COLOR)
frame_button.pack(fill=tk.BOTH)

button1 = Button("1", 3, 1)
button2 = Button("2", 3, 2)
button3 = Button("3", 3, 3)

button4 = Button("4", 2, 1)
button5 = Button("5", 2, 2)
button6 = Button("6", 2, 3)

button7 = Button("7", 1, 1)
button8 = Button("8", 1, 2)
button9 = Button("9", 1, 3)

decimal_button = Button(".", 4, 1)
button0 = Button("0", 4, 2)
clear_button = Button("C", 4, 3)

plus_button = Button("+", 1, 4)
minus_button = Button("-", 2, 4)
mult_button = Button("*", 3, 4)
divide_button = Button("/", 4, 4)


equal_button = Button("=", 5,1, 2)
bracket_left_button = Button("(", 5,3)
bracket_right_button = Button(")", 5,4)

win.mainloop()