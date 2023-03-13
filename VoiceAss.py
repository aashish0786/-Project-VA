import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to speak a given message
def speak(message):
    engine.say(message)
    engine.runAndWait()

# Define a function to recognize speech and execute a command
def recognize_speech():
    with sr.Microphone() as source:
        print("Speak now!")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print("You said: " + command)
            if "hello" in command:
                speak("Hello! How can I assist you today?")
            elif "what time is it" in command:
                speak("It's currently XX:XX AM/PM.")
            else:
                speak("Sorry, I didn't understand your command.")

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Call the function to start recognizing speech and executing commands
recognize_speech()
