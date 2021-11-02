from tkinter import *
from tkinter.ttk import *
import pandas as pd
import random

cs = pd.read_csv("anime2.csv")

num = 0
for a1 in cs["Name"]:
    num += 1

yr = {
        "Un": [], "1961": [], "1962": [], "1963": [], "1964": [], "1965": [], "1966": [], "1967": [],
        "1968": [], "1969": [], "1970": [], "1971": [], "1972": [], "1973": [], "1974": [], "1975": [],
        "1976": [], "1977": [], "1978": [], "1979": [], "1980": [], "1981": [], "1982": [], "1983": [],
        "1984": [], "1985": [], "1986": [], "1987": [], "1988": [], "1989": [], "1990": [], "1991": [],
        "1992": [], "1993": [], "1994": [], "1995": [], "1996": [], "1997": [], "1998": [], "1999": [],
        "2000": [], "2001": [], "2002": [], "2003": [], "2004": [], "2005": [], "2006": [], "2007": [],
        "2008": [], "2009": [], "2010": [], "2011": [], "2012": [], "2013": [], "2014": [], "2015": [],
        "2016": [], "2017": [], "2018": [], "2019": [], "2020": [], "2021": []
    }
Un = ["Unknown"]
Fa = ["Fall"]
sp = ["Spring"]
su = ["Summer"]
wi = ["Winter"]
for a10 in cs["Premiered"].index:
    if cs["Premiered"].loc[a10] in Un:
        yr["Un"].append(a10)
ym = 1961
yml = []
for a309 in range(61):
    yml.append(ym)
    ym += 1
for a310 in range(61):
    for a311 in cs["Premiered"].index:
        if cs["Premiered"].loc[a311][:4] in Fa:
            if int(cs["Premiered"].loc[a311][5:9]) == yml[a310]:
                yr[str(yml[a310])].append(a311)
        if cs["Premiered"].loc[a311][:6] in sp:
            if int(cs["Premiered"].loc[a311][7:11]) == yml[a310]:
                yr[str(yml[a310])].append(a311)
        if cs["Premiered"].loc[a311][:6] in su:
            if int(cs["Premiered"].loc[a311][7:11]) == yml[a310]:
                yr[str(yml[a310])].append(a311)
        if cs["Premiered"].loc[a311][:6] in wi:
            if int(cs["Premiered"].loc[a311][7:11]) == yml[a310]:
                yr[str(yml[a310])].append(a311)

window = Tk()

def RandomAnime():
    def oneanime():
        txt5 = Label(text= "Anime Name")
        txt6 = Label(text= "Episode")
        txt7 = Label(text= "Score")
        txt10 = Label(text= "Genres")
        rd = random.randint(0, num)
        tt0[0].configure(text= str(cs["Name"].loc[rd]))
        tt2[0].configure(text= str(cs["Episodes"].loc[rd]))
        tt4[0].configure(text= str(cs["Score"].loc[rd]))
        tt6[0].configure(text= str(cs["Genres"].loc[rd]))
        for a2 in range(int(len(tt0))-1):
            tt0[a2+1].configure(text= " ")
            tt2[a2+1].configure(text= " ")
            tt4[a2+1].configure(text= " ")
            tt6[a2+1].configure(text= " ")
        txt5.grid(column=0, row=3)
        txt6.grid(column=2, row=3)
        txt7.grid(column=4, row=3)
        txt10.grid(column=6, row=3)
    def threeanime():
        txt5 = Label(text= "Anime Name")
        txt6 = Label(text= "Episode")
        txt7 = Label(text= "Score")
        txt10 = Label(text= "Genres")
        for a7 in range(3):
            rd = random.randint(0, num)
            tt0[a7].configure(text= str(cs["Name"].loc[rd]))
            tt2[a7].configure(text= str(cs["Episodes"].loc[rd]))
            tt4[a7].configure(text= str(cs["Score"].loc[rd]))
            tt6[a7].configure(text= str(cs["Genres"].loc[rd]))
        for a8 in range(int(len(tt0))-3):
            tt0[a8+3].configure(text= " ")
            tt2[a8+3].configure(text= " ")
            tt4[a8+3].configure(text= " ")
            tt6[a8+3].configure(text= " ")
        txt5.grid(column=0, row=3)
        txt6.grid(column=2, row=3)
        txt7.grid(column=4, row=3)
        txt10.grid(column=6, row=3)
    def tenanime():
        txt5 = Label(text= "Anime Name")
        txt6 = Label(text= "Episode")
        txt7 = Label(text= "Score")
        txt10 = Label(text= "Genres")
        for a9 in range(10):
            rd = random.randint(0, num)
            tt0[a9].configure(text= str(cs["Name"].loc[rd]))
            tt2[a9].configure(text= str(cs["Episodes"].loc[rd]))
            tt4[a9].configure(text= str(cs["Score"].loc[rd]))
            tt6[a9].configure(text= str(cs["Genres"].loc[rd]))
        txt5.grid(column=0, row=3)
        txt6.grid(column=2, row=3)
        txt7.grid(column=4, row=3)
        txt10.grid(column=6, row=3)
    bt3 = Button(window, text="Random 1 Anime", command=oneanime)
    bt4 = Button(window, text="Random 3 Anime", command=threeanime)
    bt5 = Button(window, text="Random 10 Anime", command=tenanime)
    bt3.grid(column=1, row=2)
    bt4.grid(column=3, row=2)
    bt5.grid(column=5, row=2)


