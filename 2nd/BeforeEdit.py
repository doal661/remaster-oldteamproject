# Before Editing Code

from tkinter import *
from tkinter import ttk


def mountains(): #changing
    toplevel=Toplevel()
    toplevel.title("전북의 산")
    toplevel.geometry("400x400")
    toplevel.resizable(False, False)

    
    button0 = Button(toplevel, width = 15, text = "모악산", command = moak)
    button0.pack(side=TOP, padx=20, pady=24) # finish

    button1 = Button(toplevel, width = 15, text = "지리산", command = jiri)
    button1.pack(side=TOP, padx=20, pady=24)

    button2 = Button(toplevel, width = 15, text = "내장산", command = naejang)
    button2.pack(side=TOP, padx=20, pady=24)

    button3 = Button(toplevel, width = 15, text = "마이산", command = maee)
    button3.pack(side=TOP, padx=20, pady=24)

    button4 = Button(toplevel, width = 15, text = "닫기", command = toplevel.destroy)
    button4.pack(side=TOP, padx=20, pady=24)

    toplevel.mainloop()


def moak():
    toplevel=Toplevel()
    toplevel.geometry("400x400")
    toplevel.title("모악산")
    toplevel.resizable(False, False)

    label = Label(toplevel, text="", width=40, height=20)
    label.pack()

    button0= Button(toplevel, width=10, text="닫기", command=toplevel.destroy)
    button0.pack(side=TOP, padx=10, pady=8)

    button1 = Button(toplevel, width = 10, text = "정보", command = moakKeyword)
    button1.pack(anchor = E)

    button2 = Button(toplevel, width=10, text="소개글", command = moakInfo)
    button2.place(x=60, y=137, width=50, height=50)

    button3 = Button(toplevel, width=10, text="장소", command = moakPlace)
    button3.place(x=175, y=137, width=50, height=50)

    button4 = Button(toplevel, width=10, text="맛집", command = moakFood)
    button4.place(x=290, y=137, width=50, height=50)


def moakKeyword():
    toplevel = Toplevel()
    toplevel.geometry("200x120")
    toplevel.title("모악산 정보")
    toplevel.resizable(False, False)
    label = Label(toplevel, width = 40, height = 20, text = "높이 793m")
    label.pack()
    toplevel.mainloop

def moakPlace():
    toplevel = Toplevel()
    toplevel.geometry("300x120")
    toplevel.title("모악산 장소")
    toplevel.resizable(False, False)
    label = Label(toplevel, text="지번)  대한민국 전라북도 김제시, 전주시 완산구", width=40, height=20)
    label.pack()
    toplevel.mainloop()

def moakFood():
    toplevel = Toplevel()
    toplevel.geometry("230x120")
    toplevel.title("모악산 맛집")
    toplevel.resizable(False,False)
    label = Label(toplevel, text="모악산 손두부 ★ 3.7\n\n 모악촌 ★ 4.0", width = 40, height = 20)
    label.pack()
    toplevel.mainloop()


def moakInfo():
    toplevel=Toplevel()
    toplevel.title("모악산")
    toplevel.geometry("500x500")
    toplevel.resizable(False, False)
    

    canvas = Canvas(toplevel, bg = "white", width = 400, height = 300)
    canvas.pack()

    img = PhotoImage(file = "moak.png")

    canvas.create_image(0, 0, anchor = NW, image = img)

    label = Label(toplevel, width = 100, height = 20, text="모악산(母岳山)은 전라북도 김제시와 완주군에 걸쳐있는 높이 793m의 산이다.\n"
                             "1971년 12월 1일에 도립공원으로 지정 되었다.\n"
                             "모악산 도립공원 입구에는 백제 법왕 원년에 창건된 금산사 절이 있다.\n"
                             "2002년 10월 산림청이 모악산을 대한민국 100대 명산 중 하나로 선정하였다.\n")
    
    button = Button(toplevel, width = 10, text="닫기", command = toplevel.destroy)
    button.pack(side=BOTTOM, padx=10, pady=8)

    label.pack(side=BOTTOM)


    toplevel.mainloop()

def jiri():
    toplevel=Toplevel()
    toplevel.geometry("400x400")
    toplevel.title("지리산")
    toplevel.resizable(False, False)

    label = Label(toplevel, text="", width=40, height=20)
    label.pack()

    button0= Button(toplevel, width=10, text="닫기", command=toplevel.destroy)
    button0.pack(side=TOP, padx=10, pady=8)

    button1 = Button(toplevel, width = 10, text = "정보", command = jiriKeyword)
    button1.pack(anchor = E)

    button2 = Button(toplevel, width=10, text="소개글", command=jiriInfo)
    button2.place(x=60, y=137, width=50, height=50)

    button3 = Button(toplevel, width=10, text="장소", command=jiriPlace)
    button3.place(x=175, y=137, width=50, height=50)

    button4 = Button(toplevel, width=10, text="맛집", command=jiriFood)
    button4.place(x=290, y=137, width=50, height=50)

    toplevel.mainloop()

def jiriKeyword():
    toplevel = Toplevel()
    toplevel.geometry("200x120")
    toplevel.title("지리산 정보")
    toplevel.resizable(False, False)
    label = Label(toplevel, width = 40, height = 20, text = "높이 1915m")
    label.pack()

    toplevel.mainloop


