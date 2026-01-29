# eng-to-kan-translator

This project provides a simple web UI that translates English text to Kannada and generates spoken audio (MP3).

Files of interest:
- `app.py` — Flask web application
- `templates/index.html` — web UI
- `static/style.css` — styles
- `translate_tts.py` — CLI translator (optional)
- `requirements.txt` — Python dependencies
- `Dockerfile` — run app in container (recommended if you don't want to install Python locally)

Docker (recommended if you don't want to install Python locally):

Build the image from the project root:

```powershell
docker build -t eng-to-kan-translator:latest .
```

Run the container and publish port 5000:

```powershell
docker run --rm -p 5000:5000 eng-to-kan-translator:latest
```

Open http://localhost:5000 in your browser. The web UI accepts English text, translates to Kannada and returns an MP3 you can play.

Local Python (alternative):

```powershell
# create/activate venv
python -m venv .venv
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
.\.venv\Scripts\Activate.ps1

# install deps and run
pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

Notes:
- The app uses `googletrans` (unofficial) and `gTTS` which require network access.
- If `googletrans` fails often, consider switching to a paid translation API (Google Cloud Translate) for reliability.

Build image via GitHub Actions (no Docker locally)
------------------------------------------------
If you can't run Docker locally, you can trigger the included GitHub Actions workflow which will build the image on GitHub's runners and produce a downloadable image tarball.

1. Push your repo to GitHub.
2. In GitHub, go to Actions → "Build Docker image and upload" → Run workflow.
3. After the workflow completes, download the artifact `eng-to-kan-translator-image` (a `.tar`).
4. Load it locally with Docker:

```powershell
docker load -i eng-to-kan-translator.tar
docker run --rm -p 5000:5000 eng-to-kan-translator:latest
```
# eng-to-kan-translator

This project provides a simple web UI that translates English text to Kannada and generates spoken audio (MP3).

Files of interest:
- `app.py` — Flask web application
- `templates/index.html` — web UI
- `static/style.css` — styles
- `translate_tts.py` — CLI translator (optional)
- `requirements.txt` — Python dependencies
- `Dockerfile` — run app in container (recommended if you don't want to install Python locally)

Docker (recommended if you don't want to install Python locally):

Build the image from the project root:

```powershell
docker build -t eng-to-kan-translator:latest .
```

Run the container and publish port 5000:

```powershell
docker run --rm -p 5000:5000 eng-to-kan-translator:latest
```

Open http://localhost:5000 in your browser. The web UI accepts English text, translates to Kannada and returns an MP3 you can play.

Local Python (alternative):

```powershell
# create/activate venv
python -m venv .venv
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
.\.venv\Scripts\Activate.ps1

# install deps and run
pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

Notes:
- The app uses `googletrans` (unofficial) and `gTTS` which require network access.
- If `googletrans` fails often, consider switching to a paid translation API (Google Cloud Translate) for reliability.
# eng-to-kan-translator