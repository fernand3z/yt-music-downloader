# YouTube Music Downloader

A simple Python script to download audio from YouTube videos using the `yt-dlp` library. The script extracts audio in MP3 format with a preferred quality of 192kbps. It supports downloading both single songs and entire playlists.

## Features

- Downloads audio from YouTube URLs.
- Supports both single videos and playlists.
- Converts audio to MP3 format.
- Saves audio files with proper titles in a specified directory.
- Automatically creates a download directory if it doesn't exist.

## Prerequisites

### 1. Python
Make sure you have Python 3.6 or higher installed. You can download Python from the [official Python website](https://www.python.org/).

### 2. Install Required Libraries
Install the required Python libraries by running:
```bash
pip install yt-dlp
```

### 3. Install FFmpeg
FFmpeg is required for audio extraction and conversion. Install it as follows:
- **Linux (Ubuntu/Debian):**
  ```bash
  sudo apt install ffmpeg
  ```
- **Fedora:**
  ```bash
  sudo dnf install ffmpeg
  ```
- **macOS:**
  ```bash
  brew install ffmpeg
  ```
- **Windows:**
  - Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/).
  - Add FFmpeg to your system's PATH.

## Installation and Running

1. **Clone or Download the Repository**
   ```bash
   git clone https://github.com/yourusername/yt-music-downloader.git
   cd yt-music-downloader
   ```

2. **Set Up the Environment**
   - Ensure you have Python 3.6 or higher installed.
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
     If `requirements.txt` is not available, install `yt-dlp` manually as described above.

3. **Run the Script**
   ```bash
   python downloader.py
   ```

4. **Provide the YouTube URL**
   - For a single song: Enter the YouTube video URL.
   - For a playlist: Enter the YouTube playlist URL.

5. **View Downloads**
   - MP3 files will be saved in the `downloads` directory by default.

### Example
```plaintext
YouTube Music Downloader
------------------------
Enter YouTube URL (or 'q' to quit): https://www.youtube.com/watch?v=dQw4w9WgXcQ
INFO:root:Downloading from: https://www.youtube.com/watch?v=dQw4w9WgXcQ
INFO:root:Download completed successfully!
```

For a playlist:
```plaintext
Enter YouTube URL (or 'q' to quit): https://www.youtube.com/playlist?list=PLxyz123...
INFO:root:Downloading from: https://www.youtube.com/playlist?list=PLxyz123...
INFO:root:Download completed successfully!
```

## Script Overview

### Functions
- `download_audio(url, output_path="downloads")`:
  Downloads audio from the given YouTube URL and saves it as an MP3 file in the specified output path.
  
- `main()`:
  Provides a simple user interface to enter URLs and download audio.

### Logging
The script uses Python's built-in `logging` module to provide informative output during execution.

## Contributing

Contributions are welcome! If you have ideas for improving the script or encounter issues, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This script is for personal use only. Please ensure your usage complies with YouTube's [Terms of Service](https://www.youtube.com/t/terms).
