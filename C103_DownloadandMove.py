import time 
import os 
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir ="D:/whitehatlessons/TA/PYTHON/C102_assets-main"
to_dir=":/whitehatlessons/TA/PYTHON/C102_imageonly"


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(event)



event_handler = FileMovementHandler()

observer =Observer()
observer.schedule(event_handler,from_dir,recursive=True)
observer.start()

while True:
    time.sleep(2)
    print("running...")