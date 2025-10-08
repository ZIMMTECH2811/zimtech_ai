import speech_recognition as sr 
import pyttsx3 
import threading 
 
class SpeechProcessor: 
    def __init__(self): 
        self.recognizer = sr.Recognizer() 
        self.microphone = sr.Microphone() 
        self.is_listening = False 
        self.setup_tts() 
 
    def setup_tts(self): 
        try: 
            self.tts_engine = pyttsx3.init() 
            voices = self.tts_engine.getProperty('voices') 
            for voice in voices: 
                if 'russian' in voice.name.lower(): 
                    self.tts_engine.setProperty('voice', voice.id) 
                    break 
            self.tts_engine.setProperty('rate', 150) 
        except Exception as e: 
            print(f"Ошибка инициализации TTS: {e}") 
            self.tts_engine = None 
 
    def synthesize_speech(self, text): 
        if self.tts_engine: 
            try: 
                self.tts_engine.say(text) 
                self.tts_engine.runAndWait() 
            except Exception as e: 
                print(f"Ошибка синтеза речи: {e}") 
 
    def listen_continuous(self, callback): 
        def listen_thread(): 
            self.is_listening = True 
            while self.is_listening: 
                try: 
                    with self.microphone as source: 
                        audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=5) 
                    text = self.recognizer.recognize_google(audio, language="ru-RU") 
                    if text and text  
                        callback(text) 
                except: 
                    continue 
 
        thread = threading.Thread(target=listen_thread) 
        thread.daemon = True 
        thread.start() 
 
    def stop_listening(self): 
        self.is_listening = False 
