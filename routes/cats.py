from flask import Blueprint, render_template

cats_bp = Blueprint('cats', __name__, url_prefix='/cats')

@cats_bp.route('/')
def cats_home():
    return render_template('cats.html')

@cats_bp.route('/breeds')
def cats_breeds():
    # Список пород кошек
    breeds = [
        {"name": "Мейн-кун", "description": "Огромные, пушистые и очень добрые"},
        {"name": "Сиамская", "description": "Голубоглазые и разговорчивые"},
        {"name": "Британская", "description": "Плюшевые и независимые"},
        {"name": "Сфинкс", "description": "Лысые, но очень теплые"},
        {"name": "Персидская", "description": "Курносые и пушистые"}
    ]
    return render_template('cats.html', breeds=breeds, page='breeds')

@cats_bp.route('/care')
def cats_care():
    # Советы по уходу
    tips = [
        "Кормите качественным кормом",
        "Всегда должна быть свежая вода",
        "Регулярно вычесывайте шерсть",
        "Поставьте когтеточку",
        "Играйте с кошкой каждый день"
    ]
    return render_template('cats.html', tips=tips, page='care')
