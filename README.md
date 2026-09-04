# YT to MP3

Script en Python que descarga el audio de un video de YouTube y lo convierte
directamente a MP3, usando [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) y
`ffmpeg`. No depende de páginas de terceros ni de apps externas: todo corre
en tu computadora.

Los MP3 se guardan en la carpeta [`outputs/`](outputs).

## Requisitos

1. **Python 3.8 o superior.**
   Revisa tu versión con:
   ```bash
   python3 --version
   ```
   Si no tenés Python, descargalo de https://www.python.org/downloads/

2. **ffmpeg** (necesario para convertir el audio a MP3).
   - **Windows:** descargalo de https://www.gyan.dev/ffmpeg/builds/ (build
     "essentials"), descomprimilo, y agregá la carpeta `bin` al PATH del
     sistema. Otra opción más simple si tenés `winget`:
     ```bash
     winget install ffmpeg
     ```
   - **macOS** (con [Homebrew](https://brew.sh)):
     ```bash
     brew install ffmpeg
     ```
   - **Linux** (Debian/Ubuntu):
     ```bash
     sudo apt update && sudo apt install ffmpeg
     ```
   Para confirmar que quedó instalado:
   ```bash
   ffmpeg -version
   ```

## Instalación del proyecto

1. Descargá o cloná este proyecto y entrá a la carpeta:
   ```bash
   cd Isa-and-Edu-YT-to-MP3
   ```

2. (Opcional pero recomendado) Creá un entorno virtual para no mezclar
   dependencias con otros proyectos de Python:
   ```bash
   python3 -m venv venv
   source venv/bin/activate       # Windows: venv\Scripts\activate
   ```

3. Instalá las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Ejecutá el script:

```bash
python3 main.py
```

Te va a pedir el link del video:

```
Pega el link de YouTube: https://www.youtube.com/watch?v=CrDcSDJYddM
```

También podés pasar el link directamente como argumento, sin que te lo pida:

```bash
python3 main.py "https://www.youtube.com/watch?v=CrDcSDJYddM"
```

Cuando termine vas a ver:

```
Descarga completa. Revisa la carpeta 'outputs'.
```

Y el MP3 va a estar dentro de la carpeta `outputs/`, con el título del video
como nombre de archivo.

> Si pegás un link que además tiene datos de una lista de reproducción (por
> ejemplo `&list=...`), el script solo descarga ese video puntual, no la
> lista completa.

## ¿Cómo funciona?

`main.py` usa `yt_dlp.YoutubeDL` para:
1. Buscar el mejor audio disponible del video (`bestaudio`).
2. Descargarlo.
3. Pasarlo por el postprocesador `FFmpegExtractAudio`, que usa `ffmpeg` para
   convertirlo a MP3 (calidad 192 kbps) y lo deja en `outputs/`.

## Solución de problemas

- **`ModuleNotFoundError: No module named 'yt_dlp'`**
  No corriste `pip install -r requirements.txt`, o lo corriste en un entorno
  virtual distinto al que estás usando para ejecutar `main.py`.

- **`FileNotFoundError` / errores relacionados con `ffmpeg` durante la
  conversión**
  ffmpeg no está instalado o no está en el PATH. Revisá la sección de
  Requisitos y corré `ffmpeg -version` para confirmar.

- **`HTTP Error 403: Forbidden` o "Sign in to confirm you're not a bot"**
  YouTube cambia seguido sus protecciones anti-bot y a veces bloquea
  versiones viejas de `yt-dlp`. Actualizalo así:
  ```bash
  pip install -U yt-dlp
  ```
  Si el error persiste (pasa sobre todo si corrés el script desde un
  servidor/VPS/entorno en la nube en vez de tu PC), puede que necesites
  pasarle cookies de tu navegador para que YouTube confirme que sos una
  persona real:
  ```bash
  python3 -m pip install -U yt-dlp
  yt-dlp --cookies-from-browser chrome -f bestaudio "TU_LINK"
  ```
  (cambiá `chrome` por `firefox`, `edge`, etc. según tu navegador). Esto no
  es necesario en la mayoría de las PCs personales.

- **El nombre del archivo tiene caracteres raros**
  Es el título original del video. Si querés nombres más simples, editá la
  línea `outtmpl` en `main.py`.

## Estructura del proyecto

```
Isa-and-Edu-YT-to-MP3/
├── main.py            # script principal
├── requirements.txt   # dependencias (yt-dlp)
├── outputs/           # acá se guardan los MP3 descargados
└── README.md
```
