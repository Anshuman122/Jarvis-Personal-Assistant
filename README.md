# 🧠 Jarvis - Python Voice Assistant

**Jarvis** is a personal voice assistant built in Python that responds to voice commands to perform a variety of desktop automation tasks. It can open applications, access websites, fetch IP address, search Wikipedia, send emails, play music, control the webcam, and much more — all through your voice.

---

## 🚀 Features

- 🎤 Converts voice to text using SpeechRecognition and Google API
- 🗣️ Responds with speech via `pyttsx3` text-to-speech engine
- 📂 Opens system applications like Notepad, Command Prompt, Camera
- 🌐 Searches Google, YouTube, and Wikipedia
- 🎶 Plays local music and YouTube videos
- 📧 Sends emails using SMTP
- 🌍 Fetches your current IP address
- 💤 Can be shut down via voice command

---

## 🛠️ Technologies Used

- **Python 3.x**
- `pyttsx3` – Text-to-speech conversion
- `speech_recognition` – Voice-to-text input
- `pyaudio` – Audio input stream
- `opencv-python` – Webcam control
- `wikipedia` – Wikipedia API integration
- `requests` – Fetching public IP
- `webbrowser` – Opening websites
- `pywhatkit` – Playing YouTube videos via voice
- `smtplib` – Sending emails

---

## 📁 Directory Setup

Make sure the following directories exist or are updated in the script:

- Music Folder: Update the `music_dir` path to point to your local music folder.
- Notepad Path: Confirm the correct path for Notepad based on your OS version.

---

## 🔧 Setup Instructions

1. Clone this repository:
```bash
git clone https://github.com/yourusername/jarvis-voice-assistant.git
cd jarvis-voice-assistant

2.Install dependencies:

pip install pyttsx3 SpeechRecognition pyaudio wikipedia pywhatkit opencv-python requests


⚠️ You may need to install pyaudio manually depending on your system:

pip install pipwin
pipwin install pyaudio

3.Run the assistant:

python jarvis.py


📌 Commands You Can Say
"Open Notepad"

"Open Command Prompt"

"Open Camera"

"Play Music"

"Search Wikipedia for [topic]"

"Open [YouTube/Facebook/Google/Instagram/GeeksforGeeks]"

"Play songs on YouTube"

"Send email"

"Go to sleep"



📬 Contact
Anshuman Kumar Nidhi
📧 anshumankumarnidhi5170@gmail.com


