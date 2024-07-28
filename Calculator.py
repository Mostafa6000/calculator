from tkinter import Grid,mainloop
import customtkinter
from math import *

customtkinter.set_appearance_mode("dark")

window=customtkinter.CTk()
window.title("Calculator")
window.geometry("400x550")
window.iconbitmap(r"icon.ico")







#text
text=customtkinter.CTkEntry(window,height=1,fg_color="lightgrey",text_color="#323232",font=("Arial",30))
text.grid(row=0,rowspan=1,columnspan=5,sticky="nsew")

def get_entry():
    return text.get()
calculation=""
#functions
def add(x):
    global calculation
    calculation=str(get_entry())
    calculation += str(x)
    text.delete(0,"end")
    text.insert(0,calculation)
    
def evaluate():
    global calculation
    try:
        equation=get_entry()
        equation=equation.replace("sin(","sin((pi/180)*")
        equation=equation.replace("cos(","cos((pi/180)*")
        equation=equation.replace("tan(","tan((pi/180)*")
        equation=equation.replace("sec(","sec((pi/180)*")
        equation=equation.replace("csc(","csc((pi/180)*")
        equation=equation.replace("cot(","cot((pi/180)*")
        equation=equation.replace("÷","/")
        equation=equation.replace("x","*")
        equation=equation.replace("−","-")
        equation=equation.replace("^","**")
        equation=equation.replace("%","/100")
        equation=equation.replace("²","**2")
        equation=equation.replace("³","**3")
        equation=equation.replace("π","pi")
        equation=equation.replace("log(","log10(")
        equation=equation.replace("ln(","log(")
        equation=equation.replace("fact(","factorial(")
        equation=equation.replace("sin⁻¹(","(180/pi)*asin(")
        equation=equation.replace("tan⁻¹(","(180/pi)*atan(")
        equation=equation.replace("cos⁻¹(","(180/pi)*acos(")
        equation=equation.replace("sinh⁻¹","asinh")
        equation=equation.replace("cosh⁻¹","acosh")
        equation=equation.replace("tanh⁻¹","atanh")
        equation=equation.replace("√(","sqrt(")
        equation=equation.replace("∛(","cubic_root(")
        equation=equation.replace("sec⁻¹(","(180/pi)*asec(")
        equation=equation.replace("csc⁻¹(","(180/pi)*acsc(")
        equation=equation.replace("cot⁻¹(","(180/pi)*acot(")
        equation=equation.replace("sech⁻¹(","asech(")
        equation=equation.replace("csch⁻¹(","acsch(")
        equation=equation.replace("coth⁻¹(","acoth(")
        result=str((eval(equation)))
        result=result.replace("0.9999999999999999","1.0")
        result=result.replace("6.123233995736766e-17","0.0")
        result=result.replace("1.633123935319537e+16","Error")
        result=result.replace("1.0000000000000002","1.0")
        result=result.replace("59.99999999999999","60.0")
        result=result.replace("0.49999999999999994","0.5")
        result=result.replace("0.5000000000000001","0.5")
        result=result.replace("2.0000000000000004","2.0")
        result=result.replace("1.9999999999999996","2.0")
        result=result.replace("30.000000000000004","30.0")
        result=result.replace("60.00000000000001","60.0")
        result=result.replace("29.999999999999996","30.0")
        result=result.replace("29.999999999999993","30.0")
        text.delete(0,"end")
        text.insert(0,result)
    except:
        text.delete(0,"end")
        text.insert(0,"Error")

def clear():
    global calculation
    calculation=""
    text.delete(0,"end")
def delete():
    global calculation
    text1 = text.get()
    text2 = text1[:-1]
    calculation=text2
    text.delete(0, "end")
    text.insert(0, text2)
