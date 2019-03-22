import sys
import pandas as pd
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import projectgui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    projectgui_support.set_Tk_var()
    top = Job_Search (root)
    projectgui_support.init(root, top)
    root.mainloop()

w = None
def create_Job_Search(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    projectgui_support.set_Tk_var()
    top = Job_Search (w)
    projectgui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Job_Search():
    global w
    w.destroy()
    w = None


class Job_Search:
    def jobsearch(self):
        ks=self.ks.get()
        loc=self.loc.get()
        ey=int(self.wey.get())
        em=int(self.wem.get())
        sal=float(self.es.get())
        eq=self.eq.get()
        df=pd.read_csv('naukriData1.csv')
        df = df.dropna(how='all',axis=0)
        i=0
        print("**********************************************************************************************************")
        print("                                             Search Results                         ")
        print("**********************************************************************************************************")
        for index, row in df.iterrows():
            if(str(type(row['keyskills']))!="<class 'float'>" ):
                keys=row['keyskills'].split('     ')
            if(str(type(row['Location']))!="<class 'float'>" ):
                locs=re.split("[,    ()]+",row['Location'])
            if(str(type(row['uge']))!="<class 'float'>" ):
                eduqs=re.split("[,/-]+",row['uge'])
            if(str(type(row['pge']))!="<class 'float'>" ):
                eduqs.extend(re.split("[,/-]+",row['pge'] ))

            sf=0
            inter1=set(ks.split(',')).intersection(set(keys))
            inter2=set(loc.split(',')).intersection(set(locs))
            inter3=set(set(eq.split(',')).intersection(set(eduqs)))
            if(str(type(row['min experince']))!="<class 'float'>" ):
                exp=int(str(row['min experince'])[0:2])
            if(row['salary']=='null' or row['salary']=='Not Disclosed by Recruiter' or row['salary']=='Best In Industry'):
                sf=1
            else:
#                 s=str(row['salary'])[21:29].split(',')
#                 if(int(''.join(s))<sal*10000):
                    sf=0
            if(len(inter1)>0 and len(inter2)>0 and (ey+(em//12)>=exp) and len(inter3)>0 and sf==1):

                print(str(i+1)+'.)','Job  :',row['Job'])
                print('Company  :',row['company'])
                print('Location  :',row['Location'])
                print('Minimum working experince:',row['min experince'])
                print('Required Key skills:',row['keyskills'])
                print('Role  :',row['role'])
                print('Role category :',row['role category'])
                print('Employement type :',row['employement type'])
                print(row['functional area'])
                print('Salary:',row['salary'])
                print('Industry :',row['industry'])
                print('Job resposibilities :',row['job resposibilities'])
                print('Job requirements :',row['job requirements'])
                print('--------------------------------------------------------------------------------------------------')
                i+=1
        if(i==0):
            print("NO RESULTS FOUND")

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("600x450+465+12")
        top.title("Job Search")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#0000ff")
        self.Frame1.configure(width=575)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.42, rely=0.29, height=18, width=95)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="#ffffff")
        self.Label1.configure(background="#0000ff")
        self.Label1.configure(disabledforeground="#ffffff")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''SEARCH''')
        self.Label1.configure(width=95)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.08, rely=0.18, height=18, width=65)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''Key Skills''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.07, rely=0.24, height=18, width=75)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''Location''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.07, rely=0.31, height=18, width=95)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(text='''Work Experince''')

        self.ks = Entry(top)
        self.ks.place(relx=0.27, rely=0.18, relheight=0.04, relwidth=0.24)
        self.ks.configure(background="white")
        self.ks.configure(font="TkFixedFont")
        self.ks.configure(selectbackground="#c4c4c4")
        self.ks.configure(textvariable=projectgui_support.ks)

        self.loc = Entry(top)
        self.loc.place(relx=0.27, rely=0.24, relheight=0.04, relwidth=0.24)
        self.loc.configure(background="white")
        self.loc.configure(font="TkFixedFont")
        self.loc.configure(selectbackground="#c4c4c4")
        self.loc.configure(textvariable=projectgui_support.loc)

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)







        self.wey = Spinbox(top, from_=0.0, to=30.0)
        self.wey.place(relx=0.27, rely=0.31, relheight=0.04, relwidth=0.26)
        self.wey.configure(activebackground="#f9f9f9")
        self.wey.configure(background="white")
        self.wey.configure(highlightbackground="black")
        self.wey.configure(selectbackground="#c4c4c4")
        self.wey.configure(textvariable=projectgui_support.wey)
        self.wey.configure(to="30.0")

        self.Label5 = Label(top)
        self.Label5.place(relx=0.53, rely=0.31, height=18, width=35)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(text='''years''')

        self.wem = Spinbox(top, from_=0.0, to=12.0)
        self.wem.place(relx=0.6, rely=0.31, relheight=0.04, relwidth=0.26)
        self.wem.configure(activebackground="#f9f9f9")
        self.wem.configure(background="white")
        self.wem.configure(highlightbackground="black")
        self.wem.configure(selectbackground="#c4c4c4")
        self.wem.configure(textvariable=projectgui_support.wem)
        self.wem.configure(to="12.0")

        self.Label6 = Label(top)
        self.Label6.place(relx=0.88, rely=0.31, height=18, width=43)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(text='''months''')

        self.Label7 = Label(top)
        self.Label7.place(relx=0.07, rely=0.38, height=18, width=96)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(text='''Expected Salary''')

        self.es = Spinbox(top, from_=0.5, to=100.0)
        self.es.place(relx=0.27, rely=0.38, relheight=0.04, relwidth=0.26)
        self.es.configure(activebackground="#f9f9f9")
        self.es.configure(background="white")
        self.es.configure(from_="0.5")
        self.es.configure(highlightbackground="black")
        self.es.configure(selectbackground="#c4c4c4")
        self.es.configure(textvariable=projectgui_support.es)
        self.es.configure(to="100.0")

        self.Label8 = Label(top)
        self.Label8.place(relx=0.02, rely=0.44, height=18, width=145)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(text='''Educational Qualifications''')
        self.Label8.configure(width=145)

        self.eq = Entry(top)
        self.eq.place(relx=0.27, rely=0.44, relheight=0.04, relwidth=0.24)
        self.eq.configure(background="white")
        self.eq.configure(font="TkFixedFont")
        self.eq.configure(selectbackground="#c4c4c4")
        self.eq.configure(textvariable=projectgui_support.eq)

        self.search = Button(top)
        self.search.place(relx=0.45, rely=0.58, height=26, width=71)
        self.search.configure(activebackground="#d9d9d9")
        self.search.configure(text='''SUBMIT''')
        self.search.configure(command=self.jobsearch)
        self.Label9 = Label(top)
        self.Label9.place(relx=0.55, rely=0.38, height=18, width=97)
        self.Label9.configure(text='''Lakhs(per anum)''')

    @staticmethod
    def popup1(event):
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.post(event.x_root, event.y_root)

if __name__ == '__main__':
    vp_start_gui()