def jiriFood():
    toplevel = Toplevel()

    toplevel.geometry("230x120")
    toplevel.title("지리산 맛집")
    toplevel.resizable(False,False)
    label = Label(toplevel, text="지리산거북이산장식 ★ 4.1\n\n 거목효소식당 ★ 4.2", width = 40, height = 20)
    label.pack()

    toplevel.mainloop()

def jiriPlace():
    toplevel = Toplevel()
    toplevel.geometry("300x120")
    toplevel.title("지리산 장소")
    toplevel.resizable(False, False)
    label = Label(toplevel, text="지번)  경상남도 함양군, 산청군, 하동군;\n전라북도 남원시, 전라남도 구례군", width=40, height=20)
    label.pack()
    toplevel.mainloop()



def jiriInfo():
    toplevel=Toplevel()
    toplevel.title("지리산")
    toplevel.geometry("500x500")
    toplevel.resizable(False, False)

    canvas = Canvas(toplevel, bg = "white", width = 400, height = 300)
    canvas.pack()

    img = PhotoImage(file = "jiri.png")

    canvas.create_image(0, 0, anchor = NW, image = img)

    label = Label(toplevel, width = 100, height = 20, text="지리산(智異山)은 경상남도의 하동군, 함양군, 산청군, 전라남도의 구례군, \n"
                             "전라북도의 남원시 등 3개 도, 5개 시군에 걸쳐있는 산이다.\n"
                             "1967년 최초의 대한민국의 국립공원으로 지정되었으며 대한민국에서는\n"
                             "483.022㎢의 가장 넓은 면적을 지닌 산악형 국립공원이다.\n")
    
    button = Button(toplevel, width = 10, text="닫기", command = toplevel.destroy)
    button.pack(side=BOTTOM, padx=10, pady=8)

    label.pack(side=BOTTOM)

    toplevel.mainloop()


def naejang():
    toplevel=Toplevel()
    toplevel.geometry("400x400")
    toplevel.title("내장산")
    toplevel.resizable(False, False)

    label = Label(toplevel, text="", width=40, height=20)
    label.pack()

    button0= Button(toplevel, width=10, text="닫기", command=toplevel.destroy)
    button0.pack(side=TOP, padx=10, pady=8)

    button1 = Button(toplevel, width = 10, text = "정보", command = naejangKeyword)
    button1.pack(anchor = E)

    button2 = Button(toplevel, width=10, text="소개글", command = naejangInfo)
    button2.place(x=60, y=137, width=50, height=50)

    button3 = Button(toplevel, width=10, text="장소", command = naejangPlace)
    button3.place(x=175, y=137, width=50, height=50)

    button4 = Button(toplevel, width=10, text="맛집", command = naejangFood)
    button4.place(x=290, y=137, width=50, height=50)

def naejangKeyword():
    toplevel = Toplevel()
    toplevel.geometry("200x120")
    toplevel.title("내장산 정보")
    toplevel.resizable(False, False)
    label = Label(toplevel, width = 40, height = 20, text = "높이 763m")
    label.pack()
    toplevel.mainloop
    pass

def naejangPlace():
    toplevel = Toplevel()
    toplevel.geometry("300x120")
    toplevel.title("내장산 장소")
    toplevel.resizable(False, False)
    label = Label(toplevel, text="지번)  대한민국 전라북도 정읍시, 순창군;\n전라남도 장성군", width=40, height=20)
    label.pack()
    toplevel.mainloop()

def naejangFood():
    toplevel = Toplevel()

    toplevel.geometry("230x120")
    toplevel.title("내장산 맛집")
    toplevel.resizable(False,False)
    label = Label(toplevel, text="삼일회관 ★ 3.9\n\n 전라회관 ★ 4.8", width = 40, height = 20)
    label.pack()

    toplevel.mainloop()



def naejangInfo():
    toplevel=Toplevel()
    toplevel.title("내장산")
    toplevel.geometry("500x500")
    toplevel.resizable(False, False)

    canvas = Canvas(toplevel, bg = "white", width = 400, height = 300)
    canvas.pack()

    img = PhotoImage(file = "naejang.png")

    canvas.create_image(0, 0, anchor = NW, image = img)

    label = Label(toplevel, width = 100, height = 20, text="내장산(內藏山)은 전라북도 정읍시와 순창군 경계에 있는 산이다.\n" 
                             "호남 지방의 5대 명산(지리산·월출산·천원산·방장산)과 한국 팔경 중 하나로서\n" 
                             "500여 년 전부터 단풍 명소로 널리 알려졌으며, 내장사가 있다.\n" 
                             "1969년 1월 21일 관광지로 널리 지정되었으며 1971년 11월 17일 국립공원으로 지정되었다.\n" 
                             "봄에는 푸른 신록 사이로 피어나는 벚꽃의 아름다움과 여름에는 푸른 산록, \n"
                             "가을은 불타는 단풍, 겨울에는 설경의 아름다움으로 4계절 관광명소이다.\n")
    button = Button(toplevel, width = 10, text="닫기", command = toplevel.destroy)
    button.pack(side=BOTTOM, padx=10, pady=8)

    label.pack(side=BOTTOM)

    toplevel.mainloop()
    
    toplevel.mainloop()

    

