import tkinter as tk
import time

def update_clock():
    t = time.asctime(time.localtime(time.time()))
    ta = t.split(' ')
    Day = ta[0]
    Date = ta[1]
    Month = ta[2]
    Year = ta[4]
    RealTime = ta[3]

    # Update the label texts with the current time
    box_a.config(text=Day)
    box_b.config(text=Date)
    box_c.config(text=Month)
    box_d.config(text=Year)
    box_e.config(text=RealTime)

    # Schedule the update_clock function to run again after 1000 milliseconds (1 second)
    root.after(1000, update_clock)

def main():
    global root, box_a, box_b, box_c, box_d, box_e

    # Create the main window
    root = tk.Tk()
    root.geometry("680x250")
    root.title("Digital clock")
    root.configure(bg="light coral")

    # Set minimum and maximum width and height
    root.minsize(680, 250)  # Minimum width and height
    root.maxsize(680, 250)  # Maximum width and height

    # Create labels for A, B, C, D, and E
    

    label_a = tk.Label(root, text="Day", bg="light coral",font="bold")
    label_b = tk.Label(root, text="Date", bg="light coral",font="bold")
    label_c = tk.Label(root, text="Month", bg="light coral",font="bold")
    label_d = tk.Label(root, text="Year", bg="light coral",font="bold")
    label_e = tk.Label(root, text="Time", bg="light coral",font="bold")

    # Create boxes with numbers 1, 2, 3, 4, and RealTime
    box_a = tk.Label(root, text="", relief=tk.SOLID, width=10, height=5,font="bold")
    box_b = tk.Label(root, text="", relief=tk.SOLID, width=10, height=5,font="bold")
    box_c = tk.Label(root, text="", relief=tk.SOLID, width=10, height=5,font="bold")
    box_d = tk.Label(root, text="", relief=tk.SOLID, width=10, height=5,font="bold")
    box_e = tk.Label(root, text="", relief=tk.SOLID, width=10, height=5,font="bold")

    # Center the labels and boxes horizontally and vertically
    label_a.grid(row=0, column=0, padx=10, pady=10)
    box_a.grid(row=1, column=0, padx=10, pady=10)

    label_b.grid(row=0, column=1, padx=10, pady=10)
    box_b.grid(row=1, column=1, padx=10, pady=10)

    label_c.grid(row=0, column=2, padx=10, pady=10)
    box_c.grid(row=1, column=2, padx=10, pady=10)

    label_d.grid(row=0, column=3, padx=10, pady=10)
    box_d.grid(row=1, column=3, padx=10, pady=10)

    label_e.grid(row=0, column=4, padx=10, pady=10)
    box_e.grid(row=1, column=4, padx=10, pady=10)

    # Start the clock update function
    update_clock()

    # Start the GUI main loop
    root.mainloop()

if __name__ == "__main__":
    main()
