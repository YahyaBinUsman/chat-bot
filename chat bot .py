import speech_recognition as sr
import pyttsx3
import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI GPT-3 API key
openai.api_key = 'YOUR_API_KEY'

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return None
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response['choices'][0]['message']['content'].strip() if 'choices' in response else ''

def main():
    speak("Hello! I am your AI assistant. How can I help you today?")
    
    while True:
        command = listen()
        print("Command:", command)

        if command:
            if "exit" in command.lower():
                speak("good bye")
                break
            else:
                chat_prompt = f"User: {command}\nAssistant:"
                gpt_response = chat_with_gpt(chat_prompt)
                speak(gpt_response)

if __name__ == "__main__":
    main()









