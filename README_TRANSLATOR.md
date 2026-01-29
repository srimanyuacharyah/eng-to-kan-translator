# English → Kannada Text-to-Speech Translator

This small Python script translates English text to Kannada and generates speech (MP3) using `googletrans` and `gTTS`.

Installation (recommend inside a virtualenv):

```powershell
python -m pip install -r requirements.txt
```

Basic usage:

Generate `output.mp3` from a text string:

```powershell
python translate_tts.py -t "Hello, how are you?" -o hello_kn.mp3
```

Generate and play (Windows):

```powershell
python translate_tts.py -t "Good morning" -o gm_kn.mp3 --play
```

Use a text file as input:

```powershell
python translate_tts.py -f input.txt -o from_file.mp3
```

Notes:
- `playsound` is used for simple playback; on Windows it should play MP3 files.
- If translation fails, ensure you have network access and the packages installed.
- `googletrans` is an unofficial API wrapper for Google Translate and may sometimes be rate-limited.