def maee():
    toplevel=Toplevel()
    toplevel.geometry("400x400")
    toplevel.title("내장산")
    toplevel.resizable(False, False)

    label = Label(toplevel, text="", width=40, height=20)
    label.pack()

    button0= Button(toplevel, width=10, text="닫기", command=toplevel.destroy)
    button0.pack(side=TOP, padx=10, pady=8)

    button1 = Button(toplevel, width = 10, text = "정보", command = maeeKeyword)
    button1.pack(anchor = E)

    button2 = Button(toplevel, width=10, text="소개글", command = maeeInfo)
    button2.place(x=60, y=137, width=50, height=50)

    button3 = Button(toplevel, width=10, text="장소", command = maeePlace)
    button3.place(x=175, y=137, width=50, height=50)

    button4 = Button(toplevel, width=10, text="맛집", command = maeeFood)
    button4.place(x=290, y=137, width=50, height=50)


def maeeKeyword():
    toplevel = Toplevel()
    toplevel.geometry("200x120")
    toplevel.title("마이산  정보")
    toplevel.resizable(False, False)
    label = Label(toplevel, width = 40, height = 20, text = "높이 687m")
    label.pack()
    toplevel.mainloop
    pass

def maeePlace():
    toplevel = Toplevel()
    toplevel.geometry("300x120")
    toplevel.title("마이산 장소")
    toplevel.resizable(False, False)
    label = Label(toplevel, text="지번)  대한민국 전라북도 진안군", width=40, height=20)
    label.pack()
    toplevel.mainloop()
    pass

def maeeFood():
    toplevel = Toplevel()
    toplevel.geometry("230x120")
    toplevel.title("내장산 맛집")
    toplevel.resizable(False,False)
    label = Label(toplevel, text="마이산풍경식당 ★ 3.8\n\n 백제회관 ★ 3.8", width = 40, height = 20)
    label.pack()

    toplevel.mainloop()
    pass



def maeeInfo():
    toplevel=Toplevel()
    toplevel.title("마이산")
    toplevel.geometry("500x500")
    toplevel.resizable(False, False)

    canvas = Canvas(toplevel, bg = "white", width = 400, height = 300)
    canvas.pack()

    img = PhotoImage(file = "maee.png")

    canvas.create_image(0, 0, anchor = NW, image = img)

    label = Label(toplevel, width = 100, height = 20, text="마이산(馬耳山)은 전라북도 진안군 진안읍에 있는 산이다.\n" 
                             "1979년 10월 16일 도립공원으로 지정되었고,\n2003년 10월 31일 대한민국의 명승 제12호로 지정되었다.\n" 
                             "중생대 후기 약 1억년전까지 호수였으나,\n대홍수시 모래, 자갈 등이 물의 압력에 의하여 이루어진 수성암으로\n" 
                             "약 7천만년 전 지각 변동으로 융기되어 지금의 마이산이 이루어졌으며,\n지금도 민물고기 화석이 간혹 발견된다.\n")
    button = Button(toplevel, width = 10, text="닫기", command = toplevel.destroy)
    button.pack(side=BOTTOM, padx=10, pady=8)

    label.pack(side=BOTTOM)


    toplevel.mainloop()



def sightsee(): #changing
    toplevel=Toplevel()
    toplevel.title("전북의 관광지")
    toplevel.geometry("400x400")
    toplevel.resizable(False, False)

    
    button0 = Button(toplevel, width = 15, text = "덕진공원", command = deokjin)
    button0.pack(side=TOP, padx=20, pady=24) # finish

    button1 = Button(toplevel, width = 15, text = "남원 광한루원", command = kwanghanroo)
    button1.pack(side=TOP, padx=20, pady=24)

    button2 = Button(toplevel, width = 15, text = "경기전", command = kyeongki)
    button2.pack(side=TOP, padx=20, pady=24)

    button3 = Button(toplevel, width = 15, text = "고창읍성", command = gochang)
    button3.pack(side=TOP, padx=20, pady=24)

    button4 = Button(toplevel, width = 15, text = "닫기", command = toplevel.destroy)
    button4.pack(side=TOP, padx=20, pady=24)

    toplevel.mainloop()



def deokjin():
    toplevel=Toplevel()
    toplevel.geometry("400x400")
    toplevel.title("덕진공원")
    toplevel.resizable(False, False)

    label = Label(toplevel, text = "", width = 40, height = 20) #for design
    label.pack()

    button0 = Button(toplevel, width = 10, text = "닫기", command = toplevel.destroy)
    button0.pack(side=TOP, padx=10, pady=8)

    button1 = Button(toplevel, width = 10, text = "키워드", command = deokjinKeyword)
    button1.pack(anchor = E)

    button2 = Button(toplevel, width = 10, text = "소개글", command = deokjinInfo)
    button2.place(x=60, y=137, width = 50, height = 50)

    button3 = Button(toplevel, width = 10, text = "장소", command = deokjinPlace)
    button3.place(x=175, y=137, width = 50, height = 50)

    button4 = Button(toplevel, width = 10, text = "맛집", command = deokjinFood)
    button4.place(x=290, y=137, width = 50, height = 50)

    toplevel.mainloop()

    

def deokjinKeyword():
    toplevel = Toplevel()
    toplevel.geometry("200x120")
    toplevel.title("덕진공원 키워드")
    toplevel.resizable(False, False)

    label = Label(toplevel, width = 40, height = 20, text = "연꽃, 축제, 음악분수, 정원")
    label.pack()

    toplevel.mainloop


