import yt_dlp
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def download_audio(url, output_path="downloads"):
    try:
        # Create output directory if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Configure yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'verbose': False,
            'quiet': False,
        }

        # Download the audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            logger.info(f"Downloading from: {url}")
            ydl.download([url])
            
        logger.info("Download completed successfully!")
        return True

    except Exception as e:
        logger.error(f"Error downloading {url}: {str(e)}")
        return False

def main():
    print("YouTube Music Downloader")
    print("------------------------")
    while True:
        url = input("Enter YouTube URL (or 'q' to quit): ").strip()
        
        if url.lower() == 'q':
            break
            
        download_audio(url)

if __name__ == "__main__":
    main()
