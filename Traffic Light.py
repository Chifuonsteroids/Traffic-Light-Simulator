import tkinter as tk

class Trafficlight:
    def __init__(self, master):
        self.master = master
        self.master.title(" Traffic Light Simulation")

        self.canvas = tk.Canvas(master, width=400, height=600, bg = 'gray') 
        self.canvas.pack()

        #Draw traffic light for cars
        self.canvas.create_text(100, 30, text="Car Traffic Light", font=('Helvetica', 14), fill="white")
        self.red_light = self.canvas.create_oval(50, 50, 150, 150, fill='black')
        self.yellow_light = self.canvas.create_oval(50, 200, 150, 300, fill='black')
        self.green_light = self.canvas.create_oval(50, 350, 150, 450, fill='black')

        #Pedestrians light
        self.canvas.create_text(300, 30, text="Pedestrian Traffic Light", font=('Helvetica', 14), fill="white")
        self.pedestrain_red_light = self.canvas.create_oval(250, 50, 350, 150, fill='black')
        self.pedestrain_green_light = self.canvas.create_oval(250, 200, 350, 300, fill='black')
        self.counter_label = self.canvas.create_text(300, 350, text="", font=('Helvetica', 30), fill="white")

        self.green_counter = 10 #countdown for the green pedestrain light

    def change_light(self):
        #cars have red pedestrains have red(reset phase)
        self.canvas.itemconfig(self.red_light, fill='red')
        self.canvas.itemconfig(self.yellow_light, fill='black')
        self.canvas.itemconfig(self.green_light, fill='black')
        self.canvas.itemconfig(self.pedestrain_red_light, fill='red')
        self.canvas.itemconfig(self.pedestrain_green_light, fill='black')

        self.master.after(2000, self.set_yellow)

    def set_yellow(self):
        #cars have yellow pedestrains have red
        self.canvas.itemconfig(self.red_light, fill='black')
        self.canvas.itemconfig(self.yellow_light, fill='yellow')
        self.master.after(1000, self.set_green_for_pedestrains)

    def set_green_for_pedestrains(self):
        #cars have red pedestrains have green
        self.canvas.itemconfig(self.yellow_light, fill='black')
        self.canvas.itemconfig(self.red_light, fill='red')

        self.canvas.itemconfig(self.pedestrain_red_light, fill='black')
        self.canvas.itemconfig(self.pedestrain_green_light, fill='green')

        self.green_counter = 10
        self.update_counter()

    def update_counter(self):
        if self.green_counter > 0:
            self.canvas.itemconfig(self.counter_label, text=str(self.green_counter))
            self.green_counter -= 1
            self.master.after(1000, self.update_counter)
        else:
            self.canvas.itemconfig(self.counter_label, text="")
            self.canvas.itemconfig(self.pedestrain_green_light, fill='black')
            self.canvas.itemconfig(self.pedestrain_red_light, fill='red')
            self.set_green_for_cars()

    def set_green_for_cars(self):
        #cars have green pedestrains have red
        self.canvas.itemconfig(self.red_light, fill='black')
        self.canvas.itemconfig(self.green_light, fill='green')
        self.master.after(2000, self.change_light)

root = tk.Tk()
app = Trafficlight(root)
root.mainloop()        
