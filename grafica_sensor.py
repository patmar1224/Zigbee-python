import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime
import datetime
import matplotlib.dates as mdates
def crear_grafica():
    global fig
    global ax1
    style.use('fivethirtyeight')
    fig=plt.figure()
    ax1=fig.add_subplot(111)
    x = ["00:00", "02:00", "04:00", "06:00", "08:00", "10:00", "12:00","14:00", "16:00", "18:00", "20:00", "22:00", "23:59"]
    dates_graf = [datetime.datetime.strptime(h, "%H:%M") for h in x]
    xformater = mdates.DateFormatter('%H:%M')
    ax1.xaxis.set_major_formatter(xformater)
    ax1.set_xlim((min(dates_graf) - datetime.timedelta(hours=1),max(dates_graf) + datetime.timedelta(hours=1)))
    ax1.set(ylabel='Humedad(%)')
    
def animate (i):
    graph_data = open ('ejemplo.txt', 'r').read()
    lines=graph_data.split('\n')
    xs =[]
    ys = []
    for line in lines:
        if len(line)>1:
            y,x=line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs,ys)
    
def pintar_grafica():
    crear_grafica()
    ani=animation.FuncAnimation(fig,animate)
    plt.show()

#pintar_grafica()

        
