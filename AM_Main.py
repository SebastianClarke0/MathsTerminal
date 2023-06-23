import customtkinter


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



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("1330x728")
        customtkinter.set_appearance_mode("dark")
        self.grid_rowconfigure(0, weight=1)

        topics = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
        self.scrollable_checkbox_frame = MyScrollableFrame(self, title="Topics", topics=topics, width=300, height=728)
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=10, pady=20)
        
        self.button = customtkinter.CTkButton(self, text="Select Random", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.textbox = customtkinter.CTkTextbox(master=self, width=710, height=200,corner_radius=0)
        self.textbox.grid(row=0, column=1,padx=10, pady=20, sticky="n")
        self.textbox.insert("0.0", "Some example text!\n" * 10)

        self.my_frame = MyFrame(master=self, width=710, height=420)
        self.my_frame.grid(row=0, column=1, padx=20, pady=20, sticky="s")

    def button_callback(self):
        print("checkbox_frame:", self.checkbox_frame.get())
        print("radiobutton_frame:", self.radiobutton_frame.get())



app = App()
app.mainloop()
