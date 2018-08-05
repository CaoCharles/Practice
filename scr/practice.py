from tkinter import *

root = Tk()


canvas = Canvas(root,width = 400,height = 300)


###global clounm


curwho= 1 ##1 yellow -1 blue
over   = False


num = 10
xcount = (400/num)
ycount = (300/num)


winpos = [[0 for col in range(11)]for row in range(11)]
#print(winpos)


def xycheck(xline,yline,csum):
    global curwho,winpos


    xtmp = xline
    ytmp = yline
    while xtmp >= 0:
        #print('whowin while2',xtmp)
        xtmp = xtmp -1
        if winpos[xtmp][yline] == curwho:
            csum = csum + 1
        else:
            break


    xtmp = xline
    while xtmp <= 10:
        #print('whowin while3',xtmp)
        xtmp = xtmp + 1
        if winpos[xtmp][yline] == curwho:
            csum = csum + 1
        else:
            break
    return csum






def udcheck(xline,yline,csum):
    global curwho,winpos


    xtmp = xline
    ytmp = yline
    while ytmp >= 0:
        #print('whowin while2',ytmp)
        ytmp = ytmp -1
        if winpos[xline][ytmp] == curwho:
            csum = csum + 1
        else:
            break


    ytmp = yline
    while ytmp <= 10:
        #print('whowin while3',ytmp)
        ytmp = ytmp + 1
        if winpos[xline][ytmp] == curwho:
            csum = csum + 1
        else:
            break
    return csum




def lwcheck(xline,yline,csum):
    global curwho,winpos
    xtmp = xline
    ytmp = yline
    while ytmp >= 0 and xtmp>=0:
        #print('whowin while2',xtmp,ytmp)
        ytmp = ytmp -1
        xtmp = xtmp -1
        if winpos[xtmp][ytmp] == curwho:
            csum = csum + 1
        else:
            break


    xtmp = xline
    ytmp = yline
    while ytmp <= 10 and xtmp<=10:
        #print('whowin while3',xtmp,ytmp)
        ytmp = ytmp + 1
        xtmp = xtmp + 1
        if winpos[xtmp][ytmp] == curwho:
            csum = csum + 1
        else:
            break
    return csum


def rwcheck(xline,yline,csum):
    global curwho,winpos
    xtmp = xline
    ytmp = yline
    while ytmp<=10 and xtmp>=0:
        #print('whowin while2',xtmp,ytmp)
        ytmp = ytmp +1
        xtmp = xtmp -1
        if winpos[xtmp][ytmp] == curwho:
            csum = csum + 1
        else:
            break


    xtmp = xline
    ytmp = yline
    while ytmp >= 0 and xtmp<=10:
        #print('whowin while3',xtmp,ytmp)
        ytmp = ytmp - 1
        xtmp = xtmp + 1
        if winpos[xtmp][ytmp] == curwho:
            csum = csum + 1
        else:
            break
    return csum




def winmessage():
    global curwho
    if curwho == 1:
        msg = 'Red player Win'
    else:
        msg = 'Blue player Win'
    messagebox.showinfo(title='Gameover',message = msg)
    




##判断胜负
def whowin(xline,yline):
    global winpos,curwho,xyIsover,over
    #print('whowin begin',xline)
    csum = 1
    xyIsover = False
    #print('whowin while1 csum is:',csum)
    #print('Isover is:',xyIsover)


    csum1 = xycheck(xline,yline,csum)
    csum2 = udcheck(xline,yline,csum)
    csum3 = lwcheck(xline,yline,csum)
    csum4 = rwcheck(xline,yline,csum)


    ctmp = (csum1 if csum1>csum2 else csum2)
    ctmp = (ctmp if ctmp>csum3 else csum3)
    ctmp = (ctmp if ctmp>csum4 else csum4)


    if ctmp >= 5:
        over = True
        return curwho
    else:
        return 0


                    


##绘制棋子
def pcricle(x,y,size,color):
    canvas.create_oval(x,y,x+size,y+size,fill = color)


##确定事件位置调用绘制
def paint(event):
    global curwho,over,xcount,ycount,winpos
    if over:
        return
    col = 'blue'
    if curwho == 1:
        col = 'red'


    ###标识每个可绘点的状态，防止多次重绘
    #print('eventx is :\n ,eventy is :\n',event.x,event.y)
    #print('xcount is:ycount is :',xcount,ycount)
    x = event.x
    y = event.y
    xpos = 0
    ypos = 0
    numx = int(x/xcount)
    numy = int(y/ycount)


    if x - numx*xcount <= xcount/3:
        xpos = numx*xcount
    elif x - numx*xcount > xcount/3 and x - numx*xcount < xcount*2/3:
        return
    else:
        xpos = (numx+1)*(xcount)


    if y - numy*ycount <= ycount/3:
        ypos = numy*ycount
    elif y - numy*ycount > ycount/3 and y - numy*ycount < ycount*2/3:
        return
    else:
        ypos = (numy+1)*(ycount)


    #print('xpos is :\n ,ypos is :\n',xpos,ypos)


    ##如果当前的位置已经下棋子了，不绘图，返回
    if winpos[int(xpos/xcount)][int(ypos/ycount)] != 0:
        return 0
    
    pcricle(xpos - xcount*0.3,ypos -xcount*0.3,xcount*0.6,col)
    
    ##设置位置为已经记录，1表示red，-1表示blue
    xline = int(xpos/xcount)
    yline = int(ypos/ycount)
    if curwho == 1:
        winpos[xline][yline] = 1
    else:
        winpos[xline][yline] = -1
    #print(winpos)


    #print('here ok')
    win = whowin(xline,yline)
    if win != 0:
        winmessage()
        return -1
    else:
        curwho = curwho*(-1)
        return 0
    
#end paint




img = PhotoImage(file = 't01b24a8ad021f824a2.gif')
canvas.create_image(200,0,image = img,anchor = 'n',tags = 't1')






for line in range(0,num):
    xline = 'x%d'%line
    canvas.create_line(line*xcount,0,line*xcount,300,fill = '#FFFF00',tags = xline)
    canvas.tag_bind(xline,'<Button-1>',paint)
    #pcricle(line*xcount+5,2,xcount*0.65,'#FFFF00')
    


for line in range(0,num):
    yline = 'y%d'%line
    canvas.create_line(0,ycount*line,400,ycount*line,fill = '#FFFF00',tags = yline)
    canvas.tag_bind(yline,'<Button-1>',paint)






canvas.pack(side= LEFT,expand =YES,fill = BOTH)


root.geometry('400x300+500+300')
root.title('Line5')
root.resizable(False,False)
root.mainloop()



#其中在加载图片为随意找的一个



#实现的是最低级的五子棋实现，目前只可以在本机人人对弈，接下来会尝试实现本机人机对战