def deokjinInfo():
    toplevel=Toplevel()
    toplevel.title("덕진공원 소개글")
    toplevel.geometry("500x500")
    toplevel.resizable(False, False)

    canvas = Canvas(toplevel, bg = "white", width = 400, height = 300)
    canvas.pack()

    img = PhotoImage(file = "deokjin.png")

    canvas.create_image(0, 0, anchor = N, image = img)

    label = Label(toplevel, width = 100, height = 20, text="공원 안에 덕진호라는 거대한 호수가 있으며 그 외에는 팔각정과 큰 철교, 전망대도 있다.\n"
                     "연꽃이 피는 시기에는 호수 한쪽이 온통 연꽃으로 뒤덮혀 사진작가들에게도 인기가 많다.\n"
                     "특히 이 곳은 겨울을 제외한 계절 평일에 하루 3번 30분 동안 음악분수쇼가 열린다.\n"
                     "음악에 맞추어 분수들이 떠오르는데 밤에 하는 분수쇼에서는 조명까지 곁들여진다.\n"
                     "현재 전주천 방향으로 흘러나가는 쪽을 수문으로 막아\n"
                     "수위를 조절하고 있어 인공호수로 보기도 한다.\n")
    button = Button(toplevel, width = 10, text="닫기", command = toplevel.destroy)
    button.pack(side=BOTTOM, padx=10, pady=8)

    label.pack(side=BOTTOM)


    toplevel.mainloop()

def deokjinPlace():
    toplevel = Toplevel()
    toplevel.geometry("300x120")
    toplevel.title("덕진공원 장소")
    toplevel.resizable(False, False)
    label = Label(toplevel, text="지번) 전라북도 전주시 덕진구 권삼득로 390\n\n우편번호) 54895", width=40, height=20)
    label.pack()
    toplevel.mainloop()


def deokjinFood():
    toplevel = Toplevel()
    toplevel.geometry("230x120")
    toplevel.title("덕진공원 맛집")
    toplevel.resizable(False, False)
    label = Label(toplevel, text="옴팡집(백반) ★ 4.3\n\n족보설렁탕(설렁탕) ★ 4.3", width=40, height=20)
    label.pack()
    toplevel.mainloop()


def kwanghanroo():
    toplevel = Toplevel()
    toplevel.geometry("400x400")
    toplevel.title("남원 광한루원")
    toplevel.resizable(False, False)

    label = Label(toplevel, text="", width=40, height=20)
    label.pack()
    button0 = Button(toplevel, width=10, text="닫기", command=toplevel.destroy)
    button0.pack(side=TOP, padx=10, pady=8)

    button1 = Button(toplevel, width=10, text="키워드", command=kwanghanrooKeyword)
    button1.pack(anchor=E)

    button2 = Button(toplevel, width=10, text="소개글", command=kwanghanrooInfo)
    button2.place(x=60, y=137, width=50, height=50)

    button3 = Button(toplevel, width=10, text="장소", command=kwanghanrooPlace)
    button3.place(x=175, y=137, width=50, height=50)

    button4 = Button(toplevel, width=10, text="맛집", command=kwanghanrooFood)
    button4.place(x=290, y=137, width=50, height=50)\

    toplevel.mainloop()
    

def kwanghanrooKeyword():
    toplevel=Toplevel()
    toplevel.geometry("220x120")
    toplevel.title("남원광한루원키워드")
    toplevel.resizable(False, False)

    label = Label(toplevel, text="광한루, 오작교, 완월정, 야경", width=40, height=20)
    label.pack()

    toplevel.mainloop()

def kwanghanrooInfo():
    toplevel=Toplevel()
    toplevel.title("남원 광한루원")
    toplevel.geometry("500x500")
    toplevel.resizable(False, False)

    canvas = Canvas(toplevel, bg = "white", width = 400, height = 300)
    canvas.pack()

    img = PhotoImage(file = "kwanghanroo.png")

    canvas.create_image(0, 0, anchor = NW, image = img)

    label = Label(toplevel, width = 100, height = 20, text="광한루원(廣寒樓苑)은 대한민국 명승 제33호로,\n전라북도 남원시 천거동에 있는 조선시대의 정원이다.\n"
                             "광한루를 중심으로 영주(한라산), 봉래(금강산), 방장(지리산) 등을 뜻하는\n세 개의 삼신산이 있는 호수와 오작교가 있다.\n"
                             "오작교는 해마다 칠월칠석이면 견우와 직녀가 만난다는 안타까운 천상의 사랑을\n"
                             "춘향과 이몽룡을 통해 완성시킨 사랑의 다리이기도 한다.\n"
                             "신선의 세계관과 천상의 우주관을 표현한 우리나라 제일의 누원이라고 알려져있다.\n")
    button = Button(toplevel, width = 10, text="닫기", command = toplevel.destroy)
    button.pack(side=BOTTOM, padx=10, pady=8)

    label.pack(side=BOTTOM)


    toplevel.mainloop()

def kwanghanrooPlace():
    toplevel=Toplevel()
    toplevel.geometry("280x120")
    toplevel.title("남원 광한루원 장소")
    toplevel.resizable(False, False)

    label = Label(toplevel, text="도로명 주소) 전라북도 남원시 금동 요천로 1447\n\n우편번호) 55776", width=40, height=20)
    label.pack()
    
    toplevel.mainloop()

def kwanghanrooFood():
    toplevel=Toplevel()
    toplevel.geometry("230x120")
    toplevel.title("남원 광한루원 맛집")
    toplevel.resizable(False, False)

    label = Label(toplevel, text="광한루석쇠구이(고기집) ★ 4.4\n\n 월매추어탕(추어탕) ★ 4.4", width=40, height=20)
    label.pack()

    toplevel.mainloop()

