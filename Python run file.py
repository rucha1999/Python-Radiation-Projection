import matplotlib.pyplot as plt
from matplotlib import style
from tkinter import *
import tkinter as tk
import pandas as pd
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

def calender():
    def delcal(top):
        name = cal.selection_get()
        selTime.set(name)
        top.destroy()

    top = tk.Toplevel(root)
    cal = Calendar(top,font="Arial 14", selectmode='day',cursor="hand1", year=2018, month=6, day=22)
    cal.grid()
    ttk.Button(top, text=" OK ",command=lambda: delcal(top)).grid()

def comparison(root):
    def proceed(comp):
        comp.destroy()
    def graph1():
        data1 = pd.read_csv('BHABHA POINT.csv')
        rad_df1= data1.iloc[0:62]
        data2 = pd.read_csv('RSMS.csv')
        rad_df2= data2.iloc[0:62]
        data3 = pd.read_csv('PRAFUL.csv')
        rad_df3= data3.iloc[0:62]
        data4 = pd.read_csv('DHRUVA.csv')
        rad_df4= data4.iloc[0:62]
        ##data5 = pd.read_csv('CIRUS.csv')
        ##rad_df5= data5.iloc[0:62]
        ax = rad_df1.plot(x='DateTime',y='RadiationLevel',label = "BHABHA POINT")
        rad_df2.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "RSMS")
        rad_df3.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "PRAFUL")
        rad_df4.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "DHRUVA")
        ##rad_df5.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "CIRUS")
        plt.xlabel('TIME - AXIS')
        plt.ylabel('RADIATION LEVEL ') 
        plt.title('Comparison radiation graph!') 
        plt.legend() 
        plt.show()
        
    def graph2():
        data1 = pd.read_csv('BHABHA POINT.csv')
        rad_df1= data1.iloc[62:122]
        data2 = pd.read_csv('RSMS.csv')
        rad_df2= data2.iloc[62:122]
        data3 = pd.read_csv('PRAFUL.csv')
        rad_df3= data3.iloc[62:122]
        data4 = pd.read_csv('DHRUVA.csv')
        rad_df4= data4.iloc[62:122]
        ##data5 = pd.read_csv('CIRUS.csv')
        ##rad_df5= data5.iloc[0:62]
        ax = rad_df1.plot(x='DateTime',y='RadiationLevel',label = "BHABHA POINT")
        rad_df2.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "RSMS")
        rad_df3.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "PRAFUL")
        rad_df4.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "DHRUVA")
        ##rad_df5.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "CIRUS")
        plt.xlabel('TIME - AXIS')
        plt.ylabel('RADIATION LEVEL ') 
        plt.title('Comparison radiation graph!') 
        plt.legend() 
        plt.show()

    def graph3():
        data1 = pd.read_csv('BHABHA POINT.csv')
        rad_df1= data1.iloc[122:182]
        data2 = pd.read_csv('RSMS.csv')
        rad_df2= data2.iloc[122:182]
        data3 = pd.read_csv('PRAFUL.csv')
        rad_df3= data3.iloc[122:182]
        data4 = pd.read_csv('DHRUVA.csv')
        rad_df4= data4.iloc[122:182]
        ##data5 = pd.read_csv('CIRUS.csv')
        ##rad_df5= data5.iloc[0:62]
        ax = rad_df1.plot(x='DateTime',y='RadiationLevel',label = "BHABHA POINT")
        rad_df2.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "RSMS")
        rad_df3.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "PRAFUL")
        rad_df4.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "DHRUVA")
        ##rad_df5.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "CIRUS")
        plt.xlabel('TIME - AXIS')
        plt.ylabel('RADIATION LEVEL ') 
        plt.title('Comparison radiation graph!') 
        plt.legend() 
        plt.show()

        

    def graph4():
        data1 = pd.read_csv('BHABHA POINT.csv')
        rad_df1= data1.iloc[182:242]
        data2 = pd.read_csv('RSMS.csv')
        rad_df2= data2.iloc[182:242]
        data3 = pd.read_csv('PRAFUL.csv')
        rad_df3= data3.iloc[182:242]
        data4 = pd.read_csv('DHRUVA.csv')
        rad_df4= data4.iloc[182:242]
        ##data5 = pd.read_csv('CIRUS.csv')
        ##rad_df5= data5.iloc[0:62]
        ax = rad_df1.plot(x='DateTime',y='RadiationLevel',label = "BHABHA POINT")
        rad_df2.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "RSMS")
        rad_df3.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "PRAFUL")
        rad_df4.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "DHRUVA")
        ##rad_df5.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "CIRUS")
        plt.xlabel('TIME - AXIS')
        plt.ylabel('RADIATION LEVEL ') 
        plt.title('Comparison radiation graph!') 
        plt.legend() 
        plt.show()

    def graph5():
        data1 = pd.read_csv('BHABHA POINT.csv')
        rad_df1= data1.iloc[242:302]
        data2 = pd.read_csv('RSMS.csv')
        rad_df2= data2.iloc[242:302]
        data3 = pd.read_csv('PRAFUL.csv')
        rad_df3= data3.iloc[242:302]
        data4 = pd.read_csv('DHRUVA.csv')
        rad_df4= data4.iloc[242:302]
        ##data5 = pd.read_csv('CIRUS.csv')
        ##rad_df5= data5.iloc[0:62]
        ax = rad_df1.plot(x='DateTime',y='RadiationLevel',label = "BHABHA POINT")
        rad_df2.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "RSMS")
        rad_df3.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "PRAFUL")
        rad_df4.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "DHRUVA")
        ##rad_df5.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "CIRUS")
        plt.xlabel('TIME - AXIS')
        plt.ylabel('RADIATION LEVEL ') 
        plt.title('Comparison radiation graph!') 
        plt.legend() 
        plt.show()

    def graph6():
        data1 = pd.read_csv('BHABHA POINT.csv')
        rad_df1= data1.iloc[302:362]
        data2 = pd.read_csv('RSMS.csv')
        rad_df2= data2.iloc[302:362]
        data3 = pd.read_csv('PRAFUL.csv')
        rad_df3= data3.iloc[302:362]
        data4 = pd.read_csv('DHRUVA.csv')
        rad_df4= data4.iloc[302:362]
        ##data5 = pd.read_csv('CIRUS.csv')
        ##rad_df5= data5.iloc[0:62]
        ax = rad_df1.plot(x='DateTime',y='RadiationLevel',label = "BHABHA POINT")
        rad_df2.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "RSMS")
        rad_df3.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "PRAFUL")
        rad_df4.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "DHRUVA")
        ##rad_df5.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "CIRUS")
        plt.xlabel('TIME - AXIS')
        plt.ylabel('RADIATION LEVEL ') 
        plt.title('Comparison radiation graph!') 
        plt.legend() 
        plt.show()

    def graph7():
        data1 = pd.read_csv('BHABHA POINT.csv')
        rad_df1= data1.iloc[362:422]
        data2 = pd.read_csv('RSMS.csv')
        rad_df2= data2.iloc[362:422]
        data3 = pd.read_csv('PRAFUL.csv')
        rad_df3= data3.iloc[362:422]
        data4 = pd.read_csv('DHRUVA.csv')
        rad_df4= data4.iloc[362:422]
        ##data5 = pd.read_csv('CIRUS.csv')
        ##rad_df5= data5.iloc[0:62]
        ax = rad_df1.plot(x='DateTime',y='RadiationLevel',label = "BHABHA POINT")
        rad_df2.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "RSMS")
        rad_df3.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "PRAFUL")
        rad_df4.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "DHRUVA")
        ##rad_df5.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "CIRUS")
        plt.xlabel('TIME - AXIS')
        plt.ylabel('RADIATION LEVEL ') 
        plt.title('Comparison radiation graph!') 
        plt.legend() 
        plt.show()

    def graph8():
        data1 = pd.read_csv('BHABHA POINT.csv')
        rad_df1= data1.iloc[422:482]
        data2 = pd.read_csv('RSMS.csv')
        rad_df2= data2.iloc[422:482]
        data3 = pd.read_csv('PRAFUL.csv')
        rad_df3= data3.iloc[422:482]
        data4 = pd.read_csv('DHRUVA.csv')
        rad_df4= data4.iloc[422:482]
        ##data5 = pd.read_csv('CIRUS.csv')
        ##rad_df5= data5.iloc[0:62]
        ax = rad_df1.plot(x='DateTime',y='RadiationLevel',label = "BHABHA POINT")
        rad_df2.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "RSMS")
        rad_df3.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "PRAFUL")
        rad_df4.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "DHRUVA")
        ##rad_df5.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "CIRUS")
        plt.xlabel('TIME - AXIS')
        plt.ylabel('RADIATION LEVEL ') 
        plt.title('Comparison radiation graph!') 
        plt.legend() 
        plt.show()

    def graph9():
        data1 = pd.read_csv('BHABHA POINT.csv')
        rad_df1= data1.iloc[482:542]
        data2 = pd.read_csv('RSMS.csv')
        rad_df2= data2.iloc[482:542]
        data3 = pd.read_csv('PRAFUL.csv')
        rad_df3= data3.iloc[482:542]
        data4 = pd.read_csv('DHRUVA.csv')
        rad_df4= data4.iloc[482:542]
        ##data5 = pd.read_csv('CIRUS.csv')
        ##rad_df5= data5.iloc[0:62]
        ax = rad_df1.plot(x='DateTime',y='RadiationLevel',label = "BHABHA POINT")
        rad_df2.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "RSMS")
        rad_df3.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "PRAFUL")
        rad_df4.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "DHRUVA")
        ##rad_df5.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "CIRUS")
        plt.xlabel('TIME - AXIS')
        plt.ylabel('RADIATION LEVEL ') 
        plt.title('Comparison radiation graph!') 
        plt.legend() 
        plt.show()

    def graph10():
        data1 = pd.read_csv('BHABHA POINT.csv')
        rad_df1= data1.iloc[542:602]
        data2 = pd.read_csv('RSMS.csv')
        rad_df2= data2.iloc[542:602]
        data3 = pd.read_csv('PRAFUL.csv')
        rad_df3= data3.iloc[542:602]
        data4 = pd.read_csv('DHRUVA.csv')
        rad_df4= data4.iloc[542:602]
        ##data5 = pd.read_csv('CIRUS.csv')
        ##rad_df5= data5.iloc[0:62]
        ax = rad_df1.plot(x='DateTime',y='RadiationLevel',label = "BHABHA POINT")
        rad_df2.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "RSMS")
        rad_df3.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "PRAFUL")
        rad_df4.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "DHRUVA")
        ##rad_df5.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "CIRUS")
        plt.xlabel('TIME - AXIS')
        plt.ylabel('RADIATION LEVEL ') 
        plt.title('Comparison radiation graph!') 
        plt.legend() 
        plt.show()

    def graph11():
        data1 = pd.read_csv('BHABHA POINT.csv')
        rad_df1= data1.iloc[602:662]
        data2 = pd.read_csv('RSMS.csv')
        rad_df2= data2.iloc[602:662]
        data3 = pd.read_csv('PRAFUL.csv')
        rad_df3= data3.iloc[602:662]
        data4 = pd.read_csv('DHRUVA.csv')
        rad_df4= data4.iloc[602:662]
        ##data5 = pd.read_csv('CIRUS.csv')
        ##rad_df5= data5.iloc[0:62]
        ax = rad_df1.plot(x='DateTime',y='RadiationLevel',label = "BHABHA POINT")
        rad_df2.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "RSMS")
        rad_df3.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "PRAFUL")
        rad_df4.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "DHRUVA")
        ##rad_df5.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "CIRUS")
        plt.xlabel('TIME - AXIS')
        plt.ylabel('RADIATION LEVEL ') 
        plt.title('Comparison radiation graph!') 
        plt.legend() 
        plt.show()

    def graph12():
        data1 = pd.read_csv('BHABHA POINT.csv')
        rad_df1= data1.iloc[662:721]
        data2 = pd.read_csv('RSMS.csv')
        rad_df2= data2.iloc[662:721]
        data3 = pd.read_csv('PRAFUL.csv')
        rad_df3= data3.iloc[662:721]
        data4 = pd.read_csv('DHRUVA.csv')
        rad_df4= data4.iloc[662:721]
        ##data5 = pd.read_csv('CIRUS.csv')
        ##rad_df5= data5.iloc[0:62]
        ax = rad_df1.plot(x='DateTime',y='RadiationLevel',label = "BHABHA POINT")
        rad_df2.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "RSMS")
        rad_df3.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "PRAFUL")
        rad_df4.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "DHRUVA")
        ##rad_df5.plot(ax=ax,x='DateTime',y='RadiationLevel',label = "CIRUS")
        plt.xlabel('TIME - AXIS')
        plt.ylabel('RADIATION LEVEL ') 
        plt.title('Comparison radiation graph!') 
        plt.legend() 
        plt.show()
        
    comp = tk.Toplevel(root)
    comp.geometry("450x600")
    comp.title("COMPARISON")
    comp.configure(background='light green')
    L1=Label(comp,text='SELECTED LOCATION FOR COMPARISON ARE:',bg='light green',font="Arial 14")
    L1.grid(row=1,column=0,padx=5 ,pady=5)
    L2=Label(comp,text='BHABHA POINT , RSMS , PRAFUL , DHRUVA ',bg='light green',fg='blue',font="Arial 12")
    L2.grid(row=2,column=0,padx=5 ,pady=5)
    Label(comp,text=' SELECT THE TIME :',bg='light green',font="Arial 14").grid(row=3,column=0,pady=5,sticky=W)
    B1=Button(comp,text="00:00:00 to 2:00:00",bg='light blue',command=lambda: graph1())
    B1.grid(pady=5)
    B2=Button(comp,text="2:00:00 to 4:00:00",bg='light blue',command=lambda: graph2())
    B2.grid(pady=5)
    B3=Button(comp,text="4:00:00 to 6:00:00",bg='light blue',command=lambda: graph3())
    B3.grid(pady=5)
    B4=Button(comp,text="6:00:00 to 8:00:00",bg='light blue',command=lambda: graph4())
    B4.grid(pady=5)
    B5=Button(comp,text="8:00:00 to 10:00:00",bg='light blue',command=lambda: graph5())
    B5.grid(pady=5)
    B6=Button(comp,text="10:00:00 to 12:00:00",bg='light blue',command=lambda: graph6())
    B6.grid(pady=5)
    B7=Button(comp,text="12:00:00 to 14:00:00",bg='light blue',command=lambda: graph7())
    B7.grid(pady=5)
    B8=Button(comp,text="14:00:00 to 16:00:00",bg='light blue',command=lambda: graph8())
    B8.grid(pady=5)
    B9=Button(comp,text="16:00:00 to 18:00:00",bg='light blue',command=lambda: graph9())
    B9.grid(pady=5)
    B10=Button(comp,text="18:00:00 to 20:00:00",bg='light blue',command=lambda: graph10())
    B10.grid(pady=5)
    B11=Button(comp,text="20:00:00 to 22:00:00",bg='light blue',command=lambda: graph11())
    B11.grid(pady=5)
    B12=Button(comp,text="22:00:00 to 23:59:00",bg='light blue',command=lambda: graph12())
    B12.grid(pady=5)
    Button(comp, text=" EXIT ",bg='light blue',font="Arial 12",command=lambda: proceed(comp)).grid(padx=15,pady=10)
    comp.mainloop()
    
