import os
import tkinter
import customtkinter

def Delete():
    os.system('curl -X DELETE {}'.format(Webhook.get()))
        
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

App = customtkinter.CTk()
App.resizable(False, False)
App.geometry("450x185")
App.title("Webhook Deleter")

Title = customtkinter.CTkLabel(App, text = "Insert a Webhook", font = ("cascadia mono", 20))
Title.pack(padx = 10, pady= 10)

Webhook_Url = tkinter.StringVar()
Webhook = customtkinter.CTkEntry(App, font = ("cascadia mono", 13), width = 350, height = 40, textvariable = Webhook_Url)
Webhook.pack(padx = 10, pady= 10)

Delete_Webhook = customtkinter.CTkButton(App, text = "Delete Webhook", font = ("cascadia mono", 20), width = 350, height = 40, command = Delete)
Delete_Webhook.pack(padx = 10, pady = 10)

App.mainloop()