def kyeongki():
    toplevel=Toplevel()
    toplevel.geometry("400x400")
    toplevel.title("경기전")
    toplevel.resizable(False, False)
    
    label = Label(toplevel, text="", width=40, height=20)
    label.pack()

    button0 = Button(toplevel, width=10, text="닫기", command=toplevel.destroy)
    button0.pack(side=TOP, padx=10, pady=8)

    button1 = Button(toplevel, width=10, text="키워드", command=kyeongkiKeyword)
    button1.pack(anchor=E)

    button2 = Button(toplevel, width=10, text="소개글", command=kyeongkiInfo)
    button2.place(x=60, y=137, width=50, height=50)

    button3 = Button(toplevel, width=10, text="장소", command=kyeongkiPlace)
    button3.place(x=175, y=137, width=50, height=50)

    button4 = Button(toplevel, width=10, text="맛집", command=kyeongkiFood)
    button4.place(x=290, y=137, width=50, height=50)

    toplevel.mainloop()

def kyeongkiKeyword():
    toplevel=Toplevel()
    toplevel.geometry("200x120")
    toplevel.title("경기전 키워드")
    toplevel.resizable(False, False)
    label = Label(toplevel, text="한복, 한옥마을, 전동성당, 역사적인", width=40, height=20)
    label.pack()

    toplevel.mainloop()

def kyeongkiInfo():
    toplevel=Toplevel()
    toplevel.title("경기전")
    toplevel.geometry("500x500")
    toplevel.resizable(False, False)

    canvas = Canvas(toplevel, bg = "white", width = 400, height = 300)
    canvas.pack()

    img = PhotoImage(file = "kyeongki.png")

    canvas.create_image(0, 0, anchor = NW, image = img)

    label = Label(toplevel, width = 100, height = 20, text="전주 경기전 정전(全州 慶基殿 正殿)은 전라북도 전주시 완산구 태조로 44에 있는\n"
                             "조선 왕조의 개창자인 태조(太祖) 이성계(李成桂)의 어진을 모신 건물이다.\n"
                             "경기전은 국보 제317호인 조선 태조 이성계의 어진(御眞)인 조선태조어진을 봉안한 곳이며,\n"
                             "영정을 실제로 모신 정전 건물은 보물 제1578호이다.\n"
                             "경기전 권역은 1991년 사적 제339호로 지정됐다.\n")
    button = Button(toplevel, width = 10, text="닫기", command = toplevel.destroy)
    button.pack(side=BOTTOM, padx=10, pady=8)

    label.pack(side=BOTTOM)


    toplevel.mainloop()


def kyeongkiPlace():
    toplevel=Toplevel()
    toplevel.geometry("280x120")
    toplevel.title("경기전 장소")
    toplevel.resizable(False, False)
    label = Label(toplevel, text="도로명 주소) 전라북도 전주시 완산구 태조로 44\n\n우편번호) 55042", width=40, height=20)
    label.pack()
    toplevel.mainloop()

def kyeongkiFood():
    toplevel=Toplevel()
    toplevel.geometry("230x120")
    toplevel.title("경기전 맛집")
    toplevel.resizable(False, False)
    label = Label(toplevel, text="전동 떡갈비(떡갈비) ★ 4.1\n\n중앙숯불(고기집) ★ 4.1", width=40, height=20)
    label.pack()
    toplevel.mainloop()



def gochang():
    toplevel=Toplevel()
    toplevel.geometry("400x400")
    toplevel.title("고창읍성")
    toplevel.resizable(False, False)

    label = Label(toplevel, text="", width=40, height=20)
    label.pack()

    button0= Button(toplevel, width=10, text="닫기", command=toplevel.destroy)
    button0.pack(side=TOP, padx=10, pady=8)

    button1 = Button(toplevel, width=10, text="키워드", command=gochangKeyword)
    button1.pack(anchor=E)

    button2 = Button(toplevel, width=10, text="소개글", command=gochangInfo)
    button2.place(x=60, y=137, width=50, height=50)

    button3 = Button(toplevel, width=10, text="장소", command=gochangPlace)
    button3.place(x=175, y=137, width=50, height=50)

    button4 = Button(toplevel, width=10, text="맛집", command=gochangFood)
    button4.place(x=290, y=137, width=50, height=50)

    toplevel.mainloop()

def gochangKeyword():
    toplevel=Toplevel()
    toplevel.geometry("200x120")
    toplevel.title("고창읍성 키워드")
    toplevel.resizable(False, False)
    label = Label(toplevel, text="대나무 숲, 공북루, 동양 루, 자연적", width=40, height=20)
    label.pack()
    toplevel.mainloop()
    

def gochangInfo():
    toplevel=Toplevel()
    
    toplevel.title("고창읍성")
    toplevel.geometry("500x500")
    toplevel.resizable(False, False)

    canvas = Canvas(toplevel, bg = "white", width = 400, height = 300)
    canvas.pack()

    img = PhotoImage(file = "gochang.png")

    canvas.create_image(0, 0, anchor = NW, image = img)

    label = Label(toplevel, width = 100, height = 20, text="고창읍성(高敞邑城)은 전라북도 고창군 고창읍에 있는 옛 읍성이다.\n"
                             "1965년 4월 1일 대한민국의 사적 제145호로 지정되었다.\n"
                             "자연석 성곽으로 조선 단종 원년(1453)에 왜침을 막기 위하여 축성했다고도 하고,\n"
                             "숙종 때 완성되었다고도 하나 확실하지 않다.\n"
                             "백제 때 고창 지역을 모량부리로 불렀던 것에서 모양성이라고도 불린다.\n")
    button = Button(toplevel, width = 10, text="닫기", command = toplevel.destroy)
    button.pack(side=BOTTOM, padx=10, pady=8)

    label.pack(side=BOTTOM)


    toplevel.mainloop()

