# Author：Steve

from tkinter import *    # 调用python图形库tkinter接口，tk是一个图像库
import gui_tkMsgBox      # 得把gui_tkMsgBox放到site-packages里才能调用或者放到环境变量？？
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        gui_tkMsgBox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('hello world')
# 主消息循环:
app.mainloop()
