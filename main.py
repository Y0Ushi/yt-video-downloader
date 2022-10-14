
from pytube import YouTube

def get_link():
    link = input('yt video link')
    return link

def downloed_video(link):
    yt = YouTube(link)
    title = yt.title
    print('WAITING......' + title)
    yt.streams.filter( progressive='true',file_extension='mp4').order_by('resolation').desc().first().download('folder name')
    print("downloaded......" + title)
    return title

downloed_video(get_link())
