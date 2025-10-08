#/usr/bin/env python3 
import subprocess 
import sys 
import os 
import logging 
 
def setup_logging(): 
    logging.basicConfig( 
        level=logging.INFO, 
        handlers=[ 
            logging.FileHandler('../logs/installation.log'), 
            logging.StreamHandler() 
        ] 
    ) 
    return logging.getLogger(__name__) 
 
def run_command(cmd, logger): 
    """Выполнить команду с обработкой ошибок""" 
    logger.info(f"Выполняю: {cmd}") 
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True) 
    if result.returncode  
        logger.error(f"Ошибка: {result.stderr}") 
        return False 
    return True 
 
def install_core(): 
    logger = setup_logging() 
    logger.info("Начало установки ядра ИИ...") 
 
    # Скачивание русской модели 
    logger.info("Скачивание русской языковой модели...") 
    try: 
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM 
        model_name = "cointegrated/rubert-tiny2" 
        logger.info(f"Загрузка модели: {model_name}") 
        tokenizer = AutoTokenizer.from_pretrained(model_name) 
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name) 
        logger.info("Русская языковая модель успешно загружена") 
    except Exception as e: 
        logger.error(f"Ошибка загрузки модели: {e}") 
        return False 
 
    logger.info("Установка ядра завершена") 
    return True 
 
if __name__ == "__main__": 
    if install_core(): 
        sys.exit(0) 
    else: 
        sys.exit(1) 
