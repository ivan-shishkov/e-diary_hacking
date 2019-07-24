import random

from datacenter.models import Mark, Chastisement, Lesson, Commendation, Schoolkid


COMMENDATIONS_TEXTS = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!',
]


def fix_marks(schoolkid, bad_marks=(2, 3), good_mark=5):
    Mark.objects.filter(schoolkid=schoolkid, points__in=bad_marks).update(points=good_mark)


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def add_commendation(schoolkid, subject_name):
    last_lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject_name,
    ).order_by('date').last()

    if not last_lesson:
        return

    Commendation.objects.create(
        text=random.choice(COMMENDATIONS_TEXTS),
        created=last_lesson.date,
        schoolkid=schoolkid,
        subject=last_lesson.subject,
        teacher=last_lesson.teacher,
    )


def run_e_diary_corrector(
        schoolkid_full_name, enable_fixing_marks=False,
        enable_removing_chastisements=False,
        subjects_names_for_adding_commendations=None):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_full_name)
    except Schoolkid.DoesNotExist:
        print('Не удалось найти ученика с таким именем')
        return
    except Schoolkid.MultipleObjectsReturned:
        print('Нашлось несколько учеников. Уточните запрос')
        return

    if enable_fixing_marks:
        print('Исправление плохих оценок...')
        fix_marks(schoolkid)

    if enable_removing_chastisements:
        print('Удаление замечаний...')
        remove_chastisements(schoolkid)

    if subjects_names_for_adding_commendations:
        print('Добавление записей с похвалой...')

        for subject_name in subjects_names_for_adding_commendations:
            add_commendation(schoolkid, subject_name)

    print('Выполнено')
