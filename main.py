import os
import sys

import yt_dlp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")


def download_mp3(url: str) -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(OUTPUT_DIR, "%(title)s.%(ext)s"),
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else input("Pega el link de YouTube: ").strip()

    if not url:
        print("No ingresaste ninguna URL.")
        sys.exit(1)

    try:
        download_mp3(url)
    except yt_dlp.utils.DownloadError as error:
        print(f"No se pudo descargar el audio: {error}")
        sys.exit(1)

    print(f"Descarga completa. Revisa la carpeta '{OUTPUT_DIR}'.")


if __name__ == "__main__":
    main()
