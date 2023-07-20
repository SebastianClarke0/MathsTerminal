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

class sub_topics_frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        def topic_button_event(self, topic):
            topic_selected = topic
            pas= app.topic_pojector
            pas(topic_selected)
        
        title_font =("Helvetica",30,'bold')
        
        self.label = customtkinter.CTkLabel(self, text="Topics", width=343, height=1275,anchor="n", font=title_font)
        self.label.pack(padx=10, pady=10)
        
        Topic_list=["Proof", "Algebra and Function", "Coordinate Geometry", "Series and Sequences", "Trigonometry", "Logarithms", "Differentiation", "Integration", "Numerical Methods", "Vectors"]
        
        def make_command(obj, topic):
            return lambda: topic_button_event(obj, topic)
        
        for i in range (0, len(Topic_list)):
            y = 0.14+0.09*i
            button = customtkinter.CTkButton(self, text=Topic_list[i], command=make_command(self, Topic_list[i]), width=343, height=70, corner_radius=0)
            button.pack(padx=0, pady=0)
            button.place(relx=0.5, rely=y, anchor="s")

            
class topics_frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        def topic_button_event(self, topic):
            topic_selected = topic
            pas= app.topic_pojector
            pas(topic_selected)
        
        title_font =("Helvetica",30,'bold')
        
        self.label = customtkinter.CTkLabel(self, text="Topics", width=343, height=1275,anchor="n", font=title_font)
        self.label.pack(padx=10, pady=10)
        
        Topic_list=["Proof", "Algebra and Function", "Coordinate Geometry", "Series and Sequences", "Trigonometry", "Logarithms", "Differentiation", "Integration", "Numerical Methods", "Vectors"]
        
        def make_command(obj, topic):
            return lambda: topic_button_event(obj, topic)
        
        for i in range (0, len(Topic_list)):
            y = 0.14+0.09*i
            button = customtkinter.CTkButton(self, text=Topic_list[i], command=make_command(self, Topic_list[i]), width=343, height=70, corner_radius=0)
            button.pack(padx=0, pady=0)
            button.place(relx=0.5, rely=y, anchor="s")
        


class Toplevel_window(customtkinter.CTkToplevel):
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
        self.my_frame = topics_frame(master=self, width=343, height=1275)
        self.my_frame.grid(row=0, column=0, padx=0, pady=0, sticky="s")

        #Sub-Topic Selector
        self.my_frame = topics_frame(master=self, width=343, height=1275)
        self.my_frame.grid(row=0, column=0, padx=0, pady=0, sticky="s")

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



app = App()
app.mainloop()
