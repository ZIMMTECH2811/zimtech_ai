from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM 
import logging 
 
class LocalAI: 
    def __init__(self): 
        self.setup_logging() 
        self.load_models() 
 
    def setup_logging(self): 
        logging.basicConfig(level=logging.INFO) 
        self.logger = logging.getLogger(__name__) 
 
    def load_models(self): 
        try: 
            model_name = "cointegrated/rubert-tiny2" 
            self.tokenizer = AutoTokenizer.from_pretrained(model_name) 
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name) 
            self.logger.info("Модели успешно загружены") 
        except Exception as e: 
            self.logger.error(f"Ошибка загрузки моделей: {e}") 
 
    def process_text(self, text): 
        try: 
            responses = { 
                "привет": "Привет Я локальный ассистент на OrangePi", 
                "как дела": "Работаю стабильно, учитывая ограничения железа", 
                "что ты умеешь": "Я могу распознавать речь, синтезировать речь и распознавать жесты", 
                "стоп": "Завершаю работу" 
            } 
 
            text_lower = text.lower() 
            for key in responses: 
                if key in text_lower: 
                    return responses[key] 
 
            return self.generate_response(text) 
        except Exception as e: 
            return f"Ошибка обработки: {e}" 
 
    def generate_response(self, text): 
        try: 
            inputs = self.tokenizer(text, return_tensors="pt", max_length=512, truncation=True) 
            outputs = self.model.generate(**inputs, max_length=50) 
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True) 
            return response 
        except Exception as e: 
            return "Извините, не могу обработать этот запрос" 
