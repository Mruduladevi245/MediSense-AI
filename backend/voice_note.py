import pyttsx3

# FIX: a single module-level engine that is reused across Flask requests
# is not safe with pyttsx3. Calling say()/runAndWait() again on the same
# engine instance across separate requests (especially with Flask's
# debug/threaded server) can raise "run loop already started" or hang
# the process. Creating a new engine per call avoids that.


def speak_text(text):
    """
    Speak the given text using a fresh engine instance.
    """
    engine = pyttsx3.init()
    engine.setProperty("rate", 160)
    engine.setProperty("volume", 1)

    voices = engine.getProperty("voices")
    if voices:
        engine.setProperty("voice", voices[0].id)

    engine.say(text)
    engine.runAndWait()
    engine.stop()