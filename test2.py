import customtkinter

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Course")
        self.add("Topics")
        self.add("Sub-Topics")

        # add widgets on tabs
        self.label = customtkinter.CTkLabel(master=self.tab("Course"))
        self.label.grid(row=0, column=0, padx=20, pady=10)


class MyScrollableFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, topics, **kwargs):
        super().__init__(master, label_text=title, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.topics = topics
        self.checkboxes = []

        for i, value in enumerate(self.topics):
            checkbox = customtkinter.CTkButton(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="we")
            self.checkboxes.append(checkbox)
            
class MyFrame(customtkinter.CTkFrame):
            
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #Proof_Event
        def change_topic(topic):
            print(topic)
        #AlgebraFunctions_Event
        self.topic_selected=""

        title_font =("Helvetica",30,'bold')

        self.label = customtkinter.CTkLabel(self, text="Topics", width=343, height=1275,anchor="n", font=title_font)
        self.label.pack(padx=10, pady=10)
        topic_list=["Proof", "Algebra and Function", "Coordinate Geometry", "Series and Sequences","Trigonemetry", "Logarithms", "Differentiation", "Integration", "Numerical Methods", "Vectors"]
        
        for i in range (0, len(topic_list)):
            y = 0.14+0.09*i
            exec("button = customtkinter.CTkButton(self, text=topic_list[i], command=change_topic(topic_list[i]), width=343, height=70, corner_radius=0))")
            button.pack(padx=0, pady=0)
            button.place(relx=0.5, rely=y, anchor="s")


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1275x870")
        self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("1275x870")
        customtkinter.set_appearance_mode("dark")
        self.grid_rowconfigure(0, weight=1)
        

        #Topic Selector
        self.my_frame = MyFrame(master=self, width=343, height=1275)
        self.my_frame.grid(row=0, column=0, padx=0, pady=0, sticky="s")

        #Sub-Topics Scroll
        topics = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
        self.scrollable_checkbox_frame = MyScrollableFrame(self, title="Sub-Topics", topics=topics, width=225, height=1275)
        self.scrollable_checkbox_frame.grid(row=0, column=2, padx=0, pady=0)

        #Stats Area
        self.tab_view = MyTabView(master=self, width=640, height=528)
        self.tab_view.grid(row=0, column=1, padx=10, pady=0, sticky="s")

        #Top Level
        self.button_1 = customtkinter.CTkButton(self, text="Start Review", command=self.open_toplevel, width=40, height=330)
        self.button_1.grid(row=0, column=1, padx=20, pady=20, sticky="ne")
        self.toplevel_window = None

    def topic_pojector(self, topic_selected):
        title_font =("Helvetica",30,'bold')
        self.label2 = customtkinter.CTkLabel(self, text=(topic_selected), width=500, height=60,font=title_font)
        self.label2.place(relx=0.3,rely=0)
        print(topic_selected)

    def sub_topic_pojector(self, sub_topic_selected):
        print("")


    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    
    def button_callback(self):
        print("checkbox_frame:", self.checkbox_frame.get())
        print("radiobutton_frame:", self.radiobutton_frame.get())



app = App()
app.mainloop()