def gochangPlace():
    toplevel=Toplevel()
    toplevel.geometry("280x120")
    toplevel.resizable(False, False)
    label = Label(toplevel, text="지번) 전라북도 고창군 고창읍 성두리 286\n\n우편번호) 56426", width=40, height=20)
    label.pack()
    toplevel.mainloop()

def gochangFood():
    toplevel=Toplevel()
    toplevel.geometry("230x120")
    toplevel.title("고창읍성 맛집")
    toplevel.resizable(False, False)
    label = Label(toplevel, text="석정회관(오리고기) ★ 4.2\n\n천변밥집(백반) ★ 4.2", width=40, height=20)
    label.pack()
    toplevel.mainloop()




def ocean():
    toplevel = Toplevel() 

    toplevel.geometry("400x400")
    toplevel.title("전라도의 바다")
    toplevel.resizable(False, False)


    button0 = Button (toplevel, width=15, text ="변산해수욕장", command = byeonsan)
    button0.pack(side=TOP,padx=20, pady=24)

    button1 = Button (toplevel, width=15, text ="선유도해수욕장", command = seonyudo)
    button1.pack(side=TOP,padx=20, pady=24)

    button2 = Button (toplevel, width=15, text ="모항갯벌해수욕장", command = mohang)
    button2.pack(side=TOP,padx=20, pady=24)

    button3 = Button (toplevel, width=15, text ="구시포해수욕장", command = goosipo)
    button3.pack(side=TOP,padx=20, pady=24)

    button4 = Button (toplevel, width=15, text ="닫기", command = toplevel.destroy)
    button4.pack(side=TOP,padx=20, pady=24)

    toplevel.mainloop()


def byeonsanKeyword():
    toplevel = Toplevel()

    toplevel.geometry("200x120")
    toplevel.title("변산해수욕장 키워드")
    toplevel.resizable(False,False)
    label = Label(toplevel, text="해변, 맛조개, 오토캠핑, 깨끗한", width = 40, height = 20)
    label.pack()

    toplevel.mainloop()

def byeonsanInfo():
    toplevel = Toplevel()
    toplevel.geometry("500x500")
    toplevel.title("변산해수욕장 소개글")
    toplevel.resizable(False,False)

    canvas = Canvas(toplevel, bg = "white", width = 400, height = 300)
    canvas.pack()

    img = PhotoImage(file = "byeonsan.png")

    canvas.create_image(0, 0, anchor = W, image = img) # don't touch!
    
    label = Label(toplevel, text="부안읍에서 남서쪽으로 6 km 떨어진 곳에 있다.\n희고 고운 모래로 된 긴 해안에 푸른 소나무가 숲을 이루었으며\n 조석간만(潮汐干滿)의 차도 심하지 않아 대천 만리포 해수욕장과 함께\n 황해안의 3대 해수욕장의 하나로 꼽힌다\n 그리고 해수욕장 남쪽은 ‘내변산(內邊山)’으로서\n 한국 8경(景)의 하나가 되는 명승지이다\n1988년 변산반도 전체를 묶어 국립공원으로 지정하였다\n내변산 중에는 백제가 멸망한 후 독립군들이 백제의 부흥운동을 벌이던\n주류성(周留城)을 비롯하여 그 유적이 적지 않다.", width = 75, height = 30)

    button = Button(toplevel, width = 10, text="닫기", command = toplevel.destroy)
    button.pack(side=BOTTOM, padx=10, pady=8)

    label.pack()

    toplevel.mainloop()

def byeonsanPlace():
    toplevel = Toplevel()

    toplevel.geometry("300x120")
    toplevel.title("변산해수욕장 장소")
    toplevel.resizable(False,False)
    label = Label(toplevel, text="지번) 전라북도 부안군 변산면 대항리 567\n\n우편번호) 579-852", width = 40, height = 20)
    label.pack()

    toplevel.mainloop()

def byeonsanFood():
    toplevel = Toplevel()
    toplevel.geometry("230x120")
    toplevel.title("변산해수욕장 맛집")
    toplevel.resizable(False,False)
    label = Label(toplevel, text="변산가마솥통닭(치킨) ★ 4.34\n\n카페쿠숑(디저트) ★ 4.33", width = 40, height = 20)
    label.pack()
                 

def byeonsan(): 
    toplevel = Toplevel()

    toplevel.geometry("400x400")
    toplevel.title("변산해수욕장")
    toplevel.resizable(False, False)
    
    label = Label(toplevel, text="", width =40, height =20)
    label.pack()
    
    button0 = Button(toplevel, width=10, text ="닫기", command = toplevel.destroy)
    button0.pack(side=TOP,padx=10, pady=8)

    button1 = Button(toplevel, width=10, text ="키워드", command = byeonsanKeyword)
    button1.pack(anchor=E)

    button2 = Button(toplevel, width=10, text ="소개글", command = byeonsanInfo)
    button2.place(x=60, y=137, width=50, height=50)

    button3 = Button(toplevel, width=10, text ="장소", command = byeonsanPlace)
    button3.place(x=175, y=137, width=50, height=50)

    button4 = Button (toplevel, width=10, text ="맛집", command = byeonsanFood)
    button4.place(x=290, y=137, width=50, height=50)

    toplevel.mainloop()

