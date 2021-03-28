import sys
import os
from tkinter import *
import math,random
from tkinter import messagebox
from tkinter import ttk
import datetime
import time
root=Tk() 
scroll_text= StringVar()
msg2 = "THANK YOU FOR VISITING US..."
text2 = ""
n=0
class Bill_App:
#,bg="#03C04A"
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("WALMART")
        bg_color="#0BB5FF"
        title=Label(self.root,text="WALMART",bd=10,relief=GROOVE,bg=bg_color,fg="#003151",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #=====var====
        #====juices======
        self.sprite=IntVar()
        self.thumbsup=IntVar()
        self.coco_cola=IntVar()
        self.sveen_Up=IntVar()
        self.Dukes=IntVar()
        self.mirinda=IntVar()

        #=====chips=====
        self.lays=IntVar()
        self.doritos=IntVar()
        self.pringles=IntVar()
        self.peppy=IntVar()
        self.kurkure=IntVar()
        self.wheels=IntVar()

        #=====Chocolate====
        self.silk=IntVar()
        self.toblerone=IntVar()
        self.kitkat=IntVar()
        self.snicker=IntVar()
        self.star=IntVar()
        self.fuse=IntVar()

        #=====Total Price=====
        self.juice_price=StringVar()
        self.chips_price=StringVar()
        self.chocolate_price=StringVar()

        #=======Tax price======
        self.juice_tax=StringVar()
        self.chips_tax=StringVar()
        self.chocolate_tax=StringVar()

        #====name of customer=====
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill=StringVar()
        a=random.randint(1000,9999)
        self.bill.set(str(a))
        self.search_bill=StringVar()

        #===========cust Detail========
        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),bg=bg_color,fg="#191970")#
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Name Of Customer",bg=bg_color,fg="#003151",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=20,textvariable=self.c_name,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)

        cphn_lbl=Label(F1,text="Phone Number",bg=bg_color,fg="#003151",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=20,textvariable=self.c_phon,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=5,pady=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="#003151",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=20,textvariable=self.search_bill,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=5,pady=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,bg="#03C04A",fg="white",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=40)

        #======Juices Frame=======
        F2=LabelFrame(self.root,text="Juices",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="#191970",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        sprite_lbl1=Label(F2,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        sprite_txt=Entry(F2,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
     
        thumbsup_lbl1=Label(F2,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        thumbsup_txt=Entry(F2,width=10,textvariable=self.thumbsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        coco_cola_lbl1=Label(F2,text="Coco Cola",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        coco_cola_txt=Entry(F2,width=10,textvariable=self.coco_cola,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        sveen_Up_lbl1=Label(F2,text="7 Up",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        sveen_Up_txt=Entry(F2,width=10,textvariable=self.sveen_Up,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
       
        Dukes_lbl1=Label(F2,text="Dukes Soda",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Dukes_txt=Entry(F2,width=10,textvariable=self.Dukes,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        mirinda_lbl1=Label(F2,text="Mirinda",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        mirinda_txt=Entry(F2,width=10,textvariable=self.mirinda,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #  =======Chips Frame=======

        F3=LabelFrame(self.root,text="Chips",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="#191970",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)

        lays_lbl1=Label(F3,text="Lays",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        lays_txt=Entry(F3,width=10,textvariable=self.lays,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
     
        doritos_lbl1=Label(F3,text="Doritos",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        doritos_txt=Entry(F3,width=10,textvariable=self.doritos,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        pringles_lbl1=Label(F3,text="Pringles",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        pringles_txt=Entry(F3,width=10,textvariable=self.pringles,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        peppy_lbl1=Label(F3,text="Peppy",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        peppy_txt=Entry(F3,width=10,textvariable=self.peppy,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
       
        kurkure_lbl1=Label(F3,text="Kurkure",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        kurkure_txt=Entry(F3,width=10,textvariable=self.kurkure,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        wheels_lbl1=Label(F3,text="Wheels",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        wheels_txt=Entry(F3,width=10,textvariable=self.wheels,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #========Chocolate============

        F4=LabelFrame(self.root,text="Chocolate",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="#191970",bg=bg_color)
        F4.place(x=670,y=180,width=325,height=380)

        silk_lbl1=Label(F4,text="Silk Oreo",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        silk_txt=Entry(F4,width=10,textvariable=self.silk,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
     
        toblerone_lbl1=Label(F4,text="Toblerone",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        toblerone_txt=Entry(F4,width=10,textvariable=self.toblerone,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        kitkat_lbl1=Label(F4,text="Kit kat",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        kitkat_txt=Entry(F4,width=10,textvariable=self.kitkat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        snicker_lbl1=Label(F4,text="Snickers",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        snicker_txt=Entry(F4,width=10,textvariable=self.snicker,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
       
        star_lbl1=Label(F4,text="5 Star",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        star_txt=Entry(F4,width=10,textvariable=self.star,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        fuse_lbl1=Label(F4,text="Fuse",font=("times new roman",16,"bold"),bg=bg_color,fg="#003151").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        fuse_txt=Entry(F4,width=10,textvariable=self.fuse,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        
        # Bill

        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=520,height=380)
        bill=Label(F5,text="BILL",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #=======Button=======
        F6=LabelFrame(self.root,text="Bill Menu",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="#191970",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)

        a1_lbl1=Label(F6,text="Total Juice Price",bg=bg_color,fg="#003151",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        a1_txt=Entry(F6,width=18,textvariable=self.juice_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        a2_lbl1=Label(F6,text="Total Chips Price",bg=bg_color,fg="#003151",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        a2_txt=Entry(F6,width=18,textvariable=self.chips_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        a3_lbl1=Label(F6,text="Total Chocolate Price",bg=bg_color,fg="#003151",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        a3_txt=Entry(F6,width=18,textvariable=self.chocolate_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        
        b1_lbl1=Label(F6,text="Juice Tax",bg=bg_color,fg="#003151",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        b1_txt=Entry(F6,width=18,textvariable=self.juice_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        b2_lbl1=Label(F6,text="Chips Tax",bg=bg_color,fg="#003151",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        b2_txt=Entry(F6,width=18,textvariable=self.chips_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        b3_lbl1=Label(F6,text="Chocolate Tax",bg=bg_color,fg="#003151",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        b3_txt=Entry(F6,width=18,textvariable=self.chocolate_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_A=Frame(F6,bd=7,relief=GROOVE)
        btn_A.place(x=750,width=570,height=105)

        

        total=Button(btn_A,command=self.total,text="Total",bg="#03C04A",fg="White",bd=5,pady=15,width=11,font="arial 13 bold").grid(row=0,column=0,padx=5,pady=5)
        Generate_bill=Button(btn_A,command=self.bill_area,text="Generate Bill",bg="#03C04A",fg="White",bd=5,pady=15,width=11,font="arial 13 bold").grid(row=0,column=1,padx=5,pady=5)
        clear=Button(btn_A,text="Clear",command=self.clear_data,bg="#03C04A",fg="White",bd=5,pady=15,width=11,font="arial 13 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit=Button(btn_A,text="Exit",command=self.Exit_app,bg="#03C04A",fg="White",bd=5,pady=15,width=11,font="arial 13 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,fg="#191970",bg=bg_color)
        F6.place(x=0,y=690,relwidth=1,height=110)


         #============scroll text=============
        
        def display():
            global text2, n, msg2
            for t in range(len(msg2)):
                for k in range(t):
                    text2 += ' '
                for g in range(len(msg2) - t):
                    text2 += msg2[g]
                #text2 = text2.strip()
                F6.update()
                F6.after(200)
                text2 = text2.strip()
                scroll_text.set('')
                scroll_text.set(text2)
                text2 = ''
            scroll_text.set('')
            txtscroll.after(200,display)
        
        txtscroll=Entry(F6,textvariable=scroll_text, font=('arial',50,'bold'), fg='#003151', bd=10, bg=bg_color, width=150)
        txtscroll.grid(row=0, column=0, columnspan=4)
        display()

    def total(self):
        self.lays_price=10
        self.doritos_price=50
        self.pringles_price=90
        self.peppy_price=90
        self.kurkure_price=10
        self.wheels_price=10
        self.c_l_p=(self.lays.get()*self.lays_price)
        self.c_d_p=(self.doritos.get()*self.doritos_price)
        self.c_p_p=(self.pringles.get()*self.pringles_price)
        self.c_pe_p=(self.peppy.get()*self.peppy_price)
        self.c_ku_p=(self.kurkure.get()*self.kurkure_price)
        self.c_w_p=(self.wheels.get()*self.wheels_price)
        self.total_chips_price=float(
                                self.c_l_p+
                                self.c_d_p+
                                self.c_p_p+
                                self.c_pe_p+
                                self.c_ku_p+
                                self.c_w_p
                                )
        self.chips_price.set("Rs. "+str(self.total_chips_price))
        self.cs_tax=round((self.total_chips_price*0.1),2)
        self.chips_tax.set("Rs. "+str(self.cs_tax))

        self.sprite_price=40
        self.thumbsup_price=50
        self.coco_cola_price=50
        self.sevenup_price=40
        self.dukes_price=50
        self.mirinda_price=40
        self.j_s_p= (self.sprite.get()*self.sprite_price)
        self.j_t_p=(self.thumbsup.get()*self.thumbsup_price)
        self.j_c_p=(self.coco_cola.get()*self.coco_cola_price)
        self.j_sv_p=(self.sveen_Up.get()*self.sevenup_price)
        self.j_d_p=(self.Dukes.get()*self.dukes_price)
        self.j_m_p=(self.mirinda.get()*self.mirinda_price)
        self.total_juice_price=float(
                                self.j_s_p+
                                self.j_t_p+
                                self.j_c_p+
                                self.j_sv_p+
                                self.j_d_p+
                                self.j_m_p
                                )
        self.juice_price.set("Rs. "+str(self.total_juice_price))
        self.je_tax=round((self.total_juice_price*0.05),2)
        self.juice_tax.set("Rs. "+str(self.je_tax))

        self.silk_price=80
        self.toblerone_price=50
        self.kitkat_price=40
        self.snicker_price=50
        self.star_price=30
        self.fuse_price=20
        self.c_s_p=(self.silk.get()*self.silk_price)
        self.c_t_p=(self.toblerone.get()*self.toblerone_price)
        self.c_k_p=(self.kitkat.get()*self.kitkat_price)
        self.c_sr_p=(self.snicker.get()*self.snicker_price)
        self.c_st_p=(self.star.get()*self.star_price)
        self.c_f_p=(self.fuse.get()*self.fuse_price)
        self.total_chocolate_price=float(
                                self.c_s_p+
                                self.c_t_p+
                                self.c_k_p+
                                self.c_sr_p+
                                self.c_st_p+
                                self.c_f_p
                                )
        self.chocolate_price.set("Rs. "+str(self.total_chocolate_price))
        self.ch_tax=round((self.total_chocolate_price*0.15),2)
        self.chocolate_tax.set("Rs. "+str(self.ch_tax))
    
        self.Total_bill=float(self.total_chips_price+
                            self.total_chocolate_price+
                            self.total_juice_price+
                            self.cs_tax+
                            self.je_tax+
                            self.ch_tax
                            )   

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\t\tWELCOME FOOD RETAIL\n")
        self.txtarea.insert(END,f"\n BILL NUMBER : {self.bill.get()}")
        self.txtarea.insert(END,f"\n CUSTOMER NAME : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n PHONE NUMBER : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n===========================================================")
        self.txtarea.insert(END,f"\n PRODUCTS\t\tQUANTITY\t\tPRICE\t\tTOTAL PRICE")
        self.txtarea.insert(END,f"\n===========================================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Detais are Required")
        elif self.juice_price.get()=="Rs. 0.0" and self.chips_price.get()=="Rs. 0.0" and self.chocolate_price.get()=="Rs. 0.0":
             messagebox.showerror("Error","Products Not selected")
        else:
            self.welcome_bill()

            #====juice bill generate======
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.sprite_price}\t\t{self.j_s_p}")
            if self.thumbsup.get()!=0:
                self.txtarea.insert(END,f"\n Thumbs Up\t\t{self.thumbsup.get()}\t\t{self.thumbsup_price}\t\t{self.j_t_p}")
            if self.coco_cola.get()!=0:
                self.txtarea.insert(END,f"\n Coco Cola\t\t{self.coco_cola.get()}\t\t{self.coco_cola_price}\t\t{self.j_c_p}")
            if self.sveen_Up.get()!=0:
                self.txtarea.insert(END,f"\n 7 UP\t\t{self.sveen_Up.get()}\t\t{self.sevenup_price}\t\t{self.j_sv_p}")
            if self.Dukes.get()!=0:
                self.txtarea.insert(END,f"\n Dukes Soda\t\t{self.Dukes.get()}\t\t{self.dukes_price}\t\t{self.j_d_p}")
            if self.mirinda.get()!=0:
                self.txtarea.insert(END,f"\n Mirinda\t\t{self.mirinda.get()}\t\t{self.mirinda_price}\t\t{self.j_m_p}")
                
            #=========chips bill generate======    
            if self.lays.get()!=0:
                self.txtarea.insert(END,f"\n Lays\t\t{self.lays.get()}\t\t{self.lays_price}\t\t{self.c_l_p}")
            if self.doritos.get()!=0:
                self.txtarea.insert(END,f"\n Doritos\t\t{self.doritos.get()}\t\t{self.doritos_price}\t\t{self.c_d_p}")
            if self.pringles.get()!=0:
                self.txtarea.insert(END,f"\n Pringles\t\t{self.pringles.get()}\t\t{self.pringles_price}\t\t{self.c_p_p}")
            if self.peppy.get()!=0:
                self.txtarea.insert(END,f"\n Peppy\t\t{self.peppy.get()}\t\t{self.peppy_price}\t\t{self.c_pe_p}")
            if self.kurkure.get()!=0:
                self.txtarea.insert(END,f"\n Kurkure\t\t{self.kurkure.get()}\t\t{self.kurkure_price}\t\t{self.c_ku_p}")
            if self.wheels.get()!=0:
                self.txtarea.insert(END,f"\n Wheels\t\t{self.wheels.get()}\t\t{self.wheels_price}\t\t{self.c_w_p}")

            #=========chocolate bill generate=====
            if self.silk.get()!=0:
                self.txtarea.insert(END,f"\n DairyMilk Silk\t\t{self.silk.get()}\t\t{self.silk_price}\t\t{self.c_s_p}")
            if self.toblerone.get()!=0:
                self.txtarea.insert(END,f"\n Toblerone\t\t{self.toblerone.get()}\t\t{self.toblerone_price}\t\t{self.c_t_p}")
            if self.kitkat.get()!=0:
                self.txtarea.insert(END,f"\n Kit Kat\t\t{self.kitkat.get()}\t\t{self.kitkat_price}\t\t{self.c_k_p}")
            if self.snicker.get()!=0:
                self.txtarea.insert(END,f"\n Snicker\t\t{self.snicker.get()}\t\t{self.snicker_price}\t\t{self.c_sr_p}")
            if self.star.get()!=0:
                self.txtarea.insert(END,f"\n 5 Star\t\t{self.star.get()}\t\t{self.star_price}\t\t{self.c_st_p}")
            if self.fuse.get()!=0:
                self.txtarea.insert(END,f"\n Fuse\t\t{self.fuse.get()}\t\t{self.fuse_price}\t\t{self.c_f_p}")
            
            self.txtarea.insert(END,f"\n-----------------------------------------------------------")
            if self.juice_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Juice Tax\t\t\t\t\t\t{self.juice_tax.get()}")
            if self.chips_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Chips Tax\t\t\t\t\t\t{self.chips_tax.get()}")
            if self.chocolate_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n chocolate Tax\t\t\t\t\t\t{self.chocolate_tax.get()}")
            
            self.txtarea.insert(END,f"\n TOTAL BILL\t\t\t\t\t\tRs. {str(self.Total_bill)}")
            self.txtarea.insert(END,f"\n-----------------------------------------------------------")
            self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("D:\\Python_code\\Python_Project\\bills"+str(self.bill.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No :{self.bill.get()} Saved Succeddfully")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("D:\\Python_code\\Python_Project\\bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"D:\\Python_code\\Python_Project\\bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill Number")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you want to clear?")
        if op>0:
            self.sprite.set(0)
            self.thumbsup.set(0)
            self.coco_cola.set(0)
            self.sveen_Up.set(0)
            self.Dukes.set(0)
            self.mirinda.set(0)

            #=====chips=====
            self.lays.set(0)
            self.doritos.set(0)
            self.pringles.set(0)
            self.peppy.set(0)
            self.kurkure.set(0)
            self.wheels.set(0)

            #=====Chocolate====
            self.silk.set(0)
            self.toblerone.set(0)
            self.kitkat.set(0)
            self.snicker.set(0)
            self.star.set(0)
            self.fuse.set(0)

            #=====Total Price=====
            self.juice_price.set("")
            self.chips_price.set("")
            self.chocolate_price.set("")

            #=======Tax price======
            self.juice_tax.set("")
            self.chips_tax.set("")
            self.chocolate_tax.set("")

            #====name of customer=====
            self.c_name.set("")
            self.c_phon.set("")
            self.bill.set("")
            a=random.randint(1000,9999)
            self.bill.set(str(a))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()
  
obj=Bill_App(root)
root.configure(bg="#87CEEB")
root.mainloop()
