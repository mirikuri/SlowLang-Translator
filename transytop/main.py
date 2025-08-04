from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import asyncio
import random
from typing import List

app = FastAPI(title="SlowLang™ Translator")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

PROCESS_MESSAGES = [
    "🧪 Анализ морфем...",
    "🔍 Поиск семантических соответствий...",
    "🧠 Моделирование культурного контекста...",
    "💡 Подключение к модели ИИ...",
    "🌍 Выделение языковых шаблонов...",
    "🤔 Задумался над грамматикой...",
    "📚 Проверка словарных соответствий...",
    "⚙️ Оптимизация нейросетевых весов...",
    "🌀 Инициализация квантового переводчика..."
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/translate")  # Изменено с POST на GET
async def translate(text: str):
    async def generate():
        # Генерируем случайную последовательность сообщений
        messages = random.sample(PROCESS_MESSAGES, k=random.randint(3, 6))
        
        for msg in messages:
            await asyncio.sleep(random.uniform(2, 5))
            yield f"data: {msg}\n\n"
        
        translation = get_translation(text)
        for i in range(len(translation)):
            await asyncio.sleep(random.uniform(0.2, 0.5))
            yield f"data: TRANSLATION:{translation[:i+1]}\n\n"
        
        yield "data: DONE:📘 Перевод завершен!\n\n"
        yield "event: close\ndata: \n\n"  # Явное закрытие соединения

    return StreamingResponse(generate(), media_type="text/event-stream")

def get_translation(text: str) -> str:
    translations = {
        "hello": "привет",
    "world": "мир",
    "how are you": "как дела",
    "goodbye": "до свидания",
    "slow": "медленный",
    "translator": "переводчик",
    "friend": "друг",
    "love": "любовь",
    "hate": "ненависть",
    "peace": "мир",
    "war": "война",
    "code": "код",
    "bug": "баг",
    "feature": "фича",
    "developer": "разработчик",
    "keyboard": "клавиатура",
    "mouse": "мышь",
    "computer": "компьютер",
    "language": "язык",
    "fast": "быстрый",
    "slowly": "медленно",
    "run": "бежать",
    "stop": "стоп",
    "error": "ошибка",
    "success": "успех",
    "fire": "огонь",
    "ice": "лёд",
    "dark": "тёмный",
    "light": "светлый",
    "sky": "небо",
    "earth": "земля",
    "sun": "солнце",
    "moon": "луна",
    "star": "звезда",
    "galaxy": "галактика",
    "universe": "вселенная",
    "time": "время",
    "space": "пространство",
    "future": "будущее",
    "past": "прошлое",
    "present": "настоящее",
    "robot": "робот",
    "ai": "искусственный интеллект",
    "machine": "машина",
    "human": "человек",
    "life": "жизнь",
    "death": "смерть",
    "beginning": "начало",
    "end": "конец"
    }
    return " ".join(translations.get(word.lower(), word) for word in text.split())