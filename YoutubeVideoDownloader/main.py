#pip install pytube

from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url,save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True,file_extension="mp4")
        highest_res_Stream = streams.get_highest_resolution()
        highest_res_Stream.download(output_path=save_path)
        print("Video downloaded succesfully!")
        
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
        
    return folder

        
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    
    video_url = input("Please enter a Youtube url: ")
    save_directory = open_file_dialog()
    
    if save_directory:
        print("Started download...")
        download_video(video_url,save_directory)
    else:
        print("Invalid save location. Please select a folder")

    
    


