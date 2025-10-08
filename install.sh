#/bin/bash 
 
set -e 
 
echo "🐳 Установка локального ИИ ассистента для OrangePi" 
echo "==================================================" 
 
# Проверка Python 
    echo "❌ Python3 не установлен. Установите Python3.7+" 
    exit 1 
fi 
 
# Создание директорий 
echo "📁 Создание структуры директорий..." 
mkdir -p models 
mkdir -p logs 
 
# Создание виртуального окружения 
echo "🐍 Создание виртуального окружения..." 
python3 -m venv ai_venv 
source ai_venv/bin/activate 
 
# Обновление pip 
echo "📦 Обновление pip..." 
pip install --upgrade pip 
 
# Установка зависимостей 
echo "🔧 Установка базовых зависимостей..." 
pip install -r requirements/core.txt 
 
echo "🎵 Установка аудио компонентов..." 
pip install -r requirements/audio.txt 
 
echo "👁️ Установка компонентов компьютерного зрения..." 
pip install -r requirements/vision.txt 
 
# Установка ядра 
echo "🤖 Установка ИИ ядра..." 
python scripts/install_core.py 
 
# Скачивание моделей Vosk 
echo "🗣️ Скачивание моделей распознавания речи..." 
if [  -f "models/vosk-model-small-ru-0.22/am/final.mdl" ]; then 
    wget -c "https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip" -O vosk-model.zip 
    unzip vosk-model.zip -d models/ 
    rm vosk-model.zip 
    echo "✅ Модель Vosk установлена" 
else 
    echo "✅ Модель Vosk уже установлена" 
fi 
 
# Права на выполнение 
chmod +x scripts/*.sh 
 
echo "" 
echo "🎉 Установка завершена" 
echo "" 
echo "Для запуска:" 
echo "  source ai_venv/bin/activate" 
echo "  cd src && python3 main.py" 
