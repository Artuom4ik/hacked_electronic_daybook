from datacenter.models import Schoolkid, Subject 
from datacenter.models import Chastisement, Mark
from datacenter.models import Lesson, Commendation
from random import randint, choice


COMENDATIONS = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!",
    "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!",
    "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!",
    "Очень хороший ответ!",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!",
    "Я поражен!",
    "Уже существенно лучше!",
    "Потрясающе!",
    "Замечательно!",
    "Прекрасное начало!",
    "Так держать!",
    "Ты на верном пути!",
    "Здорово!",
    "Это как раз то, что нужно!",
    "Я тобой горжусь!",
    "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!",
    "Я вижу, как ты стараешься!",
    "Ты растешь над собой!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!",
    ]


def fix_marks(schoolkid):
    schoolkid_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for schoolkid_mark in schoolkid_marks:
        schoolkid_mark.points = randint(4, 5)
        schoolkid_mark.save()

def remove_chastisement(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()
    

def create_commendation(schoolkid, title):
    subject = Subject.objects.filter(title=title, year_of_study=schoolkid.year_of_study)
    schoolkid_lessons = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject=subject[0])
    for lesson in schoolkid_lessons:
        Commendation.objects.create(
            schoolkid=schoolkid,
            teacher=lesson.teacher,
            subject=lesson.subject,
            created=lesson.date,
            text=choise(COMENDATIONS))


if __name__ == "__main__":
    schoolkid = Schoolkid.objects.get(full_name__contains="Фролов Иван")
    fix_marks(schoolkid)
    remove_chastisement(schoolkid)
    create_commendation(schoolkid, "Математика")