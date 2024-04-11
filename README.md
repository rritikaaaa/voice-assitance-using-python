# voice-assitance-using-python

This is a simple virtual voice assistant built using Python and Jupyter Notebook. The assistant, named "Prajana Kalpa" or "Kalpa," can perform various tasks based on voice commands.

# Features
Voice Recognition: Utilizes the SpeechRecognition library to recognize voice commands from the user.
Text-to-Speech: Uses the pyttsx3 library to convert text responses into speech.
Task Automation: Performs various tasks based on user commands, including:
Playing videos on YouTube.
Providing current time.
Searching Wikipedia for information.
Opening websites in a web browser.
Opening applications like Microsoft Teams and Command Prompt.
Displaying jokes.
Providing IP address information.
Getting the current temperature of a specific location.
News Update: Fetches top headlines news from Inshorts website.
# Technologies Used
Python
Jupyter Notebook
SpeechRecognition
pyttsx3
pywhatkit
datetime
wikipedia
webbrowser
os
pyjokes
subprocess
cv2 (OpenCV)
requests
BeautifulSoup
# How to Use
Open the Jupyter Notebook file containing the code.
Run the notebook.
Once the assistant is initialized, it will greet the user and await commands.
Speak clearly and give commands to the assistant.
The assistant will perform the requested task or provide the requested information.
# Dependencies
Make sure you have the necessary libraries installed. You can install them using pip:

bash
Copy code
pip install SpeechRecognition pyttsx3 pywhatkit wikipedia opencv-python-headless pyjokes requests beautifulsoup4
# Notes
Some functionalities like webcam access (open camera) might require additional permissions and may not work as expected on all systems.
The assistant relies on an active internet connection for certain tasks such as fetching news and temperature information.
You may need to customize file paths for opening specific applications based on your system configuration.
