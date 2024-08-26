import numpy as np
from tkinter import*

x = [3,4,5,6,7]
y = [5,19,23,14,18]

def f(x):
    return (x**2-4*x+1)

horiAxes = []
vertAxes = []
coordinates = []

xMin = min(x)
xMax = max(x)
graphHoriMin = 1.25*xMin - 0.25*xMax
graphHoriMax = 1.25*xMax - 0.25*xMin
horiRange = graphHoriMax - graphHoriMin
horiParameter = 400/horiRange
yMin = min(y)
yMax = max(y)
graphVertMin = 1.25*yMin - 0.25*yMax
graphVertMax = 1.25*yMax - 0.25*yMin
vertRange = graphVertMax - graphVertMin
vertParameter = 400/vertRange

graphWindow = Tk()
graphWindow.title("Graph Window")
graphWindow.geometry("600x600")
myCanvas = Canvas(graphWindow,width=600,height=600,bg="white")
myCanvas.pack(pady=20)
myCanvas.create_line(100,500,500,500,fill="black")
myCanvas.create_line(100,100,100,500,fill="black")
myCanvas.create_line(100,100,93,120,fill="black")
myCanvas.create_line(100,100,107,120,fill="black")
myCanvas.create_line(500,500,480,493,fill="black")
myCanvas.create_line(500,500,480,507,fill="black")

class axes_1:
    def __init__(self,value):
        self.value = value

class axes_2:
    def __init__(self,value):
        self.value = value

class axes_3:
    def __init__(self,value):
        self.value = value

class coordinate_2d:
    def __init__(self,valueX,valueY,label1,label2):
        self.valueX = valueX
        self.valueY = valueY
        self.label = label1 + "," + label2
        self.color = (255,255,255)
        self.graphX = 100 + self.valueX * horiParameter - graphHoriMin * horiParameter
        self.graphY = 500 - self.valueY * vertParameter + graphVertMin * vertParameter

        #Change the color of the point
    def clrChange(self,color):
            self.color = color
        #Change the coordinate of the point
    def valueChange(self,value1,value2):
            self.valueX = value1
            self.valueY = value2
    def plot(self):
        GraphX = 100 + (self.valueX - graphHoriMin) * horiParameter
        GraphY = 500 - (self.valueY - graphVertMin) * vertParameter
        myCanvas.create_oval(GraphX - 5, GraphY - 5, GraphX + 5, GraphY + 5, fill='black')

def plot_2d(list1,list2):
    for index in range(0,len(list1)):
        
        # objectify each of the coordinates and the point
        horiAxes.append(axes_1(list1[index]))
        vertAxes.append(axes_2(list2[index]))
        coordinates.append(coordinate_2d(horiAxes[index].value,vertAxes[index].value,"horiAxes"+str(index),"vertAxes"+str(index)))
    
    for index in range(len(coordinates)):
        coordinates[index].plot()

def lineGraph(list1,list2):
    for index in range(0,len(list1)):
        
        # objectify each of the coordinates and the point
        horiAxes.append(axes_1(list1[index]))
        vertAxes.append(axes_2(list2[index]))
        coordinates.append(coordinate_2d(horiAxes[index].value,vertAxes[index].value,"horiAxes"+str(index),"vertAxes"+str(index)))
    
    for index in range(len(coordinates)):
        coordinates[index].plot()

    for index in range(len(coordinates)-1):
        myCanvas.create_line(coordinates[index].graphX,coordinates[index].graphY,coordinates[index+1].graphX,coordinates[index+1].graphY,fill="red")

lineGraph(x,y)

graphWindow.mainloop()