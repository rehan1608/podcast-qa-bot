import yt_dlp

def download_audio(youtube_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'podcast_audio.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    print("Download complete!")

if __name__ == "__main__":
    # URL for the specific Elon Musk & Nikhil Kamath WTF podcast
    video_url = "https://www.youtube.com/watch?v=Rni7Fz7208c" 
    download_audio(video_url)