def individual(root):
    def changename(index):
        name = mb.menu.entrycget(index, "label")
        selectedText.set(name)
        mb.grid(row=1, column=1)
        create_window(index)

    def destroy(top):
        top.destroy()
        
    def create_window(index):
        window = tk.Toplevel(master)
        window.geometry("200x510")
        window.configure(background='light green')
        Label(window,text=' SELECT THE TIME :',bg='light green',font="Arial 14").grid(row=1,column=0,pady=5)
        B1=Button(window,text="00:00:00 to 2:00:00",command=lambda: graph1(index))
        B1.grid(pady=5)
        B2=Button(window,text="2:00:00 to 4:00:00",command=lambda: graph2(index))
        B2.grid(pady=5)
        B3=Button(window,text="4:00:00 to 6:00:00",command=lambda: graph3(index))
        B3.grid(pady=5)
        B4=Button(window,text="6:00:00 to 8:00:00",command=lambda: graph4(index))
        B4.grid(pady=5)
        B5=Button(window,text="8:00:00 to 10:00:00",command=lambda: graph5(index))
        B5.grid(pady=5)
        B6=Button(window,text="10:00:00 to 12:00:00",command=lambda: graph6(index))
        B6.grid(pady=5)
        B7=Button(window,text="12:00:00 to 14:00:00",command=lambda: graph7(index))
        B7.grid(pady=5)
        B8=Button(window,text="14:00:00 to 16:00:00",command=lambda: graph8(index))
        B8.grid(pady=5)
        B9=Button(window,text="16:00:00 to 18:00:00",command=lambda: graph9(index))
        B9.grid(pady=5)
        B10=Button(window,text="18:00:00 to 20:00:00",command=lambda: graph10(index))
        B10.grid(pady=5)
        B11=Button(window,text="20:00:00 to 22:00:00",command=lambda: graph11(index))
        B11.grid(pady=5)
        B12=Button(window,text="22:00:00 to 23:59:00",command=lambda: graph12(index))
        B12.grid(pady=5)
        B13=Button(window,text="WHOLE DAY",command=lambda: graph13(index))
        B13.grid(pady=5)

    def graph1(index):
        answer1="NG(OUT)"
        answer2="NG(IN)"
        answer3="CC SECURITY"
        answer4="ML(H)"
        answer5="ML(S)"
        answer6="CIRUS JETTY"
        answer7="COMP SECURITY"
        answer8="HALL#7"
        answer9="BHABHA POINT"
        answer10="RLG MAIN GATE"
        answer11="RLG BACK GATE"
        answer12="WIP PORTICO"
        answer13="RSMS"
        answer14="PP SECURITY"
        answer15="SOUTH GATE"
        answer16="PRAFUL"
        answer17="IF3"
        answer18="RUMP"
        answer19="DHRUVA"
        answer20="CIRUS"
        answer21="ETP"
        answer22="LAUNDRY"
        if index==answer1:
            data = pd.read_csv('NG(OUT).csv')
        elif index==answer2:
            data = pd.read_csv('NG(IN).csv')
        elif index==answer3:
            data = pd.read_csv('CC SECURITY.csv')
        elif index==answer4:
            data = pd.read_csv('ML(H).csv')
        elif index==answer5:
            data = pd.read_csv('ML(S).csv')
        elif index==answer6:
            data = pd.read_csv('CIRUS JETTY.csv')
        elif index==answer7:
            data = pd.read_csv('COMP SECURITY.csv')
        elif index==answer8:
            data = pd.read_csv('HALL#7.csv')
        elif index==answer9:
            data = pd.read_csv('BHABHA POINT.csv')
        elif index==answer10:
            data = pd.read_csv('RLG MAIN GATE.csv')
        elif index==answer11:
            data = pd.read_csv('RLG BACK GATE.csv')
        elif index==answer12:
            data = pd.read_csv('WIP PORTICO.csv')
        elif index==answer13:
            data = pd.read_csv('RSMS.csv')
        elif index==answer14:
            data = pd.read_csv('PP SECURITY.csv')
        elif index==answer15:
            data = pd.read_csv('SOUTH GATE.csv')
        elif index==answer16:
            data = pd.read_csv('PRAFUL.csv')
        elif index==answer17:
            data = pd.read_csv('IF3.csv')
        elif index==answer13:
            data = pd.read_csv('RUMP.csv')
        elif index==answer19:
            data = pd.read_csv('DHRUVA.csv')
        elif index==answer20:
            data = pd.read_csv('CIRUS.csv')
        elif index==answer21:
            data = pd.read_csv('ETP.csv')
        elif index==answer22:
            data = pd.read_csv('LAUNDRY.csv')



        rad_df1= data.iloc[0:62]
        rad_df1.plot(kind='bar',x='DateTime',y='RadiationLevel')
        plt.title('Radiation Graph')
        plt.show()
    
    def graph2(index):
        answer1="NG(OUT)"
        answer2="NG(IN)"
        answer3="CC SECURITY"
        answer4="ML(H)"
        answer5="ML(S)"
        answer6="CIRUS JETTY"
        answer7="COMP SECURITY"
        answer8="HALL#7"
        answer9="BHABHA POINT"
        answer10="RLG MAIN GATE"
        answer11="RLG BACK GATE"
        answer12="WIP PORTICO"
        answer13="RSMS"
        answer14="PP SECURITY"
        answer15="SOUTH GATE"
        answer16="PRAFUL"
        answer17="IF3"
        answer18="RUMP"
        answer19="DHRUVA"
        answer20="CIRUS"
        answer21="ETP"
        answer22="LAUNDRY"
        if index==answer1:
            data = pd.read_csv('NG(OUT).csv')
        elif index==answer2:
            data = pd.read_csv('NG(IN).csv')
        elif index==answer3:
            data = pd.read_csv('CC SECURITY.csv')
        elif index==answer4:
            data = pd.read_csv('ML(H).csv')
        elif index==answer5:
            data = pd.read_csv('ML(S).csv')
        elif index==answer6:
            data = pd.read_csv('CIRUS JETTY.csv')
        elif index==answer7:
            data = pd.read_csv('COMP SECURITY.csv')
        elif index==answer8:
            data = pd.read_csv('HALL#7.csv')
        elif index==answer9:
            data = pd.read_csv('BHABHA POINT.csv')
        elif index==answer10:
            data = pd.read_csv('RLG MAIN GATE.csv')
        elif index==answer11:
            data = pd.read_csv('RLG BACK GATE.csv')
        elif index==answer12:
            data = pd.read_csv('WIP PORTICO.csv')
        elif index==answer13:
            data = pd.read_csv('RSMS.csv')
        elif index==answer14:
            data = pd.read_csv('PP SECURITY.csv')
        elif index==answer15:
            data = pd.read_csv('SOUTH GATE.csv')
        elif index==answer16:
            data = pd.read_csv('PRAFUL.csv')
        elif index==answer17:
            data = pd.read_csv('IF3.csv')
        elif index==answer13:
            data = pd.read_csv('RUMP.csv')
        elif index==answer19:
            data = pd.read_csv('DHRUVA.csv')
        elif index==answer20:
            data = pd.read_csv('CIRUS.csv')
        elif index==answer21:
            data = pd.read_csv('ETP.csv')
        elif index==answer22:
            data = pd.read_csv('LAUNDRY.csv')

        rad_df1= data.iloc[62:122]
        rad_df1.plot(kind='bar',x='DateTime',y='RadiationLevel')
        plt.title('Radiation Graph')
        plt.show()

    def graph3(index):
        answer1="NG(OUT)"
        answer2="NG(IN)"
        answer3="CC SECURITY"
        answer4="ML(H)"
        answer5="ML(S)"
        answer6="CIRUS JETTY"
        answer7="COMP SECURITY"
        answer8="HALL#7"
        answer9="BHABHA POINT"
        answer10="RLG MAIN GATE"
        answer11="RLG BACK GATE"
        answer12="WIP PORTICO"
        answer13="RSMS"
        answer14="PP SECURITY"
        answer15="SOUTH GATE"
        answer16="PRAFUL"
        answer17="IF3"
        answer18="RUMP"
        answer19="DHRUVA"
        answer20="CIRUS"
        answer21="ETP"
        answer22="LAUNDRY"
        if index==answer1:
            data = pd.read_csv('NG(OUT).csv')
        elif index==answer2:
            data = pd.read_csv('NG(IN).csv')
        elif index==answer3:
            data = pd.read_csv('CC SECURITY.csv')
        elif index==answer4:
            data = pd.read_csv('ML(H).csv')
        elif index==answer5:
            data = pd.read_csv('ML(S).csv')
        elif index==answer6:
            data = pd.read_csv('CIRUS JETTY.csv')
        elif index==answer7:
            data = pd.read_csv('COMP SECURITY.csv')
        elif index==answer8:
            data = pd.read_csv('HALL#7.csv')
        elif index==answer9:
            data = pd.read_csv('BHABHA POINT.csv')
        elif index==answer10:
            data = pd.read_csv('RLG MAIN GATE.csv')
        elif index==answer11:
            data = pd.read_csv('RLG BACK GATE.csv')
        elif index==answer12:
            data = pd.read_csv('WIP PORTICO.csv')
        elif index==answer13:
            data = pd.read_csv('RSMS.csv')
        elif index==answer14:
            data = pd.read_csv('PP SECURITY.csv')
        elif index==answer15:
            data = pd.read_csv('SOUTH GATE.csv')
        elif index==answer16:
            data = pd.read_csv('PRAFUL.csv')
        elif index==answer17:
            data = pd.read_csv('IF3.csv')
        elif index==answer13:
            data = pd.read_csv('RUMP.csv')
        elif index==answer19:
            data = pd.read_csv('DHRUVA.csv')
        elif index==answer20:
            data = pd.read_csv('CIRUS.csv')
        elif index==answer21:
            data = pd.read_csv('ETP.csv')
        elif index==answer22:
            data = pd.read_csv('LAUNDRY.csv')



        rad_df1= data.iloc[122:182]
        rad_df1.plot(kind='bar',x='DateTime',y='RadiationLevel')
        plt.title('Radiation Graph')
        plt.show()

    def graph4(index):
        answer1="NG(OUT)"
        answer2="NG(IN)"
        answer3="CC SECURITY"
        answer4="ML(H)"
        answer5="ML(S)"
        answer6="CIRUS JETTY"
        answer7="COMP SECURITY"
        answer8="HALL#7"
        answer9="BHABHA POINT"
        answer10="RLG MAIN GATE"
        answer11="RLG BACK GATE"
        answer12="WIP PORTICO"
        answer13="RSMS"
        answer14="PP SECURITY"
        answer15="SOUTH GATE"
        answer16="PRAFUL"
        answer17="IF3"
        answer18="RUMP"
        answer19="DHRUVA"
        answer20="CIRUS"
        answer21="ETP"
        answer22="LAUNDRY"
        if index==answer1:
            data = pd.read_csv('NG(OUT).csv')
        elif index==answer2:
            data = pd.read_csv('NG(IN).csv')
        elif index==answer3:
            data = pd.read_csv('CC SECURITY.csv')
        elif index==answer4:
            data = pd.read_csv('ML(H).csv')
        elif index==answer5:
            data = pd.read_csv('ML(S).csv')
        elif index==answer6:
            data = pd.read_csv('CIRUS JETTY.csv')
        elif index==answer7:
            data = pd.read_csv('COMP SECURITY.csv')
        elif index==answer8:
            data = pd.read_csv('HALL#7.csv')
        elif index==answer9:
            data = pd.read_csv('BHABHA POINT.csv')
        elif index==answer10:
            data = pd.read_csv('RLG MAIN GATE.csv')
        elif index==answer11:
            data = pd.read_csv('RLG BACK GATE.csv')
        elif index==answer12:
            data = pd.read_csv('WIP PORTICO.csv')
        elif index==answer13:
            data = pd.read_csv('RSMS.csv')
        elif index==answer14:
            data = pd.read_csv('PP SECURITY.csv')
        elif index==answer15:
            data = pd.read_csv('SOUTH GATE.csv')
        elif index==answer16:
            data = pd.read_csv('PRAFUL.csv')
        elif index==answer17:
            data = pd.read_csv('IF3.csv')
        elif index==answer13:
            data = pd.read_csv('RUMP.csv')
        elif index==answer19:
            data = pd.read_csv('DHRUVA.csv')
        elif index==answer20:
            data = pd.read_csv('CIRUS.csv')
        elif index==answer21:
            data = pd.read_csv('ETP.csv')
        elif index==answer22:
            data = pd.read_csv('LAUNDRY.csv')



        rad_df1= data.iloc[182:242]
        rad_df1.plot(kind='bar',x='DateTime',y='RadiationLevel')
        plt.title('Radiation Graph')
        plt.show()

    def graph5(index):
        answer1="NG(OUT)"
        answer2="NG(IN)"
        answer3="CC SECURITY"
        answer4="ML(H)"
        answer5="ML(S)"
        answer6="CIRUS JETTY"
        answer7="COMP SECURITY"
        answer8="HALL#7"
        answer9="BHABHA POINT"
        answer10="RLG MAIN GATE"
        answer11="RLG BACK GATE"
        answer12="WIP PORTICO"
        answer13="RSMS"
        answer14="PP SECURITY"
        answer15="SOUTH GATE"
        answer16="PRAFUL"
        answer17="IF3"
        answer18="RUMP"
        answer19="DHRUVA"
        answer20="CIRUS"
        answer21="ETP"
        answer22="LAUNDRY"
        if index==answer1:
            data = pd.read_csv('NG(OUT).csv')
        elif index==answer2:
            data = pd.read_csv('NG(IN).csv')
        elif index==answer3:
            data = pd.read_csv('CC SECURITY.csv')
        elif index==answer4:
            data = pd.read_csv('ML(H).csv')
        elif index==answer5:
            data = pd.read_csv('ML(S).csv')
        elif index==answer6:
            data = pd.read_csv('CIRUS JETTY.csv')
        elif index==answer7:
            data = pd.read_csv('COMP SECURITY.csv')
        elif index==answer8:
            data = pd.read_csv('HALL#7.csv')
        elif index==answer9:
            data = pd.read_csv('BHABHA POINT.csv')
        elif index==answer10:
            data = pd.read_csv('RLG MAIN GATE.csv')
        elif index==answer11:
            data = pd.read_csv('RLG BACK GATE.csv')
        elif index==answer12:
            data = pd.read_csv('WIP PORTICO.csv')
        elif index==answer13:
            data = pd.read_csv('RSMS.csv')
        elif index==answer14:
            data = pd.read_csv('PP SECURITY.csv')
        elif index==answer15:
            data = pd.read_csv('SOUTH GATE.csv')
        elif index==answer16:
            data = pd.read_csv('PRAFUL.csv')
        elif index==answer17:
            data = pd.read_csv('IF3.csv')
        elif index==answer13:
            data = pd.read_csv('RUMP.csv')
        elif index==answer19:
            data = pd.read_csv('DHRUVA.csv')
        elif index==answer20:
            data = pd.read_csv('CIRUS.csv')
        elif index==answer21:
            data = pd.read_csv('ETP.csv')
        elif index==answer22:
            data = pd.read_csv('LAUNDRY.csv')


        rad_df1= data.iloc[242:302]
        rad_df1.plot(kind='bar',x='DateTime',y='RadiationLevel')
        plt.title('Radiation Graph')
        plt.show()        

    def graph6(index):
        answer1="NG(OUT)"
        answer2="NG(IN)"
        answer3="CC SECURITY"
        answer4="ML(H)"
        answer5="ML(S)"
        answer6="CIRUS JETTY"
        answer7="COMP SECURITY"
        answer8="HALL#7"
        answer9="BHABHA POINT"
        answer10="RLG MAIN GATE"
        answer11="RLG BACK GATE"
        answer12="WIP PORTICO"
        answer13="RSMS"
        answer14="PP SECURITY"
        answer15="SOUTH GATE"
        answer16="PRAFUL"
        answer17="IF3"
        answer18="RUMP"
        answer19="DHRUVA"
        answer20="CIRUS"
        answer21="ETP"
        answer22="LAUNDRY"
        if index==answer1:
            data = pd.read_csv('NG(OUT).csv')
        elif index==answer2:
            data = pd.read_csv('NG(IN).csv')
        elif index==answer3:
            data = pd.read_csv('CC SECURITY.csv')
        elif index==answer4:
            data = pd.read_csv('ML(H).csv')
        elif index==answer5:
            data = pd.read_csv('ML(S).csv')
        elif index==answer6:
            data = pd.read_csv('CIRUS JETTY.csv')
        elif index==answer7:
            data = pd.read_csv('COMP SECURITY.csv')
        elif index==answer8:
            data = pd.read_csv('HALL#7.csv')
        elif index==answer9:
            data = pd.read_csv('BHABHA POINT.csv')
        elif index==answer10:
            data = pd.read_csv('RLG MAIN GATE.csv')
        elif index==answer11:
            data = pd.read_csv('RLG BACK GATE.csv')
        elif index==answer12:
            data = pd.read_csv('WIP PORTICO.csv')
        elif index==answer13:
            data = pd.read_csv('RSMS.csv')
        elif index==answer14:
            data = pd.read_csv('PP SECURITY.csv')
        elif index==answer15:
            data = pd.read_csv('SOUTH GATE.csv')
        elif index==answer16:
            data = pd.read_csv('PRAFUL.csv')
        elif index==answer17:
            data = pd.read_csv('IF3.csv')
        elif index==answer13:
            data = pd.read_csv('RUMP.csv')
        elif index==answer19:
            data = pd.read_csv('DHRUVA.csv')
        elif index==answer20:
            data = pd.read_csv('CIRUS.csv')
        elif index==answer21:
            data = pd.read_csv('ETP.csv')
        elif index==answer22:
            data = pd.read_csv('LAUNDRY.csv')


        rad_df1= data.iloc[302:362]
        rad_df1.plot(kind='bar',x='DateTime',y='RadiationLevel')
        plt.title('Radiation Graph')
        plt.show()

    def graph7(index):
        answer1="NG(OUT)"
        answer2="NG(IN)"
        answer3="CC SECURITY"
        answer4="ML(H)"
        answer5="ML(S)"
        answer6="CIRUS JETTY"
        answer7="COMP SECURITY"
        answer8="HALL#7"
        answer9="BHABHA POINT"
        answer10="RLG MAIN GATE"
        answer11="RLG BACK GATE"
        answer12="WIP PORTICO"
        answer13="RSMS"
        answer14="PP SECURITY"
        answer15="SOUTH GATE"
        answer16="PRAFUL"
        answer17="IF3"
        answer18="RUMP"
        answer19="DHRUVA"
        answer20="CIRUS"
        answer21="ETP"
        answer22="LAUNDRY"
        if index==answer1:
            data = pd.read_csv('NG(OUT).csv')
        elif index==answer2:
            data = pd.read_csv('NG(IN).csv')
        elif index==answer3:
            data = pd.read_csv('CC SECURITY.csv')
        elif index==answer4:
            data = pd.read_csv('ML(H).csv')
        elif index==answer5:
            data = pd.read_csv('ML(S).csv')
        elif index==answer6:
            data = pd.read_csv('CIRUS JETTY.csv')
        elif index==answer7:
            data = pd.read_csv('COMP SECURITY.csv')
        elif index==answer8:
            data = pd.read_csv('HALL#7.csv')
        elif index==answer9:
            data = pd.read_csv('BHABHA POINT.csv')
        elif index==answer10:
            data = pd.read_csv('RLG MAIN GATE.csv')
        elif index==answer11:
            data = pd.read_csv('RLG BACK GATE.csv')
        elif index==answer12:
            data = pd.read_csv('WIP PORTICO.csv')
        elif index==answer13:
            data = pd.read_csv('RSMS.csv')
        elif index==answer14:
            data = pd.read_csv('PP SECURITY.csv')
        elif index==answer15:
            data = pd.read_csv('SOUTH GATE.csv')
        elif index==answer16:
            data = pd.read_csv('PRAFUL.csv')
        elif index==answer17:
            data = pd.read_csv('IF3.csv')
        elif index==answer13:
            data = pd.read_csv('RUMP.csv')
        elif index==answer19:
            data = pd.read_csv('DHRUVA.csv')
        elif index==answer20:
            data = pd.read_csv('CIRUS.csv')
        elif index==answer21:
            data = pd.read_csv('ETP.csv')
        elif index==answer22:
            data = pd.read_csv('LAUNDRY.csv')



        rad_df1= data.iloc[362:422]
        rad_df1.plot(kind='bar',x='DateTime',y='RadiationLevel')
        plt.title('Radiation Graph')
        plt.show()

    def graph8(index):
        answer1="NG(OUT)"
        answer2="NG(IN)"
        answer3="CC SECURITY"
        answer4="ML(H)"
        answer5="ML(S)"
        answer6="CIRUS JETTY"
        answer7="COMP SECURITY"
        answer8="HALL#7"
        answer9="BHABHA POINT"
        answer10="RLG MAIN GATE"
        answer11="RLG BACK GATE"
        answer12="WIP PORTICO"
        answer13="RSMS"
        answer14="PP SECURITY"
        answer15="SOUTH GATE"
        answer16="PRAFUL"
        answer17="IF3"
        answer18="RUMP"
        answer19="DHRUVA"
        answer20="CIRUS"
        answer21="ETP"
        answer22="LAUNDRY"
        if index==answer1:
            data = pd.read_csv('NG(OUT).csv')
        elif index==answer2:
            data = pd.read_csv('NG(IN).csv')
        elif index==answer3:
            data = pd.read_csv('CC SECURITY.csv')
        elif index==answer4:
            data = pd.read_csv('ML(H).csv')
        elif index==answer5:
            data = pd.read_csv('ML(S).csv')
        elif index==answer6:
            data = pd.read_csv('CIRUS JETTY.csv')
        elif index==answer7:
            data = pd.read_csv('COMP SECURITY.csv')
        elif index==answer8:
            data = pd.read_csv('HALL#7.csv')
        elif index==answer9:
            data = pd.read_csv('BHABHA POINT.csv')
        elif index==answer10:
            data = pd.read_csv('RLG MAIN GATE.csv')
        elif index==answer11:
            data = pd.read_csv('RLG BACK GATE.csv')
        elif index==answer12:
            data = pd.read_csv('WIP PORTICO.csv')
        elif index==answer13:
            data = pd.read_csv('RSMS.csv')
        elif index==answer14:
            data = pd.read_csv('PP SECURITY.csv')
        elif index==answer15:
            data = pd.read_csv('SOUTH GATE.csv')
        elif index==answer16:
            data = pd.read_csv('PRAFUL.csv')
        elif index==answer17:
            data = pd.read_csv('IF3.csv')
        elif index==answer13:
            data = pd.read_csv('RUMP.csv')
        elif index==answer19:
            data = pd.read_csv('DHRUVA.csv')
        elif index==answer20:
            data = pd.read_csv('CIRUS.csv')
        elif index==answer21:
            data = pd.read_csv('ETP.csv')
        elif index==answer22:
            data = pd.read_csv('LAUNDRY.csv')


        rad_df1= data.iloc[422:482]
        rad_df1.plot(kind='bar',x='DateTime',y='RadiationLevel')
        plt.title('Radiation Graph')
        plt.show()

    def graph9(index):
        answer1="NG(OUT)"
        answer2="NG(IN)"
        answer3="CC SECURITY"
        answer4="ML(H)"
        answer5="ML(S)"
        answer6="CIRUS JETTY"
        answer7="COMP SECURITY"
        answer8="HALL#7"
        answer9="BHABHA POINT"
        answer10="RLG MAIN GATE"
        answer11="RLG BACK GATE"
        answer12="WIP PORTICO"
        answer13="RSMS"
        answer14="PP SECURITY"
        answer15="SOUTH GATE"
        answer16="PRAFUL"
        answer17="IF3"
        answer18="RUMP"
        answer19="DHRUVA"
        answer20="CIRUS"
        answer21="ETP"
        answer22="LAUNDRY"
        if index==answer1:
            data = pd.read_csv('NG(OUT).csv')
        elif index==answer2:
            data = pd.read_csv('NG(IN).csv')
        elif index==answer3:
            data = pd.read_csv('CC SECURITY.csv')
        elif index==answer4:
            data = pd.read_csv('ML(H).csv')
        elif index==answer5:
            data = pd.read_csv('ML(S).csv')
        elif index==answer6:
            data = pd.read_csv('CIRUS JETTY.csv')
        elif index==answer7:
            data = pd.read_csv('COMP SECURITY.csv')
        elif index==answer8:
            data = pd.read_csv('HALL#7.csv')
        elif index==answer9:
            data = pd.read_csv('BHABHA POINT.csv')
        elif index==answer10:
            data = pd.read_csv('RLG MAIN GATE.csv')
        elif index==answer11:
            data = pd.read_csv('RLG BACK GATE.csv')
        elif index==answer12:
            data = pd.read_csv('WIP PORTICO.csv')
        elif index==answer13:
            data = pd.read_csv('RSMS.csv')
        elif index==answer14:
            data = pd.read_csv('PP SECURITY.csv')
        elif index==answer15:
            data = pd.read_csv('SOUTH GATE.csv')
        elif index==answer16:
            data = pd.read_csv('PRAFUL.csv')
        elif index==answer17:
            data = pd.read_csv('IF3.csv')
        elif index==answer13:
            data = pd.read_csv('RUMP.csv')
        elif index==answer19:
            data = pd.read_csv('DHRUVA.csv')
        elif index==answer20:
            data = pd.read_csv('CIRUS.csv')
        elif index==answer21:
            data = pd.read_csv('ETP.csv')
        elif index==answer22:
            data = pd.read_csv('LAUNDRY.csv')



        rad_df1= data.iloc[482:542]
        rad_df1.plot(kind='bar',x='DateTime',y='RadiationLevel')
        plt.title('Radiation Graph')
        plt.show()


    def graph10(index):
        answer1="NG(OUT)"
        answer2="NG(IN)"
        answer3="CC SECURITY"
        answer4="ML(H)"
        answer5="ML(S)"
        answer6="CIRUS JETTY"
        answer7="COMP SECURITY"
        answer8="HALL#7"
        answer9="BHABHA POINT"
        answer10="RLG MAIN GATE"
        answer11="RLG BACK GATE"
        answer12="WIP PORTICO"
        answer13="RSMS"
        answer14="PP SECURITY"
        answer15="SOUTH GATE"
        answer16="PRAFUL"
        answer17="IF3"
        answer18="RUMP"
        answer19="DHRUVA"
        answer20="CIRUS"
        answer21="ETP"
        answer22="LAUNDRY"
        if index==answer1:
            data = pd.read_csv('NG(OUT).csv')
        elif index==answer2:
            data = pd.read_csv('NG(IN).csv')
        elif index==answer3:
            data = pd.read_csv('CC SECURITY.csv')
        elif index==answer4:
            data = pd.read_csv('ML(H).csv')
        elif index==answer5:
            data = pd.read_csv('ML(S).csv')
        elif index==answer6:
            data = pd.read_csv('CIRUS JETTY.csv')
        elif index==answer7:
            data = pd.read_csv('COMP SECURITY.csv')
        elif index==answer8:
            data = pd.read_csv('HALL#7.csv')
        elif index==answer9:
            data = pd.read_csv('BHABHA POINT.csv')
        elif index==answer10:
            data = pd.read_csv('RLG MAIN GATE.csv')
        elif index==answer11:
            data = pd.read_csv('RLG BACK GATE.csv')
        elif index==answer12:
            data = pd.read_csv('WIP PORTICO.csv')
        elif index==answer13:
            data = pd.read_csv('RSMS.csv')
        elif index==answer14:
            data = pd.read_csv('PP SECURITY.csv')
        elif index==answer15:
            data = pd.read_csv('SOUTH GATE.csv')
        elif index==answer16:
            data = pd.read_csv('PRAFUL.csv')
        elif index==answer17:
            data = pd.read_csv('IF3.csv')
        elif index==answer13:
            data = pd.read_csv('RUMP.csv')
        elif index==answer19:
            data = pd.read_csv('DHRUVA.csv')
        elif index==answer20:
            data = pd.read_csv('CIRUS.csv')
        elif index==answer21:
            data = pd.read_csv('ETP.csv')
        elif index==answer22:
            data = pd.read_csv('LAUNDRY.csv')


        rad_df1= data.iloc[542:602]
        rad_df1.plot(kind='bar',x='DateTime',y='RadiationLevel')
        plt.title('Radiation Graph')
        plt.show()


    def graph11(index):
        answer1="NG(OUT)"
        answer2="NG(IN)"
        answer3="CC SECURITY"
        answer4="ML(H)"
        answer5="ML(S)"
        answer6="CIRUS JETTY"
        answer7="COMP SECURITY"
        answer8="HALL#7"
        answer9="BHABHA POINT"
        answer10="RLG MAIN GATE"
        answer11="RLG BACK GATE"
        answer12="WIP PORTICO"
        answer13="RSMS"
        answer14="PP SECURITY"
        answer15="SOUTH GATE"
        answer16="PRAFUL"
        answer17="IF3"
        answer18="RUMP"
        answer19="DHRUVA"
        answer20="CIRUS"
        answer21="ETP"
        answer22="LAUNDRY"
        if index==answer1:
            data = pd.read_csv('NG(OUT).csv')
        elif index==answer2:
            data = pd.read_csv('NG(IN).csv')
        elif index==answer3:
            data = pd.read_csv('CC SECURITY.csv')
        elif index==answer4:
            data = pd.read_csv('ML(H).csv')
        elif index==answer5:
            data = pd.read_csv('ML(S).csv')
        elif index==answer6:
            data = pd.read_csv('CIRUS JETTY.csv')
        elif index==answer7:
            data = pd.read_csv('COMP SECURITY.csv')
        elif index==answer8:
            data = pd.read_csv('HALL#7.csv')
        elif index==answer9:
            data = pd.read_csv('BHABHA POINT.csv')
        elif index==answer10:
            data = pd.read_csv('RLG MAIN GATE.csv')
        elif index==answer11:
            data = pd.read_csv('RLG BACK GATE.csv')
        elif index==answer12:
            data = pd.read_csv('WIP PORTICO.csv')
        elif index==answer13:
            data = pd.read_csv('RSMS.csv')
        elif index==answer14:
            data = pd.read_csv('PP SECURITY.csv')
        elif index==answer15:
            data = pd.read_csv('SOUTH GATE.csv')
        elif index==answer16:
            data = pd.read_csv('PRAFUL.csv')
        elif index==answer17:
            data = pd.read_csv('IF3.csv')
        elif index==answer13:
            data = pd.read_csv('RUMP.csv')
        elif index==answer19:
            data = pd.read_csv('DHRUVA.csv')
        elif index==answer20:
            data = pd.read_csv('CIRUS.csv')
        elif index==answer21:
            data = pd.read_csv('ETP.csv')
        elif index==answer22:
            data = pd.read_csv('LAUNDRY.csv')


        rad_df1= data.iloc[602:662]
        rad_df1.plot(kind='bar',x='DateTime',y='RadiationLevel')
        plt.title('Radiation Graph')
        plt.show()

    def graph12(index):
        answer1="NG(OUT)"
        answer2="NG(IN)"
        answer3="CC SECURITY"
        answer4="ML(H)"
        answer5="ML(S)"
        answer6="CIRUS JETTY"
        answer7="COMP SECURITY"
        answer8="HALL#7"
        answer9="BHABHA POINT"
        answer10="RLG MAIN GATE"
        answer11="RLG BACK GATE"
        answer12="WIP PORTICO"
        answer13="RSMS"
        answer14="PP SECURITY"
        answer15="SOUTH GATE"
        answer16="PRAFUL"
        answer17="IF3"
        answer18="RUMP"
        answer19="DHRUVA"
        answer20="CIRUS"
        answer21="ETP"
        answer22="LAUNDRY"
        if index==answer1:
            data = pd.read_csv('NG(OUT).csv')
        elif index==answer2:
            data = pd.read_csv('NG(IN).csv')
        elif index==answer3:
            data = pd.read_csv('CC SECURITY.csv')
        elif index==answer4:
            data = pd.read_csv('ML(H).csv')
        elif index==answer5:
            data = pd.read_csv('ML(S).csv')
        elif index==answer6:
            data = pd.read_csv('CIRUS JETTY.csv')
        elif index==answer7:
            data = pd.read_csv('COMP SECURITY.csv')
        elif index==answer8:
            data = pd.read_csv('HALL#7.csv')
        elif index==answer9:
            data = pd.read_csv('BHABHA POINT.csv')
        elif index==answer10:
            data = pd.read_csv('RLG MAIN GATE.csv')
        elif index==answer11:
            data = pd.read_csv('RLG BACK GATE.csv')
        elif index==answer12:
            data = pd.read_csv('WIP PORTICO.csv')
        elif index==answer13:
            data = pd.read_csv('RSMS.csv')
        elif index==answer14:
            data = pd.read_csv('PP SECURITY.csv')
        elif index==answer15:
            data = pd.read_csv('SOUTH GATE.csv')
        elif index==answer16:
            data = pd.read_csv('PRAFUL.csv')
        elif index==answer17:
            data = pd.read_csv('IF3.csv')
        elif index==answer13:
            data = pd.read_csv('RUMP.csv')
        elif index==answer19:
            data = pd.read_csv('DHRUVA.csv')
        elif index==answer20:
            data = pd.read_csv('CIRUS.csv')
        elif index==answer21:
            data = pd.read_csv('ETP.csv')
        elif index==answer22:
            data = pd.read_csv('LAUNDRY.csv')



        rad_df1= data.iloc[662:721]
        rad_df1.plot(kind='bar',x='DateTime',y='RadiationLevel')
        plt.title('Radiation Graph')
        plt.show()
        
    def graph13(index):
        answer1="NG(OUT)"
        answer2="NG(IN)"
        answer3="CC SECURITY"
        answer4="ML(H)"
        answer5="ML(S)"
        answer6="CIRUS JETTY"
        answer7="COMP SECURITY"
        answer8="HALL#7"
        answer9="BHABHA POINT"
        answer10="RLG MAIN GATE"
        answer11="RLG BACK GATE"
        answer12="WIP PORTICO"
        answer13="RSMS"
        answer14="PP SECURITY"
        answer15="SOUTH GATE"
        answer16="PRAFUL"
        answer17="IF3"
        answer18="RUMP"
        answer19="DHRUVA"
        answer20="CIRUS"
        answer21="ETP"
        answer22="LAUNDRY"
        if index==answer1:
            data = pd.read_csv('NG(OUT).csv')
        elif index==answer2:
            data = pd.read_csv('NG(IN).csv')
        elif index==answer3:
            data = pd.read_csv('CC SECURITY.csv')
        elif index==answer4:
            data = pd.read_csv('ML(H).csv')
        elif index==answer5:
            data = pd.read_csv('ML(S).csv')
        elif index==answer6:
            data = pd.read_csv('CIRUS JETTY.csv')
        elif index==answer7:
            data = pd.read_csv('COMP SECURITY.csv')
        elif index==answer8:
            data = pd.read_csv('HALL#7.csv')
        elif index==answer9:
            data = pd.read_csv('BHABHA POINT.csv')
        elif index==answer10:
            data = pd.read_csv('RLG MAIN GATE.csv')
        elif index==answer11:
            data = pd.read_csv('RLG BACK GATE.csv')
        elif index==answer12:
            data = pd.read_csv('WIP PORTICO.csv')
        elif index==answer13:
            data = pd.read_csv('RSMS.csv')
        elif index==answer14:
            data = pd.read_csv('PP SECURITY.csv')
        elif index==answer15:
            data = pd.read_csv('SOUTH GATE.csv')
        elif index==answer16:
            data = pd.read_csv('PRAFUL.csv')
        elif index==answer17:
            data = pd.read_csv('IF3.csv')
        elif index==answer13:
            data = pd.read_csv('RUMP.csv')
        elif index==answer19:
            data = pd.read_csv('DHRUVA.csv')
        elif index==answer20:
            data = pd.read_csv('CIRUS.csv')
        elif index==answer21:
            data = pd.read_csv('ETP.csv')
        elif index==answer22:
            data = pd.read_csv('LAUNDRY.csv')


        rad_df1= data.iloc[1:721]
        rad_df1.plot(kind='line',x='DateTime',y='RadiationLevel')
        plt.title('Radiation Graph')
        plt.show()

        
    master = tk.Toplevel(root)
    master.geometry("350x90")
    master.title("RADIATION GRAPH GENERATOR")
    master.configure(background='light green')
    Label(master,text='SELECT THE LOCATION :',bg='light green',font="Arial 12").grid(row=1,column=0,padx=5 ,pady=5)
    selectedText=StringVar()
    selectedText.set("             ")
    mb=Menubutton(master, textvariable=selectedText,relief=GROOVE)
    mb.grid(row=1,column=1, padx=5, pady=5)
    mb.menu=Menu(mb, tearoff=0)
    mb.menu.add_command(label="NG(OUT)",command=lambda: changename("NG(OUT)") )
    mb.menu.add_command(label="NG(IN)",command=lambda: changename("NG(IN)") )
    mb.menu.add_command(label="CC SECURITY",command=lambda: changename("CC SECURITY") )
    mb.menu.add_command(label="ML(H)",command=lambda: changename("ML(H)") )
    mb.menu.add_command(label="ML(S)",command=lambda: changename("ML(S)") )
    mb.menu.add_command(label="CIRUS JETTY",command=lambda: changename("CIRUS JETTY") )
    mb.menu.add_command(label="COMP SECURITY",command=lambda: changename("COMP SECURITY") )
    mb.menu.add_command(label="HALL#7",command=lambda: changename("HALL#7") )
    mb.menu.add_command(label="BHABHA POINT",command=lambda: changename("BHABHA POINT") )
    mb.menu.add_command(label="RLG MAIN GATE",command=lambda: changename("RLG MAIN GATE") )
    mb.menu.add_command(label="RLG BACK GATE",command=lambda: changename("RLG BACK GATE") )
    mb.menu.add_command(label="WIP PORTICO",command=lambda: changename("WIP PORTICO") )
    mb.menu.add_command(label="RSMS",command=lambda: changename("RSMS") )
    mb.menu.add_command(label="PP SECURITY",command=lambda: changename("PP SECURITY") )
    mb.menu.add_command(label="SOUTH GATE",command=lambda: changename("SOUTH GATE") )
    mb.menu.add_command(label="PRAFUL",command=lambda: changename("PRAFUL") )
    mb.menu.add_command(label="IF3",command=lambda: changename("IF3") )
    mb.menu.add_command(label="RUMP",command=lambda: changename("RUMP") )
    mb.menu.add_command(label="DHRUVA",command=lambda: changename("DHRUVA") )
    mb.menu.add_command(label="CIRUS",command=lambda: changename("CIRUS") )
    mb.menu.add_command(label="ETP",command=lambda: changename("ETP") )
    mb.menu.add_command(label="LAUNDRY",command=lambda: changename("LAUNDRY") )
    mb["menu"]=mb.menu

    Button(master, text=" CLICK TO EXIT ",bg='light blue',command=lambda: destroy(master)).grid(row=2,column=0,padx=15,pady=10)
    
    master.mainloop()
    



    
root = tk.Tk()
root.geometry("360x150")
root.title("RADIATION GRAPH GENERATOR")
root.configure(background='light green')

Label(root, text='WELCOME TO GRAPH GENERATOR :',bg='light green',font="Arial 14").grid(row=0,column=0,columnspan=3, padx=5, pady=5)
Label(root,text='SELECT THE DATE :',bg='light green').grid(row=1,column=0)

selTime=StringVar()
selTime.set("CHOOSE HERE")

ttk.Button(root, textvariable=selTime, command=calender).grid(row=1,column=1,rowspan=3)
B1=Button(root,text=' INDIVIDUAL GRAPH ',bg='light blue',command=lambda: individual(root))
B1.grid(row=5,column=0,rowspan=3,pady=5)
B2=Button(root, text=' COMPARISON GRAPH ',bg='light blue',command=lambda: comparison(root))
B2.grid(row=5,column=1,rowspan=3,pady=5)
root.mainloop()





