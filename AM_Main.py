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

        def topic_button_event(self, topic):
            topic_selected = topic
            pas= app.topic_pojector
            pas(topic_selected)

        #Proof_Event
        def Proof_button_event():
            topic_selected = "Proof"
            pas= app.topic_pojector
            pas(topic_selected)
        #AlgebraFunctions_Event
        def AlgebraFunctions_button_event():
            topic_selected = "Alegebra and Functions"
            pas= app.topic_pojector
            pas(topic_selected)

        #CoordinateGeometry_Event
        def CoordinateGeometry_button_event():
            topic_selected = "Coordinate Geometry"
            pas= app.topic_pojector
            pas(topic_selected)

        #SeriesSequence_Event
        def SeriesSequence_button_event():
            topic_selected = "Series and Sequences"
            pas= app.topic_pojector
            pas(topic_selected)

        #Trigonometry_Event
        def Trigonometry_button_event():
            topic_selected = "Trigonometry"
            pas= app.topic_pojector
            pas(topic_selected)

        #Logarithms_Event
        def Logarithms_button_event():
            topic_selected = "Logarithms"
            pas= app.topic_pojector
            pas(topic_selected)
            
        #Differentiation_Event
        def Differentiation_button_event():
            topic_selected = "Differentation"
            pas= app.topic_pojector
            pas(topic_selected)

        #Integration_Event
        def Integration_button_event():
            topic_selected = "Integration"
            pas= app.topic_pojector
            pas(topic_selected)

        #NumericalMethods_Event
        def NumericalMethods_button_event():
            topic_selected = "Numerical Methods"
            pas= app.topic_pojector
            pas(topic_selected)

        #Vectors_Event
        def Vectors_button_event():
            topic_selected = "Vectors"
            pas= app.topic_pojector
            pas(topic_selected)
            

        super().__init__(master, **kwargs)

        self.topic_selected=""

        title_font =("Helvetica",30,'bold')

        self.label = customtkinter.CTkLabel(self, text="Topics", width=343, height=1275,anchor="n", font=title_font)
        self.label.pack(padx=10, pady=10)

        Topic_list=["Proof", "Algebra and Function", "Coordinate Geometry"]

        for i in range (0, len(Topic_list)):
            y = 0.14+0.09*i
            button = customtkinter.CTkButton(self, text=Topic_list[i], command=lambda:topic_button_event(self, Topic_list[i]), width=343, height=70, corner_radius=0)
            button.pack(padx=0, pady=0)
            button.place(relx=0.5, rely=y, anchor="s")
            
        #Proof
       #Proofbutton = customtkinter.CTkButton(self, text="Proof", command=Proof_button_event, width=343, height=70, corner_radius=0)
      #  Proofbutton.pack(padx=0, pady=0)
          #Proofbutton.place(relx=0.5, rely=0.14, anchor="s")
#
       # Algebra and Functions
     #  AlgebraFunctionsbutton = customtkinter.CTkButton(self, text="Algebra and Functions", command=Proof_button_event, width=343, height=70, corner_radius=0)
        #AlgebraFunctionsbutton.pack(padx=0, pady=0)
      #  AlgebraFunctionsbutton.place(relx=0.5, rely=0.23, anchor="s")

        #Coordinate Geometry
      #  CoordinateGeometry = customtkinter.CTkButton(self, text="Coordinate Geometry", command=CoordinateGeometry_button_event, width=343, height=70, corner_radius=0)
      #  CoordinateGeometry.pack(padx=0, pady=0)
      #  CoordinateGeometry.place(relx=0.5, rely=0.32, anchor="s")

        #Series and Sequences
        SeriesSequencebutton = customtkinter.CTkButton(self, text="Series and Sequences", command=SeriesSequence_button_event, width=343, height=70, corner_radius=0)
        SeriesSequencebutton.pack(padx=0, pady=00)
        SeriesSequencebutton.place(relx=0.5, rely=0.41, anchor="s")

        #Trigonometry
        Trigonometrybutton = customtkinter.CTkButton(self, text="Trigonometry", command=Trigonometry_button_event, width=343, height=70, corner_radius=0)
        Trigonometrybutton.pack(padx=0, pady=0)
        Trigonometrybutton.place(relx=0.5, rely=0.5, anchor="s")

        #Logarithms
        Logarithmsbutton = customtkinter.CTkButton(self, text="Logarithms", command=Logarithms_button_event, width=343, height=70, corner_radius=0)
        Logarithmsbutton.pack(padx=0, pady=0)
        Logarithmsbutton.place(relx=0.5, rely=0.59, anchor="s")

        #Differentiation
        Differentiationbutton = customtkinter.CTkButton(self, text="Differentiation", command=Differentiation_button_event, width=343, height=70, corner_radius=0)
        Differentiationbutton.pack(padx=0, pady=0)
        Differentiationbutton.place(relx=0.5, rely=0.68, anchor="s")

        #Integration
        Integrationbutton = customtkinter.CTkButton(self, text="Integration", command=Integration_button_event, width=343, height=70, corner_radius=0)
        Integrationbutton.pack(padx=0, pady=0)
        Integrationbutton.place(relx=0.5, rely=0.77, anchor="s")

        #Numerical Methods
        NumericalMethodsbutton = customtkinter.CTkButton(self, text="Numerical Methods", command=NumericalMethods_button_event, width=343, height=70, corner_radius=0)
        NumericalMethodsbutton.pack(padx=0, pady=0)
        NumericalMethodsbutton.place(relx=0.5, rely=0.86, anchor="s")

        #Vectors
        Vectorsbutton = customtkinter.CTkButton(self, text="Vectors", command=Vectors_button_event, width=343, height=70, corner_radius=0)
        Vectorsbutton.pack(padx=0, pady=0)
        Vectorsbutton.place(relx=0.5, rely=0.95, anchor="s")
        


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