def seonyudoKeyword():
    toplevel = Toplevel()

    toplevel.geometry("220x120")
    toplevel.title("선유도해수욕장 키워드")
    toplevel.resizable(False,False)
    label = Label(toplevel, text="섬, 해변, 유람선, 쾌적한, 갯벌체험", width = 40, height = 20)
    label.pack()

    toplevel.mainloop()

def seonyudoInfo():
    toplevel = Toplevel()
    toplevel.geometry("500x500")
    toplevel.title("선유도해수욕장 소개")
    toplevel.resizable(False,False)

    canvas = Canvas(toplevel, bg = "white", width = 400, height = 300)
    canvas.pack()

    img = PhotoImage(file = "seonyudo.png")

    canvas.create_image(0, 0, anchor = NW, image = img)
    
    label = Label(toplevel, text="전라북도 군산시 옥도면 선유도에 있는 해수욕장으로\n모래사장이 10여 리에 걸쳐 있다 하여 일명 명사십리해수욕장으도 불린다\n선유도의 선유8경인 명사십리·선유낙조·평사낙안·망주폭포·장자어화·월영단풍과\n삼도귀범·무산십이봉 가운데에도 단연 백미로 꼽히는 곳이다.", width = 75, height = 30)

    button = Button(toplevel, width = 10, text="닫기", command = toplevel.destroy)
    button.pack(side=BOTTOM, padx=10, pady=8)

    label.pack()

    toplevel.mainloop()
    
def seonyudoPlace():
    toplevel = Toplevel()

    toplevel.geometry("230x120")
    toplevel.title("선유도해수욕장 장소")
    toplevel.resizable(False,False)
    label = Label(toplevel, text="지번) 전북 군산시 옥도면 선유도리", width = 40, height = 20)
    label.pack()
    toplevel.mainloop()
    
def seonyudoFood():
    toplevel = Toplevel()

    toplevel.geometry("230x120")
    toplevel.title("선유도해수욕장 맛집")
    toplevel.resizable(False,False)
    label = Label(toplevel, text="선유도 선유횟집(생선회) ★ 4.12\n\n 남도밥상(백반) ★ 4.26", width = 40, height = 20)
    label.pack()

    toplevel.mainloop()

def seonyudo(): 
    toplevel = Toplevel()

    toplevel.geometry("400x400")
    toplevel.title("선유도해수욕장")
    toplevel.resizable(False, False)
    
    label = Label(toplevel, text="", width =40, height =20)
    label.pack()

    button0 = Button(toplevel, width=10, text ="닫기", command = toplevel.destroy)
    button0.pack(side=TOP,padx=10, pady=8)
    
    button1 = Button(toplevel, width=10, text ="키워드", command = seonyudoKeyword)
    button1.pack(anchor=E)

    button2 = Button(toplevel, width=10, text ="소개글", command = seonyudoInfo)
    button2.place(x = 60, y=137, width=50, height=50)

    button3 = Button(toplevel, width=10, text ="장소", command = seonyudoPlace)
    button3.place(x = 175, y=137, width=50, height=50)

    button4 = Button(toplevel, width=10, text ="맛집", command = seonyudoFood)
    button4.place(x = 290, y=137, width=50, height=50)
    
    toplevel.mainloop()
    
def mohangKeyword():
    toplevel = Toplevel()

    toplevel.geometry("200x120")
    toplevel.title("모항갯벌해수욕장 키워드")
    toplevel.resizable(False,False)
    label = Label(toplevel, text="캠핑, 해변, 갯벌체험, 아담한", width = 40, height = 20)
    label.pack()

    toplevel.mainloop()

def mohangInfo():
    toplevel = Toplevel()
    toplevel.geometry("500x500")
    toplevel.title("모항갯벌해수욕장 소개글")
    toplevel.resizable(False,False)

    canvas = Canvas(toplevel, bg = "white", width = 400, height = 300)
    canvas.pack()

    img = PhotoImage(file = "mohang.png")

    canvas.create_image(0, 0, anchor = W, image = img)

    label = Label(toplevel, text="내변산(內邊山)과 외변산이 마주치는 지점의 바닷가에 자연 조성된 자그마한 해수욕장으로\n아담한 백사장과 울창한 소나무밭이 아름다운 조화를 이룬다.\n규모는 작지만 서해의 다른 해변과 달리 물이 빠져 해변이 드러나도 하얀 모래가 가득하고\n해수욕장 곳곳에서 바다낚시와 선상낚시를 즐길 수 있다.", width = 100, height = 30)

    button = Button(toplevel, width = 10, text="닫기", command = toplevel.destroy)
    button.pack(side=BOTTOM, padx=10, pady=8)

    label.pack()

    toplevel.mainloop()

def mohangPlace():
    toplevel = Toplevel()
    toplevel.geometry("280x120")
    toplevel.title("모항갯벌해수욕장 장소")
    toplevel.resizable(False,False)
    label = Label(toplevel, text="지번) 전라북도 부안군 변산면 도청리 203-45\n\n우편번호) 579-853", width = 40, height = 20)
    label.pack()

    toplevel.mainloop()

def mohangFood():
    toplevel = Toplevel()

    toplevel.geometry("230x120")
    toplevel.title("모항갯벌해수욕장 맛집")
    toplevel.resizable(False,False)
    label = Label(toplevel, text="모항횟집(생선회) ★ 4.22\n\n카페티라(디저트) ★ 4.69", width = 40, height = 20)
    label.pack()

    toplevel.mainloop()

