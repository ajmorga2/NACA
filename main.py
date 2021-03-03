from tkinter import *
from functools import partial

def points(event):
    #Get current contents in loan amount textbox
    loan = loanAmt.get()
    #concatinate loan amount + event.char and multiply by .01 to get point value
    pointValue = int(loan + event.char) * .01
    #delete contents in 'one point' entry and insert point value
    onePointEntry.delete(0, 'end')
    dollarAmount= onePointEntry.insert(END,pointValue)

# function created to create dynamic relationship between current & desired interest rate
def differenceValue(event, x):
    current = currentInt.get()
    desired = desiredInt.get()

    #if user is making changes to desired interest rate run this code
    if x == True:
        #concatinate desired + event and then subratract from
        difference = float(current) - float(desired + event.char)
        differenceEntry.delete(0, 'end')
        differenceEntry.insert(END, float(difference))
    #if user is making changes to current interest rate run this code
    else:
        difference = float(current + event.char) - float(desired)
        differenceEntry.delete(0, 'end')
        differenceEntry.insert(END, float(difference))


def total(*args, selection=NONE):
    term = selection.get()
    if term == '30':
        percentage = .25
        point = float(difference.get()) / percentage
        pointEntry.delete(0, 'end')
        pointEntry.insert(END, point)
        #Multiply point * points needs to buy down for total buy down cost
        total = float(buyDownPoints.get()) * float(onePoint.get())
        totalCostEntry.delete(0, 'end')
        totalCostEntry.insert(END, total)
    else:
        percentage = .50
        point = float(difference.get()) / percentage
        pointEntry.delete(0, 'end')
        pointEntry.insert(END, point) 
        total = float(buyDownPoints.get()) * float(onePoint.get())
        totalCostEntry.delete(0, 'end')
        totalCostEntry.insert(END, total)






root = Tk()

#StringVar variables
option1 = StringVar()
option2 = StringVar()

onePoint = StringVar()

loanAmt = StringVar()

currentInt = StringVar()

desiredInt = StringVar()

difference = StringVar()

buyDownPoints = StringVar()



#Labels
loanAmtLabel = Label(root, text='Loan Amount')
onePointLabel = Label(root, text='One Point')
currentIntLabel = Label(root, text='Current INT.')
desiredIntLabel = Label(root, text='Desired INT.')
diffrenceLabel = Label(root, text='Diffrence')
termMenuLabel = Label(root, text='Term')
pointLabel = Label(root, text='Point')
totalCostLabel = Label(root, text='Total Buydown Cost')



# label screen placement
loanAmtLabel.grid(column=0, row=0)
onePointLabel.grid(column=0, row=1)
currentIntLabel.grid(column=0, row=2)
desiredIntLabel.grid(column=0, row=3)
diffrenceLabel.grid(column=0, row=4)
termMenuLabel.grid(column=0, row=5)
pointLabel.grid(column=0, row=6)
totalCostLabel.grid(column=0, row=7)

#list & stringvar for option menu
terms = ['15','30']
termVar = StringVar()
termVar.set(terms[1])


#Entry boxes
loanAmtEntry = Entry(root, textvariable=loanAmt)
onePointEntry = Entry(root, textvariable=onePoint)
currentIntEntry = Entry(root, textvariable=currentInt)
desiredIntEntry = Entry(root, textvariable=desiredInt)
differenceEntry = Entry(root, textvariable=difference)
termMenu = OptionMenu(root, termVar, *terms)
pointEntry = Entry(root, textvariable=buyDownPoints )
totalCostEntry = Entry(root, )

#Bindings & traces
loanAmtEntry.bind('<Key>', points)
desiredIntEntry.bind('<Key>', lambda event, x=True: differenceValue(event,x))
currentIntEntry.bind('<Key>', lambda event, x=False: differenceValue(event,x))
termVar.trace('w', partial(total, selection=termVar))

#Entry screen placement
loanAmtEntry.grid(column=1, row=0)
onePointEntry.grid(column=1, row=1)
currentIntEntry.grid(column=1, row=2)
desiredIntEntry.grid(column=1, row=3)
differenceEntry.grid(column=1, row=4)
termMenu.grid(column=1, row=5)
pointEntry.grid(column=1, row=6)
totalCostEntry.grid(column=1, row=7)


root.mainloop()

#mortgage = int(input('type in your mortgage'))

#pointValue = mortgage * .01

#currRate = int(input('current interest rate'))

#desiredRate = int(input('current desired rate'))

#difference = currRate - desiredRate

#pointsToBuyDown= difference / .025

#costToBuyDown = pointValue * pointsToBuyDown



