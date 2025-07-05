import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 = male, 1 = female

# Function to speak text
def speak(text):
    print("🤖 Robo:", text)
    engine.say(text)
    engine.runAndWait()

# Robo's response logic
def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I help you?"

    elif "your name" in user_input:
        return "I am Robo Speaker, your voice assistant."

    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm doing great!"

    elif "time" in user_input:
        from datetime import datetime
        return "The current time is " + datetime.now().strftime("%I:%M %p")


    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I didn't understand that."

# Main loop
while True:
    user = input("👤 You: ")

    if user.lower() in ["bye", "exit", "stop"]:
        speak("Goodbye! See you next time.")
        break

    response = get_response(user)
    speak(response)


