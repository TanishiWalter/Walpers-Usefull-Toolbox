import customtkinter
import yt_downloader

customtkinter.set_appearance_mode("dark") #system, light, dark
customtkinter.set_default_color_theme("dark-blue") #blue, green, dark-blue

root = customtkinter.CTk()
root.geometry("600x454")

YTDownloaderframe = customtkinter.CTkFrame(master=root)
YTDownloaderframe.pack(pady=150,padx=300,fill="both",expand=True)

YTDownloadLable = customtkinter.CTkLabel(master=YTDownloaderframe,text="YouTube downloader")
YTDownloadLable.pack(pady=30,padx=300)

YTDownloaderInput = customtkinter.CTkEntry(master=YTDownloaderframe,placeholder_text="input URL here")
YTDownloaderInput.pack(pady=30,padx=10)

YTDownloaderInfo = customtkinter.CTkLabel(master=root,text="Nothing is happening rn")
YTDownloaderInfo.pack(pady=30,padx=10)

def downloadYT():
    print(yt_downloader.downloadYouTubeVid(YTDownloaderInput.get()))

YTDownloaderButton = customtkinter.CTkButton(master=YTDownloaderframe,text="Download",command=downloadYT)
YTDownloaderButton.pack(pady=30,padx=10)

root.mainloop()
