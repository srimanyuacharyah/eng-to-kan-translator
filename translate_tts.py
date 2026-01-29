#!/usr/bin/env python3
import argparse
import os
from deep_translator import GoogleTranslator
from gtts import gTTS


def translate_and_tts(text: str, out_path: str, play: bool = False):
    translated = GoogleTranslator(source='auto', target='kn').translate(text)
    tts = gTTS(text=translated, lang='kn')
    tts.save(out_path)
    print("Translated text:\n", translated)
    print(f"Saved TTS audio to: {out_path}")
    if play:
        try:
            from playsound import playsound
            playsound(out_path)
        except Exception as e:
            print("Playback failed:", e)


def main():
    parser = argparse.ArgumentParser(description='English → Kannada translator + TTS')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--text', help='Input text in English')
    group.add_argument('-f', '--file', help='Path to text file with English input')
    parser.add_argument('-o', '--out', help='Output MP3 file path', default='output.mp3')
    parser.add_argument('--play', action='store_true', help='Play audio after generation')
    args = parser.parse_args()

    if args.file:
        if not os.path.exists(args.file):
            print('Input file not found:', args.file)
            return
        with open(args.file, 'r', encoding='utf-8') as fh:
            text = fh.read().strip()
    else:
        text = args.text.strip()

    if not text:
        print('No input text provided.')
        return

    translate_and_tts(text, args.out, play=args.play)


if __name__ == '__main__':
    main()
