# Утилита для проверки наличия метки "i18n" в HTML тегах
## Описание проекта:
В данном проекте реализован класс с набором методов для проверки html файлов на наличие метки "i18n" в HTML тегах

## Пример использования:

#### Проверка директории целиком:

```python
from Checker import CheckerTagi18n

checker = CheckerTagi18n()

###Для использования собственного списка тегов 
#tags = ['p', 'h', 'h2', 'h5' , 'span']
#checker = CheckerTagi18n(tags)

checker.check_project('C:/Users/stejk/Documents/tubus_repo')
checker.write_errors_file() #Запись результата проверки всех файлов в файл

```

#### Проверка строки:
```python
#Проверка строки на наличие отсутствующих меток "i18n"
#Note: В случае ошибки возвращает False и первый тег с ошибкой
checker.check_tags('<p>This is the partial for view 2.</pi18n>') 
#resault False, <p>
```

#### Проверка файла:
```python
checker.check_file (file_path) #проверка файла на ошибки
#return [(Путь к файлу, номер_строки_с_ошибкой, тег_с_ошибкой), (...), ...]
```
#### Очистка списка ошибок:
```python
checker.reset_errors() #Метод удаляет все ранне зафиксированные ошибки
```