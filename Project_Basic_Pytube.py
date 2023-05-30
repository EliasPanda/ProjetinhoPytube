from tkinter import *
from pytube import *
from pytube import YouTube
import customtkinter, tkinter
from tkinter import *
from PIL import Image

# Criando tela
tela = customtkinter.CTk()


my_image = customtkinter.CTkImage(light_image=Image.open('imgs/youtube.png'),
                                    size=(130,60))
LabelImagem = customtkinter.CTkLabel(
                           tela, text='', image=my_image).place(x=80, y=20)



tela.title('Download Youtube')
largura = 300
altura = 300
largura_tela = tela.winfo_screenwidth()
altura_tela = tela.winfo_screenheight()
posX = largura_tela / 2 - largura / 2
posY = altura_tela / 2 - altura  / 2
tela.geometry("%dx%d+%d+%d"%(largura, altura, posX, posY))
tela._set_appearance_mode('System')

def baixarMP4():
    YouTube(video.get()).streams.first().download()
    yt = YouTube('http://youtube.com')
    yt.streams
    yt.title
    filter(progressive=True, file_extension='mp4')


video = customtkinter.CTkEntry(tela)
video.place(x=80,y=100)

customtkinter.CTkButton(tela, text="Baixar MP4",fg_color='#8B008B',hover_color='#4B0082' ,command=baixarMP4).place(x=80, y=150)



tela.mainloop()
