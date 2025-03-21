import speech_recognition

def speech():
    mic = speech_recognition.Microphone()
    recog = speech_recognition.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)

        result = ""

        try:
            result = recog.recognize_google(audio, language="pl-PL")
        except:
            result = "Coś poszło nie tak..."

        return result