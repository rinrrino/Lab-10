solution.py  
`python
#!/usr/bin/env python3
# solution.py — Lab-10 (voice assistant variant 1)
import requests, os, random
import pyttsx3

ENGINE = pyttsx3.init()

def speak(text):
    ENGINE.say(text)
    ENGINE.runAndWait()

def random_dog():
    r = requests.get('https://dog.ceo/api/breeds/image/random', timeout=10)
    j = r.json()
    return j.get('message')

def name_breed_from_url(url):
    # url like https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg
    parts = url.split('/')
    for p in parts:
        if '-' in p:
            return p.split('-')[0]
    return 'unknown'

def main():
    print("Voice assistant (text-mode). Commands: show, save, next, breed, quit")
    cur = None
    while True:
        cmd = input("> ").strip().lower()
        if cmd in ('quit','q'):
            speak("Goodbye")
            break
        if cmd in ('show','next'):
            cur = random_dog()
            print("Image URL:", cur)
            speak("Here is a dog image")
        elif cmd == 'save' and cur:
            fname = 'dog.jpg'
            r = requests.get(cur)
            with open(fname,'wb') as f:
                f.write(r.content)
            print("Saved as", fname)
            speak("Saved image")
        elif cmd == 'breed' and cur:
            b = name_breed_from_url(cur)
            print("Breed (inferred):", b)
            speak(f"The breed is {b}")
        else:
            print("Unknown or nothing to operate. Try show/next/save/breed/quit")

if name == 'main':
    main()
