import speech_recognition as sr
from deepmultilingualpunctuation import PunctuationModel

model = PunctuationModel()

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Silakan berbicara...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="id-ID")
        print("Teks mentah:", text)

        formatted_text = model.restore_punctuation(text)
        print("Teks dengan tanda baca:", formatted_text)

    except sr.UnknownValueError:
        print("Maaf, saya tidak dapat memahami audio.")
    except sr.RequestError:
        print("Maaf, ada masalah dengan layanan pengenalan suara.")