def absolute():
    global calculation
    try:
        equation=get_entry()
        equation=equation.replace("sin(","sin((pi/180)*")
        equation=equation.replace("cos(","cos((pi/180)*")
        equation=equation.replace("tan(","tan((pi/180)*")
        equation=equation.replace("sec(","sec((pi/180)*")
        equation=equation.replace("csc(","csc((pi/180)*")
        equation=equation.replace("cot(","cot((pi/180)*")
        equation=equation.replace("÷","/")
        equation=equation.replace("x","*")
        equation=equation.replace("−","-")
        equation=equation.replace("^","**")
        equation=equation.replace("%","/100")
        equation=equation.replace("²","**2")
        equation=equation.replace("³","**3")
        equation=equation.replace("π","pi")
        equation=equation.replace("log(","log10(")
        equation=equation.replace("ln(","log(")
        equation=equation.replace("fact(","factorial(")
        equation=equation.replace("sin⁻¹","asin")
        equation=equation.replace("tan⁻¹","atan")
        equation=equation.replace("cos⁻¹","acos")
        equation=equation.replace("sinh⁻¹","asinh")
        equation=equation.replace("cosh⁻¹","acosh")
        equation=equation.replace("tanh⁻¹","atanh")
        equation=equation.replace("√(","sqrt(")
        equation=equation.replace("∛(","cubic_root(")
        equation=equation.replace("sec⁻¹(","asec(")
        equation=equation.replace("csc⁻¹(","acsc(")
        equation=equation.replace("cot⁻¹(","acot(")
        equation=equation.replace("sech⁻¹(","asech(")
        equation=equation.replace("csch⁻¹(","acsch(")
        equation=equation.replace("coth⁻¹(","acoth(")
        result=str(abs(eval(equation)))
        result=result.replace("0.9999999999999999","1.0")
        result=result.replace("6.123233995736766e-17","0.0")
        result=result.replace("1.633123935319537e+16","Error")
        result=result.replace("1.0000000000000002","1.0")
        result=result.replace("59.99999999999999","60.0")
        result=result.replace("0.49999999999999994","0.5")
        result=result.replace("0.5000000000000001","0.5")
        result=result.replace("2.0000000000000004","2.0")
        result=result.replace("1.9999999999999996","2.0")
        result=result.replace("30.000000000000004","30.0")
        result=result.replace("60.00000000000001","60.0")
        result=result.replace("29.999999999999996","30.0")
        result=result.replace("29.999999999999993","30.0")
        text.delete(0,"end")
        text.insert(0,result)
    except:
        text.delete(0,"end")
        text.insert(0,"Error")
def multiplicative_inverse():
    global calculation
    try:
        equation=get_entry()
        equation=equation.replace("sin(","sin((pi/180)*")
        equation=equation.replace("cos(","cos((pi/180)*")
        equation=equation.replace("tan(","tan((pi/180)*")
        equation=equation.replace("sec(","sec((pi/180)*")
        equation=equation.replace("csc(","csc((pi/180)*")
        equation=equation.replace("cot(","cot((pi/180)*")
        equation=equation.replace("÷","/")
        equation=equation.replace("x","*")
        equation=equation.replace("−","-")
        equation=equation.replace("^","**")
        equation=equation.replace("%","/100")
        equation=equation.replace("²","**2")
        equation=equation.replace("³","**3")
        equation=equation.replace("π","pi")
        equation=equation.replace("log(","log10(")
        equation=equation.replace("ln(","log(")
        equation=equation.replace("fact(","factorial(")
        equation=equation.replace("sin⁻¹","asin")
        equation=equation.replace("tan⁻¹","atan")
        equation=equation.replace("cos⁻¹","acos")
        equation=equation.replace("sinh⁻¹","asinh")
        equation=equation.replace("cosh⁻¹","acosh")
        equation=equation.replace("tanh⁻¹","atanh")
        equation=equation.replace("√(","sqrt(")
        equation=equation.replace("∛(","cubic_root(")
        equation=equation.replace("sec⁻¹(","asec(")
        equation=equation.replace("csc⁻¹(","acsc(")
        equation=equation.replace("cot⁻¹(","acot(")
        equation=equation.replace("sech⁻¹(","asech(")
        equation=equation.replace("csch⁻¹(","acsch(")
        equation=equation.replace("coth⁻¹(","acoth(")
        result=str(1/eval(equation))
        result=result.replace("0.9999999999999999","1.0")
        result=result.replace("6.123233995736766e-17","0.0")
        result=result.replace("1.633123935319537e+16","Error")
        result=result.replace("1.0000000000000002","1.0")
        result=result.replace("59.99999999999999","60.0")
        result=result.replace("0.49999999999999994","0.5")
        result=result.replace("0.5000000000000001","0.5")
        result=result.replace("2.0000000000000004","2.0")
        result=result.replace("1.9999999999999996","2.0")
        result=result.replace("30.000000000000004","30.0")
        result=result.replace("60.00000000000001","60.0")
        result=result.replace("29.999999999999996","30.0")
        result=result.replace("29.999999999999993","30.0")
        text.delete(0,"end")
        text.insert(0,result)
    except:
        text.delete(0,"end")
        text.insert(0,"Error")