def AnimeList():
    window2 = Tk()

    def Unk():
        def Enter1():
            noc1 = int(dropbox.get())
            i1 = noc1*30
            if noc1 < 427:
                for a23 in range(30):
                    ttw21[a23].configure(text= str(cs["Name"].loc[yr["Un"][i1]]))
                    ttw22[a23].configure(text= str(cs["Episodes"].loc[yr["Un"][i1]]))
                    ttw23[a23].configure(text= str(cs["Score"].loc[yr["Un"][i1]]))
                    ttw24[a23].configure(text= str(cs["Premiered"].loc[yr["Un"][i1]]))
                    ttw25[a23].configure(text= str(cs["Genres"].loc[yr["Un"][i1]]))
                    i1 += 1
            if noc1 == 427:
                for a24 in range(7):
                    ttw21[a24].configure(text= str(cs["Name"].loc[yr["Un"][i1]]))
                    ttw22[a24].configure(text= str(cs["Episodes"].loc[yr["Un"][i1]]))
                    ttw23[a24].configure(text= str(cs["Score"].loc[yr["Un"][i1]]))
                    ttw24[a24].configure(text= str(cs["Premiered"].loc[yr["Un"][i1]]))
                    ttw25[a24].configure(text= str(cs["Genres"].loc[yr["Un"][i1]]))
                    i1 += 1
                a251 = 7
                for a25 in range(23):
                    ttw21[a251].configure(text= " ")
                    ttw22[a251].configure(text= " ")
                    ttw23[a251].configure(text= " ")
                    ttw24[a251].configure(text= " ")
                    ttw25[a251].configure(text= " ")
                    a251 += 1
        Unknow = []
        p1 = int(len(yr["Un"])/30)
        for a22 in range(p1):
            Unknow.append(a22+1)
        dropbox["values"] = Unknow
        dropbox.current(0)
        page3 = 0
        for a24 in range(30):
            ttw21[a24].configure(text= str(cs["Name"].loc[yr["Un"][page3]]))
            ttw22[a24].configure(text= str(cs["Episodes"].loc[yr["Un"][page3]]))
            ttw23[a24].configure(text= str(cs["Score"].loc[yr["Un"][page3]]))
            ttw24[a24].configure(text= str(cs["Premiered"].loc[yr["Un"][page3]]))
            ttw25[a24].configure(text= str(cs["Genres"].loc[yr["Un"][page3]]))
            page3 += 1
        bt14.configure(text="Enter", command=Enter1)

    def y1961():
        def Enter2():
            noc2 = int(dropbox.get())-1
            i2 = noc2*30
            for a41 in range(30):
                if i2 == 0:
                    ttw21[a41].configure(text= str(cs["Name"].loc[yr["1961"][i2]]))
                    ttw22[a41].configure(text= str(cs["Episodes"].loc[yr["1961"][i2]]))
                    ttw23[a41].configure(text= str(cs["Score"].loc[yr["1961"][i2]]))
                    ttw24[a41].configure(text= str(cs["Premiered"].loc[yr["1961"][i2]]))
                    ttw25[a41].configure(text= str(cs["Genres"].loc[yr["1961"][i2]]))
                if i2 > 0:
                    ttw21[a41].configure(text= " ")
                    ttw22[a41].configure(text= " ")
                    ttw23[a41].configure(text= " ")
                    ttw24[a41].configure(text= " ")
                    ttw25[a41].configure(text= " ")
                i2 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i2 = 0
        for a41 in range(30):
            if i2 == 0:
                ttw21[a41].configure(text= str(cs["Name"].loc[yr["1961"][i2]]))
                ttw22[a41].configure(text= str(cs["Episodes"].loc[yr["1961"][i2]]))
                ttw23[a41].configure(text= str(cs["Score"].loc[yr["1961"][i2]]))
                ttw24[a41].configure(text= str(cs["Premiered"].loc[yr["1961"][i2]]))
                ttw25[a41].configure(text= str(cs["Genres"].loc[yr["1961"][i2]]))
            if i2 > 0:
                ttw21[a41].configure(text= " ")
                ttw22[a41].configure(text= " ")
                ttw23[a41].configure(text= " ")
                ttw24[a41].configure(text= " ")
                ttw25[a41].configure(text= " ")
            i2 += 1
        bt14.configure(text="Enter", command=Enter2)

    def y1962():
        def Enter3():
            noc3 = int(dropbox.get())-1
            i3 = noc3*30
            for a42 in range(30):
                if i3 == 0:
                    ttw21[a42].configure(text= str(cs["Name"].loc[yr["1962"][i3]]))
                    ttw22[a42].configure(text= str(cs["Episodes"].loc[yr["1962"][i3]]))
                    ttw23[a42].configure(text= str(cs["Score"].loc[yr["1962"][i3]]))
                    ttw24[a42].configure(text= str(cs["Premiered"].loc[yr["1962"][i3]]))
                    ttw25[a42].configure(text= str(cs["Genres"].loc[yr["1962"][i3]]))
                if i3 > 0:
                    ttw21[a42].configure(text= " ")
                    ttw22[a42].configure(text= " ")
                    ttw23[a42].configure(text= " ")
                    ttw24[a42].configure(text= " ")
                    ttw25[a42].configure(text= " ")
                i3 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i3 = 0
        for a42 in range(30):
            if i3 == 0:
                ttw21[a42].configure(text= str(cs["Name"].loc[yr["1962"][i3]]))
                ttw22[a42].configure(text= str(cs["Episodes"].loc[yr["1962"][i3]]))
                ttw23[a42].configure(text= str(cs["Score"].loc[yr["1962"][i3]]))
                ttw24[a42].configure(text= str(cs["Premiered"].loc[yr["1962"][i3]]))
                ttw25[a42].configure(text= str(cs["Genres"].loc[yr["1962"][i3]]))
            if i3 > 0:
                ttw21[a42].configure(text= " ")
                ttw22[a42].configure(text= " ")
                ttw23[a42].configure(text= " ")
                ttw24[a42].configure(text= " ")
                ttw25[a42].configure(text= " ")
            i3 += 1
        bt14.configure(text="Enter", command=Enter3)

    def y1963():
        def Enter4():
            noc4 = int(dropbox.get())-1
            i4 = noc4*30
            for a43 in range(30):
                if i4 <= 4:
                    ttw21[a43].configure(text= str(cs["Name"].loc[yr["1963"][i4]]))
                    ttw22[a43].configure(text= str(cs["Episodes"].loc[yr["1963"][i4]]))
                    ttw23[a43].configure(text= str(cs["Score"].loc[yr["1963"][i4]]))
                    ttw24[a43].configure(text= str(cs["Premiered"].loc[yr["1963"][i4]]))
                    ttw25[a43].configure(text= str(cs["Genres"].loc[yr["1963"][i4]]))
                if i4 > 4:
                    ttw21[a43].configure(text= " ")
                    ttw22[a43].configure(text= " ")
                    ttw23[a43].configure(text= " ")
                    ttw24[a43].configure(text= " ")
                    ttw25[a43].configure(text= " ")
                i4 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i4 = 0
        for a43 in range(30):
            if i4 <= 4:
                ttw21[a43].configure(text= str(cs["Name"].loc[yr["1963"][i4]]))
                ttw22[a43].configure(text= str(cs["Episodes"].loc[yr["1963"][i4]]))
                ttw23[a43].configure(text= str(cs["Score"].loc[yr["1963"][i4]]))
                ttw24[a43].configure(text= str(cs["Premiered"].loc[yr["1963"][i4]]))
                ttw25[a43].configure(text= str(cs["Genres"].loc[yr["1963"][i4]]))
            if i4 > 4:
                ttw21[a43].configure(text= " ")
                ttw22[a43].configure(text= " ")
                ttw23[a43].configure(text= " ")
                ttw24[a43].configure(text= " ")
                ttw25[a43].configure(text= " ")
            i4 += 1
        bt14.configure(text="Enter", command=Enter4)
    def y1964():
        def Enter5():
            noc5 = int(dropbox.get())-1
            i5 = noc5*30
            for a44 in range(30):
                if i5 <= 3:
                    ttw21[a44].configure(text= str(cs["Name"].loc[yr["1964"][i5]]))
                    ttw22[a44].configure(text= str(cs["Episodes"].loc[yr["1964"][i5]]))
                    ttw23[a44].configure(text= str(cs["Score"].loc[yr["1964"][i5]]))
                    ttw24[a44].configure(text= str(cs["Premiered"].loc[yr["1964"][i5]]))
                    ttw25[a44].configure(text= str(cs["Genres"].loc[yr["1964"][i5]]))
                if i5 > 3:
                    ttw21[a44].configure(text= " ")
                    ttw22[a44].configure(text= " ")
                    ttw23[a44].configure(text= " ")
                    ttw24[a44].configure(text= " ")
                    ttw25[a44].configure(text= " ")
                i5 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i5 = 0
        for a44 in range(30):
            if i5 <= 3:
                ttw21[a44].configure(text= str(cs["Name"].loc[yr["1964"][i5]]))
                ttw22[a44].configure(text= str(cs["Episodes"].loc[yr["1964"][i5]]))
                ttw23[a44].configure(text= str(cs["Score"].loc[yr["1964"][i5]]))
                ttw24[a44].configure(text= str(cs["Premiered"].loc[yr["1964"][i5]]))
                ttw25[a44].configure(text= str(cs["Genres"].loc[yr["1964"][i5]]))
            if i5 > 3:
                ttw21[a44].configure(text= " ")
                ttw22[a44].configure(text= " ")
                ttw23[a44].configure(text= " ")
                ttw24[a44].configure(text= " ")
                ttw25[a44].configure(text= " ")
            i5 += 1
        bt14.configure(text="Enter", command=Enter5)
    def y1965():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 11:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1965"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1965"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1965"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1965"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1965"][i6]]))
                if i6 > 11:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 11:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1965"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1965"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1965"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1965"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1965"][i6]]))
            if i6 > 11:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1966():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 10:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1966"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1966"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1966"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1966"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1966"][i6]]))
                if i6 > 10:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 10:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1966"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1966"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1966"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1966"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1966"][i6]]))
            if i6 > 10:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1967():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 14:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1967"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1967"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1967"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1967"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1967"][i6]]))
                if i6 > 14:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 14:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1967"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1967"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1967"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1967"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1967"][i6]]))
            if i6 > 14:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1968():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 13:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1968"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1968"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1968"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1968"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1968"][i6]]))
                if i6 > 13:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 13:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1968"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1968"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1968"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1968"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1968"][i6]]))
            if i6 > 13:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1969():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 15:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1969"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1969"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1969"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1969"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1969"][i6]]))
                if i6 > 15:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 15:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1969"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1969"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1969"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1969"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1969"][i6]]))
            if i6 > 15:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1970():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 16:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1970"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1970"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1970"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1970"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1970"][i6]]))
                if i6 > 16:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 16:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1970"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1970"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1970"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1970"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1970"][i6]]))
            if i6 > 16:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1971():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 15:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1971"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1971"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1971"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1971"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1971"][i6]]))
                if i6 > 15:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 15:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1971"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1971"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1971"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1971"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1971"][i6]]))
            if i6 > 15:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1972():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 14:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1972"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1972"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1972"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1972"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1972"][i6]]))
                if i6 > 14:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 14:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1972"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1972"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1972"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1972"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1972"][i6]]))
            if i6 > 14:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1973():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 17:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1973"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1973"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1973"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1973"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1973"][i6]]))
                if i6 > 17:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 17:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1973"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1973"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1973"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1973"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1973"][i6]]))
            if i6 > 17:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1974():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 21:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1974"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1974"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1974"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1974"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1974"][i6]]))
                if i6 > 21:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 21:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1974"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1974"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1974"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1974"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1974"][i6]]))
            if i6 > 21:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1975():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 20:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1975"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1975"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1975"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1975"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1975"][i6]]))
                if i6 > 20:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 20:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1975"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1975"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1975"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1975"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1975"][i6]]))
            if i6 > 20:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1976():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 24:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1976"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1976"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1976"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1976"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1976"][i6]]))
                if i6 > 24:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 24:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1976"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1976"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1976"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1976"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1976"][i6]]))
            if i6 > 24:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1977():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 26:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1977"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1977"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1977"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1977"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1977"][i6]]))
                if i6 > 26:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 26:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1977"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1977"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1977"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1977"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1977"][i6]]))
            if i6 > 26:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1978():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 21:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1978"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1978"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1978"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1978"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1978"][i6]]))
                if i6 > 21:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 21:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1978"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1978"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1978"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1978"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1978"][i6]]))
            if i6 > 21:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1979():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 25:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1979"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1979"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1979"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1979"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1979"][i6]]))
                if i6 > 25:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 25:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1979"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1979"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1979"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1979"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1979"][i6]]))
            if i6 > 25:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1980():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 27:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1980"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1980"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1980"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1980"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1980"][i6]]))
                if i6 > 27:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 27:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1980"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1980"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1980"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1980"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1980"][i6]]))
            if i6 > 27:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1981():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1981"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1981"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1981"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1981"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1981"][i6]]))
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["1981"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1981"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["1981"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1981"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1981"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1982():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 28:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1982"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1982"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1982"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1982"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1982"][i6]]))
                if i6 > 28:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 28:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1982"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1982"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1982"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1982"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1982"][i6]]))
            if i6 > 28:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1983():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 1:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["1983"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1983"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["1983"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1983"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1983"][i6]]))
                    i6 += 1
            if noc6 == 1:
                for a46 in range(30):
                    if i6 <= 36:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["1983"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1983"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["1983"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1983"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1983"][i6]]))
                    if i6 > 36:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["1983"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1983"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["1983"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1983"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1983"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1984():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 1:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["1984"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1984"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["1984"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1984"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1984"][i6]]))
                    i6 += 1
            if noc6 == 1:
                for a46 in range(30):
                    if i6 <= 36:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["1984"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1984"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["1984"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1984"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1984"][i6]]))
                    if i6 > 36:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["1984"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1984"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["1984"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1984"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1984"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1985():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 19:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1985"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1985"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1985"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1985"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1985"][i6]]))
                if i6 > 19:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 19:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1985"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1985"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1985"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1985"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1985"][i6]]))
            if i6 > 19:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1986():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 26:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1986"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1986"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1986"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1986"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1986"][i6]]))
                if i6 > 26:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 26:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1986"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1986"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1986"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1986"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1986"][i6]]))
            if i6 > 26:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1987():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1987"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1987"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1987"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1987"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1987"][i6]]))
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["1987"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1987"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["1987"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1987"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1987"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1988():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 1:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["1988"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1988"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["1988"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1988"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1988"][i6]]))
                    i6 += 1
            if noc6 == 1:
                for a46 in range(30):
                    if i6 <= 37:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["1988"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1988"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["1988"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1988"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1988"][i6]]))
                    if i6 > 37:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["1988"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1988"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["1988"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1988"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1988"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1989():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 1:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["1989"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1989"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["1989"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1989"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1989"][i6]]))
                    i6 += 1
            if noc6 == 1:
                for a46 in range(30):
                    if i6 <= 36:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["1989"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1989"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["1989"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1989"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1989"][i6]]))
                    if i6 > 36:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["1989"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1989"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["1989"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1989"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1989"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1990():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 27:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1990"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1990"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1990"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1990"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1990"][i6]]))
                if i6 > 27:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 27:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1990"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1990"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1990"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1990"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1990"][i6]]))
            if i6 > 27:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1991():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 1:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["1991"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1991"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["1991"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1991"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1991"][i6]]))
                    i6 += 1
            if noc6 == 1:
                for a46 in range(30):
                    if i6 <= 37:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["1991"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1991"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["1991"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1991"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1991"][i6]]))
                    if i6 > 37:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["1991"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1991"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["1991"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1991"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1991"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1992():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 1:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["1992"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1992"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["1992"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1992"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1992"][i6]]))
                    i6 += 1
            if noc6 == 1:
                for a46 in range(30):
                    if i6 <= 40:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["1992"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1992"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["1992"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1992"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1992"][i6]]))
                    if i6 > 40:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["1992"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1992"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["1992"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1992"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1992"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1993():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            for a45 in range(30):
                if i6 <= 20:
                    ttw21[a45].configure(text= str(cs["Name"].loc[yr["1993"][i6]]))
                    ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1993"][i6]]))
                    ttw23[a45].configure(text= str(cs["Score"].loc[yr["1993"][i6]]))
                    ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1993"][i6]]))
                    ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1993"][i6]]))
                if i6 > 20:
                    ttw21[a45].configure(text= " ")
                    ttw22[a45].configure(text= " ")
                    ttw23[a45].configure(text= " ")
                    ttw24[a45].configure(text= " ")
                    ttw25[a45].configure(text= " ")
                i6 += 1
        dropbox["values"] = 1
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            if i6 <= 20:
                ttw21[a45].configure(text= str(cs["Name"].loc[yr["1993"][i6]]))
                ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1993"][i6]]))
                ttw23[a45].configure(text= str(cs["Score"].loc[yr["1993"][i6]]))
                ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1993"][i6]]))
                ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1993"][i6]]))
            if i6 > 20:
                ttw21[a45].configure(text= " ")
                ttw22[a45].configure(text= " ")
                ttw23[a45].configure(text= " ")
                ttw24[a45].configure(text= " ")
                ttw25[a45].configure(text= " ")
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1994():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 1:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["1994"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1994"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["1994"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1994"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1994"][i6]]))
                    i6 += 1
            if noc6 == 1:
                for a46 in range(30):
                    if i6 <= 39:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["1994"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1994"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["1994"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1994"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1994"][i6]]))
                    if i6 > 39:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["1994"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1994"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["1994"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1994"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1994"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1995():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 1:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["1995"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1995"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["1995"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1995"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1995"][i6]]))
                    i6 += 1
            if noc6 == 1:
                for a46 in range(30):
                    if i6 <= 43:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["1995"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1995"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["1995"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1995"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1995"][i6]]))
                    if i6 > 43:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["1995"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1995"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["1995"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1995"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1995"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1996():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 1:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["1996"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1996"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["1996"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1996"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1996"][i6]]))
                    i6 += 1
            if noc6 == 1:
                for a46 in range(30):
                    if i6 <= 39:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["1996"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1996"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["1996"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1996"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1996"][i6]]))
                    if i6 > 39:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["1996"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1996"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["1996"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1996"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1996"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1997():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 1:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["1997"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1997"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["1997"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1997"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1997"][i6]]))
                    i6 += 1
            if noc6 == 1:
                for a46 in range(30):
                    if i6 <= 44:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["1997"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1997"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["1997"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1997"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1997"][i6]]))
                    if i6 > 44:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["1997"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1997"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["1997"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1997"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1997"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1998():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 2:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["1998"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1998"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["1998"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1998"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1998"][i6]]))
                    i6 += 1
            if noc6 == 2:
                for a46 in range(30):
                    if i6 <= 80:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["1998"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1998"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["1998"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1998"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1998"][i6]]))
                    if i6 > 80:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["1998"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1998"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["1998"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1998"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1998"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y1999():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 3:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["1999"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1999"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["1999"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1999"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1999"][i6]]))
                    i6 += 1
            if noc6 == 3:
                for a46 in range(30):
                    if i6 <= 90:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["1999"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["1999"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["1999"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["1999"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["1999"][i6]]))
                    if i6 > 90:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["1999"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["1999"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["1999"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["1999"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["1999"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2000():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 1:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2000"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2000"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2000"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2000"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2000"][i6]]))
                    i6 += 1
            if noc6 == 1:
                for a46 in range(30):
                    if i6 <= 56:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2000"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2000"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2000"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2000"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2000"][i6]]))
                    if i6 > 56:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2000"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2000"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2000"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2000"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2000"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2001():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 3:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2001"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2001"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2001"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2001"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2001"][i6]]))
                    i6 += 1
            if noc6 == 3:
                for a46 in range(30):
                    if i6 <= 90:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2001"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2001"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2001"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2001"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2001"][i6]]))
                    if i6 > 90:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2001"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2001"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2001"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2001"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2001"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2002():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 2:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2002"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2002"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2002"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2002"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2002"][i6]]))
                    i6 += 1
            if noc6 == 2:
                for a46 in range(30):
                    if i6 <= 88:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2002"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2002"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2002"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2002"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2002"][i6]]))
                    if i6 > 88:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2002"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2002"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2002"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2002"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2002"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2003():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 3:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2003"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2003"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2003"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2003"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2003"][i6]]))
                    i6 += 1
            if noc6 == 3:
                for a46 in range(30):
                    if i6 <= 109:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2003"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2003"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2003"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2003"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2003"][i6]]))
                    if i6 > 109:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2003"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2003"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2003"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2003"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2003"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2004():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 4:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2004"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2004"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2004"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2004"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2004"][i6]]))
                    i6 += 1
            if noc6 == 4:
                for a46 in range(30):
                    if i6 <= 128:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2004"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2004"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2004"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2004"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2004"][i6]]))
                    if i6 > 128:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2004"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2004"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2004"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2004"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2004"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2005():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 4:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2005"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2005"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2005"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2005"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2005"][i6]]))
                    i6 += 1
            if noc6 == 4:
                for a46 in range(30):
                    if i6 <= 121:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2005"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2005"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2005"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2005"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2005"][i6]]))
                    if i6 > 121:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2005"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2005"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2005"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2005"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2005"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2006():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 6:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2006"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2006"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2006"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2006"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2006"][i6]]))
                    i6 += 1
            if noc6 == 6:
                for a46 in range(30):
                    if i6 <= 182:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2006"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2006"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2006"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2006"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2006"][i6]]))
                    if i6 > 182:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5,6,7]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2006"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2006"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2006"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2006"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2006"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2007():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 5:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2007"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2007"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2007"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2007"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2007"][i6]]))
                    i6 += 1
            if noc6 == 5:
                for a46 in range(30):
                    if i6 <= 159:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2007"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2007"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2007"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2007"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2007"][i6]]))
                    if i6 > 159:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5,6]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2007"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2007"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2007"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2007"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2007"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2008():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 5:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2008"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2008"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2008"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2008"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2008"][i6]]))
                    i6 += 1
            if noc6 == 5:
                for a46 in range(30):
                    if i6 <= 154:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2008"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2008"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2008"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2008"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2008"][i6]]))
                    if i6 > 154:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5,6]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2008"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2008"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2008"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2008"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2008"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2009():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 4:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2009"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2009"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2009"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2009"]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2009"][i6]]))
                    i6 += 1
            if noc6 == 4:
                for a46 in range(30):
                    if i6 <= 148:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2009"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2009"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2009"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2009"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2009"][i6]]))
                    if i6 > 148:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2009"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2009"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2009"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2009"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2009"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2010():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 4:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2010"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2010"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2010"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2010"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2010"][i6]]))
                    i6 += 1
            if noc6 == 4:
                for a46 in range(30):
                    if i6 <= 125:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2010"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2010"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2010"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2010"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2010"][i6]]))
                    if i6 > 125:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2010"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2010"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2010"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2010"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2010"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2011():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 5:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2011"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2011"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2011"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2011"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2011"][i6]]))
                    i6 += 1
            if noc6 == 5:
                for a46 in range(30):
                    if i6 <= 165:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2011"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2011"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2011"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2011"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2011"][i6]]))
                    if i6 > 165:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5,6]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2011"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2011"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2011"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2011"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2011"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2012():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 5:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2012"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2012"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2012"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2012"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2012"][i6]]))
                    i6 += 1
            if noc6 == 5:
                for a46 in range(30):
                    if i6 <= 166:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2012"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2012"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2012"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2012"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2012"][i6]]))
                    if i6 > 166:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5,6]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2012"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2012"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2012"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2012"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2012"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2013():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 6:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2013"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2013"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2013"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2013"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2013"][i6]]))
                    i6 += 1
            if noc6 == 6:
                for a46 in range(30):
                    if i6 <= 195:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2013"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2013"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2013"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2013"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2013"][i6]]))
                    if i6 > 195:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5,6,7]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2013"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2013"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2013"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2013"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2013"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2014():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 7:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2014"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2014"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2014"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2014"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2014"][i6]]))
                    i6 += 1
            if noc6 == 7:
                for a46 in range(30):
                    if i6 <= 226:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2014"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2014"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2014"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2014"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2014"][i6]]))
                    if i6 > 226:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5,6,7,8]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2014"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2014"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2014"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2014"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2014"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2015():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 7:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2015"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2015"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2015"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2015"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2015"][i6]]))
                    i6 += 1
            if noc6 == 7:
                for a46 in range(30):
                    if i6 <= 228:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2015"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2015"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2015"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2015"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2015"][i6]]))
                    if i6 > 228:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5,6,7,8]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2015"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2015"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2015"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2015"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2015"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2016():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 8:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2016"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2016"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2016"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2016"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2016"][i6]]))
                    i6 += 1
            if noc6 == 8:
                for a46 in range(30):
                    if i6 <= 261:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2016"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2016"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2016"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2016"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2016"][i6]]))
                    if i6 > 261:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5,6,7,8,9]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2016"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2016"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2016"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2016"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2016"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2017():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 8:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2017"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2017"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2017"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2017"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2017"][i6]]))
                    i6 += 1
            if noc6 == 8:
                for a46 in range(30):
                    if i6 <= 265:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2017"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2017"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2017"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2017"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2017"][i6]]))
                    if i6 > 265:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5,6,7,8,9]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2017"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2017"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2017"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2017"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2017"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2018():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 8:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2018"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2018"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2018"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2018"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2018"][i6]]))
                    i6 += 1
            if noc6 == 8:
                for a46 in range(30):
                    if i6 <= 256:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2018"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2018"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2018"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2018"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2018"][i6]]))
                    if i6 > 256:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5,6,7,8,9]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2018"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2018"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2018"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2018"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2018"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2019():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 6:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2019"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2019"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2019"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2019"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2019"][i6]]))
                    i6 += 1
            if noc6 == 6:
                for a46 in range(30):
                    if i6 <= 201:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2019"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2019"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2019"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2019"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2019"][i6]]))
                    if i6 > 201:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5,6,7]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2019"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2019"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2019"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2019"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2019"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2020():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 6:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2020"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2020"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2020"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2020"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2020"][i6]]))
                    i6 += 1
            if noc6 == 6:
                for a46 in range(30):
                    if i6 <= 190:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2020"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2020"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2020"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2020"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2020"][i6]]))
                    if i6 > 190:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5,6,7]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2020"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2020"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2020"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2020"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2020"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    def y2021():
        def Enter6():
            noc6 = int(dropbox.get())-1
            i6 = noc6*30
            if noc6 < 4:
                for a46 in range(30):
                    ttw21[a46].configure(text= str(cs["Name"].loc[yr["2021"][i6]]))
                    ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2021"][i6]]))
                    ttw23[a46].configure(text= str(cs["Score"].loc[yr["2021"][i6]]))
                    ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2021"][i6]]))
                    ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2021"][i6]]))
                    i6 += 1
            if noc6 == 4:
                for a46 in range(30):
                    if i6 <= 140:
                        ttw21[a46].configure(text= str(cs["Name"].loc[yr["2021"][i6]]))
                        ttw22[a46].configure(text= str(cs["Episodes"].loc[yr["2021"][i6]]))
                        ttw23[a46].configure(text= str(cs["Score"].loc[yr["2021"][i6]]))
                        ttw24[a46].configure(text= str(cs["Premiered"].loc[yr["2021"][i6]]))
                        ttw25[a46].configure(text= str(cs["Genres"].loc[yr["2021"][i6]]))
                    if i6 > 140:
                        ttw21[a46].configure(text= " ")
                        ttw22[a46].configure(text= " ")
                        ttw23[a46].configure(text= " ")
                        ttw24[a46].configure(text= " ")
                        ttw25[a46].configure(text= " ")
                    i6 += 1
        page80 = [1,2,3,4,5]
        dropbox["values"] = page80
        dropbox.current(0)
        i6 = 0
        for a45 in range(30):
            ttw21[a45].configure(text= str(cs["Name"].loc[yr["2021"][i6]]))
            ttw22[a45].configure(text= str(cs["Episodes"].loc[yr["2021"][i6]]))
            ttw23[a45].configure(text= str(cs["Score"].loc[yr["2021"][i6]]))
            ttw24[a45].configure(text= str(cs["Premiered"].loc[yr["2021"][i6]]))
            ttw25[a45].configure(text= str(cs["Genres"].loc[yr["2021"][i6]]))
            i6 += 1
        bt14.configure(text="Enter", command=Enter6)
    
    def All():
        def Enter7():
            noc7 = int(dropbox.get())-1
            i7 = noc7*30
            if noc7 < 585:
                for a27 in range(30):
                    ttw21[a27].configure(text= str(cs["Name"].loc[nu1[i7]]))
                    ttw22[a27].configure(text= str(cs["Episodes"].loc[nu1[i7]]))
                    ttw23[a27].configure(text= str(cs["Score"].loc[nu1[i7]]))
                    ttw24[a27].configure(text= str(cs["Premiered"].loc[nu1[i7]]))
                    ttw25[a27].configure(text= str(cs["Genres"].loc[nu1[i7]]))
                    i7 += 1
            if noc7 == 585:
                for a28 in range(12):
                    ttw21[a28].configure(text= str(cs["Name"].loc[nu1[i7]]))
                    ttw22[a28].configure(text= str(cs["Episodes"].loc[nu1[i7]]))
                    ttw23[a28].configure(text= str(cs["Score"].loc[nu1[i7]]))
                    ttw24[a28].configure(text= str(cs["Premiered"].loc[nu1[i7]]))
                    ttw25[a28].configure(text= str(cs["Genres"].loc[nu1[i7]]))
                    i7 += 1
                a291 = 12
                for a29 in range(18):
                    ttw21[a291].configure(text= " ")
                    ttw22[a291].configure(text= " ")
                    ttw23[a291].configure(text= " ")
                    ttw24[a291].configure(text= " ")
                    ttw25[a291].configure(text= " ")
                    a291 += 1
        page1=0
        for a26 in range(30):
            ttw21[a26].configure(text= str(cs["Name"].loc[page1]))
            ttw22[a26].configure(text= str(cs["Episodes"].loc[page1]))
            ttw23[a26].configure(text= str(cs["Score"].loc[page1]))
            ttw24[a26].configure(text= str(cs["Premiered"].loc[page1]))
            ttw25[a26].configure(text= str(cs["Genres"].loc[page1]))
            page1 += 1
        bt14.configure(text="Enter", command=Enter7)
        dropbox["values"] = pa1
        dropbox.current(0)

    def Enter():
        noc = int(dropbox.get())-1
        i = noc*30
        if noc < 585:
            for a19 in range(30):
                ttw21[a19].configure(text= str(cs["Name"].loc[nu1[i]]))
                ttw22[a19].configure(text= str(cs["Episodes"].loc[nu1[i]]))
                ttw23[a19].configure(text= str(cs["Score"].loc[nu1[i]]))
                ttw24[a19].configure(text= str(cs["Premiered"].loc[nu1[i]]))
                ttw25[a19].configure(text= str(cs["Genres"].loc[nu1[i]]))
                i += 1
        if noc == 585:
            for a20 in range(12):
                ttw21[a20].configure(text= str(cs["Name"].loc[nu1[i]]))
                ttw22[a20].configure(text= str(cs["Episodes"].loc[nu1[i]]))
                ttw23[a20].configure(text= str(cs["Score"].loc[nu1[i]]))
                ttw24[a20].configure(text= str(cs["Premiered"].loc[nu1[i]]))
                ttw25[a20].configure(text= str(cs["Genres"].loc[nu1[i]]))
                i += 1
            a211 = 12
            for a21 in range(18):
                ttw21[a211].configure(text= " ")
                ttw22[a211].configure(text= " ")
                ttw23[a211].configure(text= " ")
                ttw24[a211].configure(text= " ")
                ttw25[a211].configure(text= " ")
                a211 += 1

    ttw21 = []
    ttw22 = []
    ttw23 = []
    ttw24 = []
    ttw25 = []
    for a11 in range(30):
        ttw21.append(str("txtw24")+str(a11+1))
        ttw21[a11] = Label(window2, text=" ")
        ttw21[a11].grid(column=4, row=a11+2)
    for a12 in range(30):
        ttw22.append(str("txtw25")+str(a12+1))
        ttw22[a12] = Label(window2, text= " ")
        ttw22[a12].grid(column=5, row=a12+2)
    for a13 in range(30):
        ttw23.append(str("txt26")+str(a13+1))
        ttw23[a13] = Label(window2, text=" ")
        ttw23[a13].grid(column=6, row=a13+2)
    for a14 in range(30):
        ttw24.append(str("txt27")+str(a14+1))
        ttw24[a14] = Label(window2, text=" ")
        ttw24[a14].grid(column=7, row=a14+2)
    for a15 in range(30):
        ttw25.append(str("txt28")+str(a15+1))
        ttw25[a15] = Label(window2, text=" ")
        ttw25[a15].grid(column=8, row=a15+2)

    p = int(len(cs["Name"])/30)
    n = n1 = 0
    pa1 = []
    nu1 = []
    nun = []
    for a18 in range(p+1):
        pa1.append(a18+1)
    for a18 in cs["Name"].index:
        nu1.append(n)
        n+=1
    for a18 in range(len(yr["Un"])):
        nun.append(n1)
        n1 += 1

    bt6 = Button(window2, text="Unknown", command=Unk)
    yrs = 1961
    b = 15
    b1 = 1
    b2 = 2
    com = [
        y1961,y1962,y1963,y1964,y1965,y1966,y1967,y1968,y1969,y1970,y1971,y1972,y1973,y1974,y1975,y1976,
        y1977,y1978,y1979,y1980,y1981,y1982,y1983,y1984,y1985,y1986,y1987,y1988,y1989,y1990,y1991,y1992
        ,y1993,y1994,y1995,y1996,y1997,y1998,y1999,y2000,y2001,y2002,y2003,y2004,y2005,y2006,y2007,y2008
        ,y2009,y2010,y2011,y2012,y2013,y2014,y2015,y2016,y2017,y2018,y2019,y2020,y2021
        ]
    
    bott = []
    for a101 in range(61):
        bott.append("bt"+str(b))
        b+=1
    for a102 in range(61):
        bott[a102] = Button(window2, text=yrs,command=com[a102])
        if a102 <= 30:
            bott[a102].grid(column=0,row=b1)
            b1+=1
        if a102 > 30:
            bott[a102].grid(column=1,row=b2)
            b2+=1
        yrs += 1
    bt13 = Button(window2, text="All", command=All)
    # bt11 = Button(window2, text="Back", command=Back)
    dropbox = Combobox(window2)
    dropbox["values"] = pa1
    dropbox.current(0)
    bt14 = Button(window2, text="Enter",command=Enter)
    # bt12 = Button(window2, text="Next",command=Next)
    txtw201 = Label(window2, text="Anime Name")
    txtw202 = Label(window2, text="Episodes")
    txtw203 = Label(window2, text="Score")
    txtw204 = Label(window2, text="Premiered")
    txtw205 = Label(window2, text="Genres")

    page=0
    for a16 in range(30):
        ttw21[a16].configure(text= str(cs["Name"].loc[page]))
        ttw22[a16].configure(text= str(cs["Episodes"].loc[page]))
        ttw23[a16].configure(text= str(cs["Score"].loc[page]))
        ttw24[a16].configure(text= str(cs["Premiered"].loc[page]))
        ttw25[a16].configure(text= str(cs["Genres"].loc[page]))
        page += 1
        
    bt6.grid(column=1, row=1)
    bt13.grid(column=0, row=0)
    # bt11.grid(column=1, row=0)
    dropbox.grid(column=2, row=0)
    # bt12.grid(column=3, row=0)
    bt14.grid(column=2, row=1)
    txtw201.grid(column=4, row=1)
    txtw202.grid(column=5, row=1)
    txtw203.grid(column=6, row=1)
    txtw204.grid(column=7, row=1)
    txtw205.grid(column=8, row=1)
    window2.mainloop()

