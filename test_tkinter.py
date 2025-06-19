print("Starting test...")

try:
    print("Importing tkinter...")
    from tkinter import *
    print("Tkinter imported successfully!")
    
    print("Creating window...")
    root = Tk()
    root.title("Test Window")
    root.geometry("300x200")
    print("Window created!")

    label = Label(root, text="If you see this, tkinter is working!", font=("Arial", 14))
    label.pack(pady=50)

    button = Button(root, text="Click me!", command=lambda: print("Button clicked!"))
    button.pack()

    print("Starting mainloop...")
    root.mainloop()
    print("Mainloop ended.")
    
except Exception as e:
    print(f"ERROR: {e}")
    print("Tkinter failed to work!")

print("Test finished.") 