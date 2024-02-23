import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognizer and text-to-speech converter
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-us')
            print("User said:", query)
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, I'm unable to access the Google API.")
            return ""

# Function to respond to user commands
def assistant():
    while True:
        query = listen()

        if "hello" in query:
            speak("Hello! How can I assist you today?")
            print("Hello! How can I assist you today?")

        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
            print(f"The current time is {current_time}")

        elif "date" in query:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}")
            print(f"Today's date is {current_date}")

        elif "search" in query:
            speak("What would you like me to search for?")
            search_query = listen()
            if search_query:
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(url)
                speak(f"Here are the search results for {search_query}")
                print(f"Here are the search results for {search_query}")

        elif "exit" in query:
            speak("Goodbye!")
            print("Goodbye!")
            break

        else:
            speak("Sorry, I'm not sure how to help with that.")

if __name__ == "__main__":
    speak("Hello! I'm your voice assistant. How can I assist you today?")
    assistant()
