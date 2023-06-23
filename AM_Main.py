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

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("1330x728")
        customtkinter.set_appearance_mode("dark")
        self.grid_rowconfigure(0, weight=1)

        #Topics Scroll
        topics = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
        self.scrollable_checkbox_frame = MyScrollableFrame(self, title="Topics", topics=topics, width=300, height=728)
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=10, pady=20)
        
        #Topics Button
        self.button = customtkinter.CTkButton(self, text="Select Random", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        #Text Box
        self.textbox = customtkinter.CTkTextbox(master=self, width=200, height=200,corner_radius=0)
        self.textbox.grid(row=0, column=1,padx=10, pady=20, sticky="nw")
        self.textbox.insert("0.0", "Some example text!\n" * 10)

        #Stats Area
        self.my_frame = MyFrame(master=self, width=710, height=420)
        self.my_frame.grid(row=0, column=1, padx=20, pady=20, sticky="s")

        #Top Level
        self.button_1 = customtkinter.CTkButton(self, text="open toplevel", command=self.open_toplevel)
        self.button_1.grid(row=0, column=1, padx=20, pady=20, sticky="n")

        self.toplevel_window = None


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