def mohang(): 
    toplevel = Toplevel()

    toplevel.geometry("400x400")
    toplevel.title("모항갯벌해수욕장")
    toplevel.resizable(False, False)

    label = Label(toplevel, text="", width =40, height =20)
    label.pack()
    
    button0 = Button(toplevel, width=10, text ="닫기", command = toplevel.destroy)
    button0.pack(side=TOP, padx=10, pady=8)

    button1 = Button(toplevel, width=10, text ="키워드", command = mohangKeyword)
    button1.pack(anchor = E)

    button2 = Button(toplevel, width=10, text ="소개글", command = mohangInfo)
    button2.place(x = 60, y=137, width=50, height=50)

    button3 = Button(toplevel, width=10, text ="장소", command = mohangPlace)
    button3.place(x = 175, y=137, width=50, height=50)

    button4 = Button(toplevel, width=10, text ="맛집", command = mohangFood)
    button4.place(x = 290, y=137, width=50, height=50)

    toplevel.mainloop()

def goosipoKeyword():
    toplevel = Toplevel()
    toplevel.geometry("200x120")
    toplevel.title("구시포해수욕장 키워드")
    toplevel.resizable(False,False)
    label = Label(toplevel, text="해변, 캠핑, 바다낚시, 편안한", width = 40, height = 20)
    label.pack()

    toplevel.mainloop()


def goosipoInfo():
    toplevel = Toplevel()
    toplevel.geometry("500x500")
    toplevel.title("구시포해수욕장 소개글")
    toplevel.resizable(False,False)

    canvas = Canvas(toplevel, bg = "white", width = 400, height = 300)
    canvas.pack()

    img = PhotoImage(file = "goosipo.png")

    canvas.create_image(0, 0, anchor = NW, image = img)
    
    label = Label(toplevel, text="전라북도 고창군 상하면 자룡리에 있는 해수욕장으로\n 길이 약 1.7km, 폭 2m의 백사장과 우거진 송림, 완만한 경사, 특이한 지형을 이룬다.\n특히 바닷물이 빠지면 백사장이 아주 단단해지고,\n나지막한 야산으로 둘러싸여 있어 아늑하며, 갯벌 한 점 없이 고운 백사장이 돋보이는 곳이다.\n편의시설이 잘 갖추어져 있고, 오토캠핑을 할 수도 있으며, 야영을 하기도 좋은 환경이다.\n해수욕장 주변의 고창읍성, 선운사, 선운산도립공원, 석정온천, 동호해수욕장을 비롯해\n세계적인 문화재로 평가받고 있는 지석묘군도 함께 둘러볼 만하다.", width = 100, height = 30)

    button = Button(toplevel, width = 10, text="닫기", command = toplevel.destroy)
    button.pack(side=BOTTOM, padx=10, pady=8)

    label.pack()

    toplevel.mainloop()

def goosipoPlace():
    toplevel = Toplevel()

    toplevel.geometry("280x120")
    toplevel.title("구시포해수욕장 장소")
    toplevel.resizable(False,False)
    label = Label(toplevel, text="지번) 전북 고창군 상하면 자룡리", width = 40, height = 20)
    label.pack()

    toplevel.mainloop()

def goosipoFood():
    toplevel = Toplevel()

    toplevel.geometry("230x120")
    toplevel.title("구시포해수욕장 맛집")
    toplevel.resizable(False,False)
    label = Label(toplevel, text="서해바다(생선회) ★ 0.0\n\n구시포하우스(쭈꾸미) ★ 4.4", width = 40, height = 20)
    label.pack()

    toplevel.mainloop()

    
def goosipo(): 
    toplevel = Toplevel()
    toplevel.geometry("400x400")
    toplevel.title("구시포해수욕장")
    toplevel.resizable(False, False)

    label = Label(toplevel, text="", width = 40, height = 20)
    label.pack()
    
    button0 = Button(toplevel, width=10, text ="닫기", command = toplevel.destroy)
    button0.pack(side=TOP,padx=10, pady=8)

    button1 = Button(toplevel, width=10, text ="키워드", command = goosipoKeyword)
    button1.pack(anchor=E)

    button2 = Button(toplevel, width=10, text ="소개글", command = goosipoInfo)
    button2.place(x = 60, y=137, width=50, height=50)

    button3 = Button(toplevel, width=10, text ="장소", command = goosipoPlace)
    button3.place(x = 175, y=137, width=50, height=50)

    button4 = Button(toplevel, width=10, text ="맛집", command = goosipoFood)
    button4.place(x = 290, y=137, width=50, height=50)

    toplevel.mainloop()



root = Tk()
root.geometry("400x400")
root.title("전라북도 관광지") # 창 이름

label = Label(root, text="원하는 관광지", width = 50, height = 10)
label.pack()

button0 = Button(root, width=10, text="산", command = mountains)
button0.pack(side = TOP, padx = 10, pady = 8)

button1 = Button(root, width=10, text="바다", command = ocean)
button1.pack(side = TOP, padx = 10, pady = 8)

button2 = Button(root, width=10, text="관광지", command = sightsee)
button2.pack(side = TOP, padx = 10, pady = 8)

button3 = Button(root, width=10, text="닫기", command = root.destroy)
button3.pack(side = TOP, padx = 10, pady = 8)

root.mainloop()
