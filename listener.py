import speech_recognition as sr

def listen_and_convert():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the source
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise

        while True:
            try:
                print("Listening...")
                # Listen for speech
                audio = recognizer.listen(source)

                # Recognize speech using Google's speech recognition
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")

            except sr.UnknownValueError:
                # In case of unrecognized speech
                print("Sorry, I did not understand that.")
            except sr.RequestError as e:
                # In case of API request error
                print(f"Could not request results; {e}")
            except KeyboardInterrupt:
                # Exit the loop gracefully on Ctrl+C
                print("\nExiting program.")
                break

# Call the function to start listening
listen_and_convert()
