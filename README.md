# Линейные преобразования

## Установка
```
pip install poetry
poetry install
```

## Вывод справки
```
python3 main.py --help
```

## Примеры запусков
### Изменение имён входных и выходных файлов
```
python3 main.py --input img.png --output out.png
```
### Применение фильтра Гаусса
```
python3 main.py --input img.png --gauss
```
### Применение медианного фильтра
```
python3 main.py --input img.png --median
```
### Применение фильтра для увеличения четкости изображения
```
python3 main.py --input img.png --sharpness
```
