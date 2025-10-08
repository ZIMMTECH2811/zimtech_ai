#/usr/bin/env python3 
import os 
import sys 
import time 
import signal 
 
sys.path.append(os.path.dirname(__file__)) 
 
from ai_core import LocalAI 
from speech_module import SpeechProcessor 
from config import CONFIG 
 
class AIAssistant: 
    def __init__(self): 
        self.ai = LocalAI() 
        self.speech = SpeechProcessor() 
        self.is_running = False 
 
    def speech_callback(self, text): 
        print(f"Распознано: {text}") 
        response = self.ai.process_text(text) 
        print(f"Ответ: {response}") 
        self.speech.synthesize_speech(response) 
 
        if "стоп" in text.lower(): 
            self.stop() 
 
    def start(self): 
        self.is_running = True 
        print("Ассистент запущен... Говорите") 
 
        self.speech.listen_continuous(self.speech_callback) 
 
        try: 
            while self.is_running: 
                time.sleep(0.1) 
        except KeyboardInterrupt: 
            self.stop() 
 
    def stop(self): 
        self.is_running = False 
        self.speech.stop_listening() 
        print("Ассистент остановлен") 
 
if __name__ == "__main__": 
    signal.signal(signal.SIGINT, signal.signal.SIG_DFL) 
    assistant = AIAssistant() 
    assistant.start() 
