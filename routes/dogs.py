from flask import Blueprint, render_template

dogs_bp = Blueprint('dogs', __name__, url_prefix='/dogs')

@dogs_bp.route('/')
def dogs_home():
    return render_template('dogs.html')

@dogs_bp.route('/breeds')
def dogs_breeds():
    # Список пород собак
    breeds = [
        {"name": "Лабрадор", "description": "Дружелюбный семейный пес"},
        {"name": "Немецкая овчарка", "description": "Умный и преданный"},
        {"name": "Такса", "description": "Охотничий пес с длинным телом"},
        {"name": "Хаски", "description": "Красивый, но упрямый"},
        {"name": "Йоркширский терьер", "description": "Маленький, но смелый"}
    ]
    return render_template('dogs.html', breeds=breeds, page='breeds')

@dogs_bp.route('/training')
def dogs_training():
    # Команды для дрессировки
    commands = [
        "Сидеть - базовая команда",
        "Лежать - учит собаку спокойствию",
        "Ко мне - самая важная команда",
        "Рядом - для комфортных прогулок",
        "Дай лапу - просто для удовольствия"
    ]
    return render_template('dogs.html', commands=commands, page='training')
