# -*- coding: utf-8 -*-
#import module
import gtk,serial,time
global COM
global BAUD  
#create app use object extends Window
class PyApp(gtk.Window):
    def __init__(self):
        #init program
        super(PyApp,self).__init__()
        try:
            #for window set a icon 
            self.set_icon_from_file("t.png")
        except Exception,e:
            sys.exit(1)
        #close window call
        self.connect("destroy",gtk.main_quit)
        #set title
        self.set_title("Micro Air Monitoring System")
        #set windows size
        self.set_size_request(350,150)
        #set windows position
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_border_width(8)
        #table contain 8*4
        table = gtk.Table(6,5,False)
        table.set_col_spacings(3)
        #com title
        title = gtk.Label("串口设置".decode('utf-8'))
        table.attach(title,0,2,0,1,gtk.FILL,gtk.FILL,0,0)
        #left com set
        com_lab  = gtk.Label("串口".decode('utf-8'))
        table.attach(com_lab,0,1,1,2,gtk.FILL,gtk.SHRINK,1,1)
        com_cb = gtk.combo_box_new_text()
        com_cb.connect("changed",self.com_changed)
        com_cb.append_text('com1')
        com_cb.append_text('com2')
        com_cb.append_text('com3')
        com_cb.append_text('com4')
        com_cb.append_text('com5')
        com_cb.append_text('com6')
        com_cb.append_text('com7')
        table.attach(com_cb,1,2,1,2,gtk.FILL,gtk.SHRINK,1,1)
       
        baud_lab = gtk.Label("波特率".decode('utf-8'))
        table.attach(baud_lab,0,1,2,3,gtk.FILL,gtk.SHRINK,1,1)
        baud_cb = gtk.combo_box_new_text()
        baud_cb.connect("changed",self.baud_changed)
        baud_cb.append_text('4800')
        baud_cb.append_text('9600')
        baud_cb.append_text('19200')
        baud_cb.append_text('38400')
        baud_cb.append_text('57600')
        baud_cb.append_text('115200')
        table.attach(baud_cb,1,2,2,3,gtk.FILL,gtk.SHRINK,1,1)
        
        activate = gtk.Button("Read DATA")
        activate.set_size_request(50,30)
        activate.connect("clicked", self.com_open)
        table.attach(activate,1,2,3,4,gtk.FILL,gtk.SHRINK,1,1)
        #right sensor data
        ti = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        self.data_title = gtk.Label("传感器数据   ".decode('utf-8') )
        table.attach(self.data_title,2,6,0,1,gtk.FILL,gtk.FILL,0,0)

        temp = gtk.Label("温度(oC):".decode('utf-8'))
        self.temp_label = gtk.Label("-")
        table.attach(temp,2,3,1,2,gtk.FILL,gtk.FILL,0,0)
        table.attach(self.temp_label,3,4,1,2,gtk.FILL,gtk.FILL,0,0)
        humi = gtk.Label("湿度(%):".decode('utf-8'))
        self.humi_label = gtk.Label("-")
        table.attach(humi,4,5,1,2,gtk.FILL,gtk.FILL,0,0)
        table.attach(self.humi_label,5,6,1,2,gtk.FILL,gtk.FILL,0,0)
        light = gtk.Label("光照(lx):".decode('utf-8'))
        self.light_label = gtk.Label("-")
        table.attach(light,2,3,2,3,gtk.FILL,gtk.FILL,0,0)
        table.attach(self.light_label,3,4,2,3,gtk.FILL,gtk.FILL,0,0)
        press = gtk.Label("气压(Pa):".decode('utf-8'))
        self.press_label = gtk.Label("-")
        table.attach(press,4,5,2,3,gtk.FILL,gtk.FILL,0,0)
        table.attach(self.press_label,5,6,2,3,gtk.FILL,gtk.FILL,0,0)
        dust = gtk.Label("PM2.5(ug/m3):".decode('utf-8'))
        self.dust_label = gtk.Label("-")
        table.attach(dust,2,3,3,4,gtk.FILL,gtk.FILL,0,0)
        table.attach(self.dust_label,3,4,3,4,gtk.FILL,gtk.FILL,0,0)
        aqi = gtk.Label("AQI:".decode('utf-8'))
        self.aqi_label = gtk.Label("-")
        table.attach(aqi,4,5,3,4,gtk.FILL,gtk.FILL,0,0)
        table.attach(self.aqi_label,5,6,3,4,gtk.FILL,gtk.FILL,0,0)

         
        self.add(table)
        self.show_all()

    def com_changed(self,widget):
        global COM
        COM = widget.get_active_text()
        print COM
    def baud_changed(self,widget):
        global BAUD
        BAUD = int(widget.get_active_text())
        print BAUD
    def com_open(self,widget):
        global t,h,l,p,d,a
        ser = serial.Serial(COM,BAUD)
        print "Serial Reading..."
        line = ser.readline()
        data = line.split(',')
        if(data[0]=='start'):
            t = data[1]
            h = data[2]
            l = data[3]
            p = data[4]
            d = data[5]
            a = data[6]
            ser.close()
            ti = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
            self.data_title.set_label("传感器数据   ".decode('utf-8')+ti)
            self.temp_label.set_label(t)
            self.humi_label.set_label(h)
            self.light_label.set_label(l)
            self.press_label.set_label(p)
            self.dust_label.set_label(d)
            if(a==0):
                aqi = '优'.decode('utf-8')
            elif(a==1):
                aqi = '良'.decode('utf-8')
            elif(a==2):
                aqi = '轻度污染'.decode('utf-8')
            elif(a==3):
                aqi = '中度污染'.decode('utf-8')
            elif(a==4):
                aqi = '重度污染'.decode('utf-8')
            else:
                aqi = '严重污染'.decode('utf-8')
            self.aqi_label.set_label(aqi)
             
        else:
            temp = ser.readline()
    
PyApp()  
gtk.main()
