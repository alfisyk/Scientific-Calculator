#muhammad_alfi_syakir
#sistem_informasi
#1806191364

#mengimport module
from tkinter import * 
from math import *
from struct import *
from idlelib.tooltip import *

class SuperCal():   #make SuperCal() class
    def __init__(self):
        window= Tk() #create window
        window.title("Supercalculator [by Muhammad Alfi Syakir for DDP1 2018]")
        window.resizable(False,False) #make window unresizeable
       
        self.memory= '' #memory
        self.expr= ''   #current expression
        self.startOfNextOperand= True #start of new operand
        #make a buttons title
        buttons= [['Clr','MC', 'M+', 'M-', 'MR'],
                  ['d', 'e', 'f', '+', '-'],
                  ['a', 'b', 'c', '/', '*'],
                  ['7', '8', '9', '**', '\u221a'],
                  ['4', '5', '6', 'sin', 'cos'],
                  ['1', '2', '3', 'tan', 'ln'],
                  ['0', '.', '±', '~', '2C'],
                  ['x', 'o', '^', '|', '&'],
                  ['π', 'int', 'rad', '//', 'exp'],
                  ['→IEEE', '←IEEE', 'asin', 'acos', 'atan'],
                  ['bin', 'hex', 'oct', '%', '=']]
        #make a buttons tip
        tiptext=[['Clear the display field','Clear memory', 'Add to memory', 'Subtract from memory', 'Recall from memory'],
                  ['letter d', 'letter e', 'letter f', 'add', 'subtract'],
                  ['letter a', 'letter b', 'letter c', 'divide', 'multiply'],
                  ['digit 7', 'digit 8', 'digit 9', 'power', 'sqrt'],
                  ['digit 4', 'digit 5', 'igit 6', 'sine(radians)', 'cosine(radians)'],
                  ['digit 1', 'digit 2', 'digit 3', 'tangent(radians)', 'natural log'],
                  ['digit 0', 'decimal point', 'toogle +- sign', 'bitwise complement', "32-bit 2's complement"],
                  ['letter x', 'letter o', 'bitwise xor', 'bitwise or', 'bitwise and'],
                  ['the number Pi', 'truncate float to int', 'convert degrees to radians', 'integer divide', 'power of E(2.718...)'],
                  ['decimal to 64-bit IEEE 754 representation (in hex)', '64-bit IEEE 754 representation (in hex) to decimal', 'arc sine, in radians', 'arc cosine, in radians', 'arc tangent, in radians'],
                  ['convert int to binary', 'convert int to hexadecimal', 'convert int to octal', 'modulus', 'compute to decimal']]
        #make math dictionary
        self.mathem= {'int': floor,'ln': log ,'exp': exp,'\u221a': sqrt, 'rad': radians, 'sin': sin, 'cos': cos, 'tan': tan, 'asin':asin, 'acos':acos, 'atan': atan, 'bin': bin, 'hex': hex, 'oct': oct}         
        #use Entry widget for dispaly
        self.entry= Entry(window, relief=RIDGE, borderwidth=3,
                          width= 35, bg='cyan', fg='blue', font=('Helvetica', 18))
        self.entry.grid(row=0, column=0, columnspan=5)
        self.entry.insert(END, 'Welcome :)')
        #create and place buttons in appropriate row and column
        for r in range (11):
            for c in range (5):
                def cmd(x=buttons[r][c]):
                    self.click(x)
                #make different buttons color
                if ((1<= r <=5) and (0<= c <= 2)) or (r==6 and c==0):    
                    self.tombol= Button(window, text= buttons[r][c], width=6, font='Arial 18', bg='cyan', fg='#0E4D92', relief= RAISED, command=cmd)
                elif r==0:
                    if c==0:
                        self.tombol= Button(window, text= buttons[r][c], width=6, font='Arial 18', bg='red', fg='black', relief= RAISED, command=cmd) 
                    else:
                        self.tombol= Button(window, text= buttons[r][c], width=6, font='Arial 18', bg='#008ECC', fg='#1D2951', relief= RAISED, command=cmd)
                else:
                    self.tombol= Button(window, text= buttons[r][c], width=6, font='Arial 18', bg='#0E4D92', fg='cyan', relief= RAISED, command=cmd)
                self.tombol.grid(row= r+1, column= c)
                tooltips= tiptext[r][c]
                ToolTip(self.tombol, tooltips) #add button tip
        window.mainloop()

    def click(self,key): #handler for event of pressing button labeled key
        if key== '=':
            #evaluate the expression, including the value
            #displayed in entry and display result
            try:
                result = eval(self.expr + self.entry.get())
                self.entry.delete(0,END)
                self.entry.insert(END, result)
                self.expr= ''
                self.startOfNextOperand=True
            except: 
                self.entry.delete(0, END)
                self.entry.insert(END, 'Error')

        elif key == 'MC': #clear memory
            self.memory=''
        elif key == 'M+': #add to memory
            try:
                if self.memory != '':
                    self.memory= str(eval(self.memory) + eval(self.entry.get()))
                else:
                    self.memory+= str(eval(self.entry.get()))
            except: #if there is no value in entry or value error, insert Error
                self.entry.delete(0, END)
                self.entry.insert(END, 'Error')
        elif key == 'M-': #subtract from memory
            try:
                if self.memory != '':
                    self.memory= str(eval(self.memory) - eval(self.entry.get()))
                else:
                    self.memory= str(0- eval(self.entry.get()))
            except: #if there is no value in entry or value error, insert Error
                self.entry.delete(0, END)
                self.entry.insert(END, 'Error') 
        elif key == 'MR': #recall memory
            self.entry.delete(0,END)
            self.entry.insert(END, self.memory)

        elif key in '+//*-**/%^|&': #add operand displayed in entry and operator key
            self.expr += self.entry.get()
            self.expr += key
            self.startOfNextOperand= True #to expression and prepare for next operand

        elif key == '~': #bitwise complement
            try:
                self.expr+= str(~eval(self.entry.get()))
                self.entry.delete(0,END)
                self.entry.insert(END, self.expr)
                self.expr= ''
                self.startOfNextOperand= True
            except: #if there is no value in entry or value error, insert Error
                self.entry.delete(0, END)
                self.entry.insert(END, 'Error')

        elif key == '2C': #find 32-bit 2's complement 
            try:
                self.expr += '0b' + (format(int(self.entry.get())+2**32, 'b')[1:])
                self.entry.delete(0,END)
                self.entry.insert(END, self.expr)
                self.expr= ''
                self.startOfNextOperand= True
            except: #if there is no value in entry or value error, insert Error
                self.entry.delete(0, END)
                self.entry.insert(END, 'Error')
        
        elif key == 'π': #insert pi to entry
            self.entry.delete(0,END)
            self.entry.insert(END, pi)
            self.startOfNextOperand= True
                    
        elif key in self.mathem: #run math operation (trigonometry, bin, hex, oct, int)
            try:
                self.expr += str(self.mathem[key](eval(self.entry.get())))
                self.entry.delete(0,END)
                self.entry.insert(END, self.expr)
                self.expr= ''
                self.startOfNextOperand= True
            except: #if there is no value in entry or value error, insert Error
                self.entry.delete(0, END)
                self.entry.insert(END, 'Error')
        
        elif key == '±':
            #switch entry from positive to negative or vice verse
            #if there is no value in entry, do nothing
            try:
                if self.entry.get()[0] == '-':
                    self.entry.delete(0)
                else:
                    self.entry.insert(0, '-')
            except IndexError:
                pass

        elif key == '→IEEE': #decimal to 64-bit IEEE 754 representation (in hex)
            try:
                self.expr= (hex(unpack('Q', pack('d', eval(self.entry.get())))[0]))[2:] 
                self.entry.delete(0,END)
                self.entry.insert(END, self.expr)
                self.expr= ''
                self.startOfNextOperand= True
            except: #if there is no value in entry or value error, insert Error
                self.entry.delete(0, END)
                self.entry.insert(END, 'Error')

        elif key == '←IEEE': #64-bit IEEE 754 representation (in hex) to decimal
            try:
                self.expr= unpack('d', pack('Q', int('0x' + self.entry.get(),16)))[0]
                self.entry.delete(0,END)
                self.entry.insert(END, self.expr)
                self.expr= ''
                self.startOfNextOperand= True
            except: #if there is no value in entry or value error, insert Error
                self.entry.delete(0, END)
                self.entry.insert(END, 'Error')

        elif key == 'Clr': #clear all entry
            self.entry.delete(0, END)
           
        else:
            #insert digit at end of entry, or as the first
            #digit if start of next operand
            if self.startOfNextOperand:
                self.entry.delete(0, END)
                self.startOfNextOperand= False
            self.entry.insert(END,key)

if __name__ == "__main__":       
    SuperCal()