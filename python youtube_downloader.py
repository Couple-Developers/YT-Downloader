import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import yt_dlp

def download_video():
    url = url_entry.get()
    download_type = download_type_var.get()  # Get the selected download type

    # Set options based on download type
    if download_type == "video":
        ydl_opts = {
            'format': 'bestvideo[height<=?1080]+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
        }
    elif download_type == "audio":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
        }
    else:
        messagebox.showerror("Error", "Please select a download type.")
        return

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', None)
            messagebox.showinfo("Success", f"{download_type.capitalize()} downloaded: {video_title}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("YouTube Downloader")

# Set window size
root.geometry("630x360")

# Load and set the background image
try:
    background_image = Image.open("background.jpg")  # Ensure this path is correct
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)
except Exception as e:
    messagebox.showerror("Error", f"Failed to load background image: {str(e)}")

# Create and place the URL label and entry
url_label = tk.Label(root, text="YouTube URL:", bg="#e1e1e1", font=("Helvetica", 14))
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50, font=("Helvetica", 12))
url_entry.pack(pady=5)

# Create and place download type options
download_type_var = tk.StringVar(value="video")  # Default to video

video_radio = tk.Radiobutton(root, text="Download Video", variable=download_type_var, value="video", bg="#e1e1e1", font=("Helvetica", 12))
video_radio.pack(anchor='w', padx=20, pady=5)

audio_radio = tk.Radiobutton(root, text="Download Audio", variable=download_type_var, value="audio", bg="#e1e1e1", font=("Helvetica", 12))
audio_radio.pack(anchor='w', padx=20, pady=5)

# Create and place the download button
download_button = tk.Button(root, text="Download", command=download_video, bg="#4CAF50", fg="white", font=("Helvetica", 14))
download_button.pack(pady=20)

# Run the GUI event loop
root.mainloop()
