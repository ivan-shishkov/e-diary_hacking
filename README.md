# Взломщик электронного дневника

Данный модуль позволяет выполнить "взлом" [электронного дневника школы](https://github.com/devmanorg/e-diary), т.е. выполнить для выбранного ученика следующие действия:

* исправить оценки (заменить двойки и тройки на пятёрки)
* удалить все замечания
* добавить записи с похвалой по выбранным предметам

## Интерфейс модуля

Интерфейс модуля представлен следующей функцией:

```py

run_e_diary_corrector(
	schoolkid_full_name, 
	enable_fixing_marks=False, 
	enable_removing_chastisements=False,
	subjects_names_for_adding_commendations=None)

```

Аргументы функции:

* **schoolkid_full_name** - полное имя ученика, для которого необходимо выполнить коррекцию записей (например, 'Фролов Иван')
* **enable_fixing_marks** - включить исправление оценок (по умолчанию: False)
* **enable_removing_chastisements** - включить удаление всех замечаний (по умолчанию: False)
* **subjects_names_for_adding_commendations** - список предметов, по которым нужно добавить записи с похвалой (по умолчанию: None)

## Как запустить

* Выполнить установку и запуск [электронного дневника школы](https://github.com/devmanorg/e-diary) в соответствии с прилагаемой инструкцией
* Скопировать файл `e_diary_corrector.py` в директорию с проектом [электронного дневника школы](https://github.com/devmanorg/e-diary)
* Запустить консоль Django с помощью команды:
```bash

$ python manage.py shell

```
* Выполнить запуск коррекции электронного дневника для выбранного школьника:
```py

>>> from e_diary_corrector import run_e_diary_corrector
>>> run_e_diary_corrector('Дмитриев Валерьян', True, True, ['Информатика','География','Химия'])
Исправление плохих оценок...
Удаление замечаний...
Добавление записей с похвалой...
Выполнено

```

# Цели проекта

Код написан в учебных целях. Это урок из курса по веб-разработке — [Девман](https://dvmn.org).