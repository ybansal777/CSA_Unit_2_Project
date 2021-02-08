#Import all necessary libraries
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
import csv
import numpy as np


#Creates the window needed to run the program
root = tk.Tk()
root.geometry("750x550")

#Used to collect the filenames the user enters
surface_var = tk.StringVar()
ocean_var = tk.StringVar()

#Creates list for dates
date_list = ["2/1","2/2","2/3","2/4","2/5","2/6","2/7"]

#Creates blank dataframe with correct headers
df = pd.DataFrame(columns=['Date', 'Surface Temp (F)', 'Ocean Temp (F)'])

#Fills in the date column for the dataframe
df['Date'] = date_list

#Graph function handles the matplotlib library using user inputs
def graph():
    #Gets user entry
    surface=surface_var.get()
    ocean=ocean_var.get()

    #print("The surface file is: " + surface)
    #print("The ocean file is: " + ocean)

    #Makes text box empty to allow for more entries
    surface_var.set("")
    ocean_var.set("")

    #Reads files from user entry
    data1 = pd.read_csv(surface)
    data2 = pd.read_csv(ocean)

    #Graph data model which averages data
    for ind in df.index:
        if not df['Surface Temp (F)'][ind] > 0:
            df['Surface Temp (F)'][ind] = data1['Temperature(F)'][ind]
        else:
            df['Surface Temp (F)'][ind] = (df['Surface Temp (F)'][ind] + data1['Temperature(F)'][ind])/(2)
        if not df['Ocean Temp (F)'][ind] > 0:
            df['Ocean Temp (F)'][ind] = data2['Temperature(F)'][ind]
        else:
            df['Ocean Temp (F)'][ind] = (df['Ocean Temp (F)'][ind] + data2['Temperature(F)'][ind])/(2)

    #print(df)

    #Calculates correlation coefficient
    surface_list = df['Surface Temp (F)'].tolist()
    ocean_list = df['Ocean Temp (F)'].tolist()
    surface_simple = np.array(surface_list)
    ocean_simple = np.array(ocean_list)
    correlation = np.corrcoef(surface_simple, ocean_simple)
    correlation = correlation[0][1]
    print("The correlation coefficient for the data is about " + str(correlation))

    #Interprets correlation coefficient
    if correlation == 1:
        print("This means there is a complete direct relationship between Surface and Ocean Temperature")
    elif correlation >= 0.8:
        print("This means there is a strong direct relationship between Surface and Ocean Temperature")
    elif correlation >= 0.5:
        print("This means there is a moderate direct relationship between Surface and Ocean Temperature")
    elif correlation > 0:
        print("This means there is a weak direct relationship between Surface and Ocean Temperature")
    elif correlation == 0:
        print("This means there is no relationship between Surface and Ocean Temperature")
    elif correlation > -0.5:
        print("This means there is a weak inverse relationship between Surface and Ocean Temperature")
    elif correlation > -0.8:
        print("This means there is a moderate inverse relationship between Surface and Ocean Temperature")
    elif correlation > -1:
        print("This means there is a strong inverse relationship between Surface and Ocean Temperature")
    elif correlation == -1:
        print("This means there is a complete inverse relationship between Surface and Ocean Temperature")

    #Plots data with title and axis labels
    df.plot()
    plt.suptitle('Alaska Surface vs Ocean Temperature', fontsize=15)
    plt.xlabel("Date")
    plt.ylabel("Temperature (F)")
    plt.xticks(df.index, df['Date'])

    #Displays graph
    plt.show()




#Title label
title = tk.Label(
    root,
    text="Data Analysis",
    justify="center",
    font=("Times New Roman", 48),
    pady=10
)

#Title image
titleImage = tk.PhotoImage(
    file="datatitle.png"
)

#Image placed as a label
image = tk.Label(
    root,
    image = titleImage
)

#Group description
subtitle = tk.Label(
    root,
    text="A Simple Introduction by Tejas, Yash, Tameem, and Rohan",
    justify="center",
    font=("Times New Roman", 18),
    pady=10
)

#Label for surface data text field
surface_label = tk.Label(
    root,
    text = 'Surface Data',
    font=('calibre',10, 'bold')
)

#Surface data text field
surface_entry = tk.Entry(
    root,
    textvariable = surface_var,
    font=('calibre',10,'normal')
)

#Label for ocean data text field
ocean_label = tk.Label(
    root,
    text='Ocean Data',
    font=('calibre',10,'bold')
)

#Ocean data text field
ocean_entry = tk.Entry(
    root,
    textvariable = ocean_var,
    font=('calibre',10,'normal')
)

#Graph button
graph_btn=tk.Button(
    root,
    text = 'Graph',
    justify="center",
    command = graph
)

#Organizing all elements on the window
title.grid(row=0)
image.grid(row=1)
subtitle.grid(row=2)
surface_label.grid(row=3,column=0)
surface_entry.grid(row=3,column=1)
ocean_label.grid(row=4,column=0)
ocean_entry.grid(row=4,column=1)
graph_btn.grid(row=6)

#Displays the window
root.mainloop()