def hyp():
    btn_30.configure(text="sinh",command=lambda:add("sinh("))
    btn_31.configure(text="cosh",command=lambda:add("cosh("))
    btn_32.configure(text="tanh",command=lambda:add("tanh("))
    btn_34.configure(text="sech",command=lambda:add("sech("))
    btn_35.configure(text="csch",command=lambda:add("csch("))
    btn_36.configure(text="coth",command=lambda:add("coth("))
    btn_33.configure(text="trig",command=lambda:trig())
def trig():
    btn_30.configure(text="sin",command=lambda:add("sin("))
    btn_31.configure(text="cos",command=lambda:add("cos("))
    btn_32.configure(text="tan",command=lambda:add("tan("))
    btn_34.configure(text="sec",command=lambda:add("sec("))
    btn_35.configure(text="csc",command=lambda:add("csc("))
    btn_36.configure(text="cot",command=lambda:add("cot("))
    btn_33.configure(text="hyp",command=lambda:hyp())
def inv():
    if btn_40.cget("text")=="x²":
        btn_40.configure(text="√",command=lambda:add("√("))
    elif btn_40.cget("text")=="√":
        btn_40.configure(text="x²",command=lambda:add("²"))
    if btn_39.cget("text")=="x³":
        btn_39.configure(text="∛",command=lambda:add("∛("))
    elif btn_39.cget("text")=="∛":
        btn_39.configure(text="x³",command=lambda:add("³"))

    if btn_30.cget("text")=="sin":
        btn_30.configure(text="sin⁻¹",command=lambda:add("sin⁻¹("))
        btn_31.configure(text="cos⁻¹",command=lambda:add("cos⁻¹("))
        btn_32.configure(text="tan⁻¹",command=lambda:add("tan⁻¹("))
        btn_34.configure(text="sec⁻¹",command=lambda:add("sec⁻¹("))
        btn_35.configure(text="csc⁻¹",command=lambda:add("csc⁻¹("))
        btn_36.configure(text="cot⁻¹",command=lambda:add("cot⁻¹("))
        
    elif btn_30.cget("text")=="sinh":
        btn_30.configure(text="sinh⁻¹",command=lambda:add("sinh⁻¹("))
        btn_31.configure(text="cosh⁻¹",command=lambda:add("cosh⁻¹("))
        btn_32.configure(text="tanh⁻¹",command=lambda:add("tanh⁻¹("))
        btn_34.configure(text="sech⁻¹",command=lambda:add("sech⁻¹("))
        btn_35.configure(text="csch⁻¹",command=lambda:add("csch⁻¹("))
        btn_36.configure(text="coth⁻¹",command=lambda:add("coth⁻¹("))
        
    elif btn_30.cget("text")=="sin⁻¹":
        btn_30.configure(text="sin",command=lambda:add("sin("))
        btn_31.configure(text="cos",command=lambda:add("cos("))
        btn_32.configure(text="tan",command=lambda:add("tan("))
        btn_34.configure(text="sec",command=lambda:add("sec("))
        btn_35.configure(text="csc",command=lambda:add("csc("))
        btn_36.configure(text="cot",command=lambda:add("cot("))
        
    elif btn_30.cget("text")=="sinh⁻¹":
        btn_30.configure(text="sinh",command=lambda:add("sinh("))
        btn_31.configure(text="cosh",command=lambda:add("cosh("))
        btn_32.configure(text="tanh",command=lambda:add("tanh("))
        btn_34.configure(text="sech",command=lambda:add("sech("))
        btn_35.configure(text="csch",command=lambda:add("csch("))
        btn_36.configure(text="coth",command=lambda:add("coth("))
def asec(x):
    global calculation
    y=1/x
    return acos(y)
def acsc(x):
    global calculation
    y=1/x
    return asin(y)
def acot(x):
    global calculation
    y=1/x
    return atan(y)
def asech(x):
    global calculation
    y=1/x
    return acosh(y)
def acsch(x):
    global calculation
    y=1/x
    return asinh(y)