tt0 = []
tt2 = []
tt4 = []
tt6 = []
for a3 in range(10):
    tt0.append(str("txt0")+str(a3+4))
    tt0[a3] = Label(window, text=" ")
    tt0[a3].grid(column=0, row=a3+4)
for a4 in range(10):
    tt2.append(str("txt2")+str(a4+4))
    tt2[a4] = Label(window, text= " ")
    tt2[a4].grid(column=2, row=a4+4)
for a5 in range(10):
    tt4.append(str("txt4")+str(a5+4))
    tt4[a5] = Label(window, text=" ")
    tt4[a5].grid(column=4, row=a5+4)
for a6 in range(10):
    tt6.append(str("txt6")+str(a6+4))
    tt6[a6] = Label(window, text=" ")
    tt6[a6].grid(column=6, row=a6+4)

txt1 = Label(window, text="Anime List/Random",font=35)
txt2 = Label(window, text="------>", font=("Arial Bold",20))
txt3 = Label(window, text="------>", font=("Arial Bold",20))
bt1 = Button(window, text="Random",command=RandomAnime)
bt2 = Button(window, text="Anime List",command=AnimeList)

txt1.grid(column=1, row=0)
txt2.grid(column=3, row=0)
txt3.grid(column=3, row=1)
bt1.grid(column=5, row=0)
bt2.grid(column=5, row=1)

window.title("Anime List/Random")
# window.geometry("1000x400")
window.mainloop()