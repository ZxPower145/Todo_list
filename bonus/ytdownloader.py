import tkinter as tk
import customtkinter as ctk
from pytube import YouTube


def downaudio():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        audio = ytObject.streams.get_audio_only()

        title.configure(text=ytObject.title, text_color="aqua")
        finishLabel.configure(text="")

        audio.download()
        finishLabel.configure(text="Download complete", text_color="aqua")
    except:
        finishLabel.configure(text="Invalid Link!", text_color="red")


def downvid():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="aqua")
        finishLabel.configure(text="")

        video.download()
        finishLabel.configure(text="Download complete", text_color="aqua")
    except:
        finishLabel.configure(text="Invalid Link!", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # Update progress bar:
    progressBar.set(float(percentage_of_completion) / 100)


# Sys settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

# App frame
app = ctk.CTk()
app.geometry("720x480")
app.title("YouTube downloader")

# Adding UI
title = ctk.CTkLabel(app, text="Inset a YT link", text_color="orange")
title.pack(padx=10, pady=10)

# Link input
url_var = tk.StringVar()
link = ctk.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack(padx=10, pady=10)

# Finished Downloading
finishLabel = ctk.CTkLabel(app, text="")
finishLabel.pack()

# Progress %
pPercentage = ctk.CTkLabel(app, text="0%")
pPercentage.pack()
progressBar = ctk.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download btn
btnaudio = ctk.CTkButton(app, fg_color="#99CB0E", text="Audio", text_color="black" ,command=downaudio)
btnvideo = ctk.CTkButton(app, fg_color="#99CB0E", text="Video", text_color="black", command=downvid)
btnaudio.pack(padx=20, pady=20)
btnvideo.pack(padx=20, pady=20)

# Run app (as a loop)
app.mainloop()