def acoth(x):
    global calculation
    y=1/x
    return atanh(y)

def cubic_root(x):
    if x<0:
        return str(-(-x)**(1/3))
    else:
        return str(x**(1/3))
def sec(x):
    y=cos(x)
    return 1/y
def csc(x):
    y=sin(x)
    return 1/y
def cot(x):
    y=str(tan(x))
    y=float(y.replace("1.633123935319537e+16","Error"))
    return 1/y
def sech(x):
    y=cosh(x)
    return 1/y
def csch(x):
    y=sinh(x)
    return 1/y
def coth(x):
    y=tanh(x)
    return 1/y



        



#buttons
btn_1=customtkinter.CTkButton(master=window,text="0",font=("Arial",20),fg_color="#323232",text_color="white",hover_color="#3c3c3c",command=lambda:add("0"))
btn_1.grid(row=8,column=2,sticky="nsew")
btn_2=customtkinter.CTkButton(master=window,text=".",font=("Arial",20),fg_color="#323232",text_color="white",hover_color="#3c3c3c",command=lambda:add("."))
btn_2.grid(row=8,column=3,sticky="nsew")
btn_3=customtkinter.CTkButton(master=window,text="1",font=("Arial",20),fg_color="#323232",text_color="white",hover_color="#3c3c3c",command=lambda:add("1"))
btn_3.grid(row=7,column=1,sticky="nsew")
btn_4=customtkinter.CTkButton(master=window,text="2",font=("Arial",20),fg_color="#323232",text_color="white",hover_color="#3c3c3c",command=lambda:add("2"))
btn_4.grid(row=7,column=2,sticky="nsew")
btn_5=customtkinter.CTkButton(master=window,text="3",font=("Arial",20),fg_color="#323232",text_color="white",hover_color="#3c3c3c",command=lambda:add("3"))
btn_5.grid(row=7,column=3,sticky="nsew")
btn_6=customtkinter.CTkButton(master=window,text="4",font=("Arial",20),fg_color="#323232",text_color="white",hover_color="#3c3c3c",command=lambda:add("4"))
btn_6.grid(row=6,column=1,sticky="nsew")
btn_7=customtkinter.CTkButton(master=window,text="5",font=("Arial",20),fg_color="#323232",text_color="white",hover_color="#3c3c3c",command=lambda:add("5"))
btn_7.grid(row=6,column=2,sticky="nsew")
btn_8=customtkinter.CTkButton(master=window,text="6",font=("Arial",20),fg_color="#323232",text_color="white",hover_color="#3c3c3c",command=lambda:add("6"))
btn_8.grid(row=6,column=3,sticky="nsew")
btn_9=customtkinter.CTkButton(master=window,text="7",font=("Arial",20),fg_color="#323232",text_color="white",hover_color="#3c3c3c",command=lambda:add("7"))
btn_9.grid(row=5,column=1,sticky="nsew")
btn_10=customtkinter.CTkButton(master=window,text="8",font=("Arial",20),fg_color="#323232",text_color="white",hover_color="#3c3c3c",command=lambda:add("8"))
btn_10.grid(row=5,column=2,sticky="nsew")
btn_11=customtkinter.CTkButton(master=window,text="9",font=("Arial",20),fg_color="#323232",text_color="white",hover_color="#3c3c3c",command=lambda:add("9"))
btn_11.grid(row=5,column=3,sticky="nsew")
btn_12=customtkinter.CTkButton(master=window,text="=",font=("Arial",20),fg_color="#ca9c9d",text_color="#323232",hover_color="#ca9c9d",command=lambda:evaluate())
btn_12.grid(row=8,column=4,sticky="nsew")
btn_13=customtkinter.CTkButton(master=window,text="+",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("+"))
btn_13.grid(row=7,column=4,sticky="nsew")
btn_14=customtkinter.CTkButton(master=window,text="−",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("−"))
btn_14.grid(row=6,column=4,sticky="nsew")
btn_15=customtkinter.CTkButton(master=window,text="x",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("x"))
btn_15.grid(row=5,column=4,sticky="nsew")
btn_16=customtkinter.CTkButton(master=window,text="%",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("%"))
btn_16.grid(row=3,column=4,sticky="nsew")
btn_17=customtkinter.CTkButton(master=window,text="÷",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("÷"))
btn_17.grid(row=4,column=4,sticky="nsew")
btn_18=customtkinter.CTkButton(master=window,text=")",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add(")"))
btn_18.grid(row=4,column=2,sticky="nsew")
btn_19=customtkinter.CTkButton(master=window,text="(",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("("))
btn_19.grid(row=4,column=1,sticky="nsew")
btn_20=customtkinter.CTkButton(master=window,text="C",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:clear())
btn_20.grid(row=1,column=3,sticky="nsew")
btn_21=customtkinter.CTkButton(master=window,text="DEL",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:delete())
btn_21.grid(row=1,column=4,sticky="nsew")
btn_22=customtkinter.CTkButton(master=window,text="x!",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("fact("))
btn_22.grid(row=4,column=3,sticky="nsew")
btn_23=customtkinter.CTkButton(master=window,text="00",font=("Arial",20),fg_color="#323232",text_color="white",hover_color="#3c3c3c",command=lambda:add("00"))
btn_23.grid(row=8,column=1,sticky="nsew")
btn_24=customtkinter.CTkButton(master=window,text="ln",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("ln("))
btn_24.grid(row=8,column=0,sticky="nsew")
btn_25=customtkinter.CTkButton(master=window,text="log",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("log("))
btn_25.grid(row=7,column=0,sticky="nsew")
btn_26=customtkinter.CTkButton(master=window,text="e",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("e"))
btn_26.grid(row=6,column=0,sticky="nsew")
btn_27=customtkinter.CTkButton(master=window,text="π",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("π"))
btn_27.grid(row=5,column=0,sticky="nsew")
btn_28=customtkinter.CTkButton(master=window,text="|x|",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:absolute())
btn_28.grid(row=4,column=0,sticky="nsew")
btn_29=customtkinter.CTkButton(master=window,text="INV",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:inv())
btn_29.grid(row=3,column=0,sticky="nsew")
btn_30=customtkinter.CTkButton(master=window,text="sin",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("sin("))
btn_30.grid(row=3,column=1,sticky="nsew")
btn_31=customtkinter.CTkButton(master=window,text="cos",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("cos("))
btn_31.grid(row=3,column=2,sticky="nsew")
btn_32=customtkinter.CTkButton(master=window,text="tan",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("tan("))
btn_32.grid(row=3,column=3,sticky="nsew")
btn_33=customtkinter.CTkButton(master=window,text="hyp",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:hyp())
btn_33.grid(row=2,column=0,sticky="nsew")
btn_34=customtkinter.CTkButton(master=window,text="sec",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("sec("))
btn_34.grid(row=2,column=1,sticky="nsew")
btn_35=customtkinter.CTkButton(master=window,text="csc",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("csc("))
btn_35.grid(row=2,column=2,sticky="nsew")
btn_36=customtkinter.CTkButton(master=window,text="cot",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("cot("))
btn_36.grid(row=2,column=3,sticky="nsew")
btn_37=customtkinter.CTkButton(master=window,text="^",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("^"))
btn_37.grid(row=2,column=4,sticky="nsew")
btn_38=customtkinter.CTkButton(master=window,text="1/x",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:multiplicative_inverse())
btn_38.grid(row=1,column=0,sticky="nsew")
btn_39=customtkinter.CTkButton(master=window,text="x³",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("³"))
btn_39.grid(row=1,column=1,sticky="nsew")
btn_40=customtkinter.CTkButton(master=window,text="x²",font=("Arial",20),fg_color="#3c3c3c",text_color="white",hover_color="#323232",command=lambda:add("²"))
btn_40.grid(row=1,column=2,sticky="nsew")
#configuration
Grid.rowconfigure(window,0,weight=1)
Grid.rowconfigure(window,1,weight=1)
Grid.rowconfigure(window,2,weight=1)
Grid.rowconfigure(window,3,weight=1)
Grid.rowconfigure(window,4,weight=1)
Grid.rowconfigure(window,5,weight=1)
Grid.rowconfigure(window,6,weight=1)
Grid.rowconfigure(window,7,weight=1)
Grid.rowconfigure(window,8,weight=1)
Grid.columnconfigure(window,0,weight=1)
Grid.columnconfigure(window,1,weight=1)
Grid.columnconfigure(window,2,weight=1)
Grid.columnconfigure(window,3,weight=1)
Grid.columnconfigure(window,4,weight=1)


window.mainloop()