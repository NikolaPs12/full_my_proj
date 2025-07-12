from flask import Blueprint, render_template, redirect, url_for, flash
import requests
from api_key import API_TOKEN


main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    url_img = None  # Инициализируем переменную
    headers = {"x-api-key": API_TOKEN}  # The Cat API требует ключ в headers
    
    try:
        response = requests.get(
            "https://api.thecatapi.com/v1/images/search",
            headers=headers,
            timeout=5  # Таймаут на случай долгого ответа
        )
        response.raise_for_status()  # Проверка на ошибки HTTP
        
        data = response.json()
        if data and isinstance(data, list):  # Проверка что данные получены
            url_img = data[0]["url"]  # Берем URL первого изображения
            
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        # Можно добавить flash-сообщение для пользователя:
        # flash("Не удалось загрузить изображение кота", "error")
    
    return render_template('main/index.html', url_img=url_img)