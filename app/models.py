from distutils.command import upload
from statistics import mode
from turtle import title
from unicodedata import category
from django.db import models
# from django.contrib.auth.models import AbstractUser




class Seminar(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    description = models.TextField()
    count_lessons = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}{self.type}{self.description}{self.count_lessons}'

class Category_detail_seminar(models.Model):
    title = models.CharField(max_length=250)
    description_title = models.CharField(max_length=250)
    start_date1 = models.CharField(max_length=100)
    in_date2 = models.CharField(max_length=100)
    time_date3 = models.CharField(max_length=100)
    video = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
    about_seminar1 = models.CharField(max_length=100)
    about_seminar2 = models.CharField(max_length=250)
    about_seminar_min_text1 = models.CharField(max_length=250)
    about_seminar_min_text2 = models.CharField(max_length=250)
    about_seminar_min_text3 = models.CharField(max_length=250)
    about_seminar_min_text4 = models.CharField(max_length=250)
    question_for_payments = models.CharField(max_length=500)
    block_question_1 = models.CharField(max_length=100)
    category = models.ForeignKey(Seminar,on_delete=models.PROTECT)
    teacher_seminar = models.CharField(max_length=100)
    jobs_teacher = models.CharField(max_length=100)
    description_teacher_text = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Изображение')

    def __str__(self):
        return f'{self.title}{self.category}'

class Category_makala(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=50,blank=True)
    date = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.title}'

class Makala_detail(models.Model):
    title = models.CharField(max_length=250)
    date = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    video = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
    title2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=250)
    description3 = models.TextField(blank=True)

    category = models.ForeignKey(Category_makala,on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    title = models.TextField(verbose_name='Комментарий калтырып кетиңиз')

    def __str__(self):
        return f'{self.title}'

class Category_trainings(models.Model):
    type  = models.CharField(max_length=50,verbose_name='тип тренинга')
    name = models.CharField(max_length=100,verbose_name='название тренинга')
    description = models.TextField(verbose_name='описание тренинга')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Изображение')
    def __str__(self):
        return f'{self.name}'

class Detail_trainings(models.Model):
    title_name = models.CharField(max_length=100,verbose_name='Название курса')
    description_title_name = models.TextField(verbose_name='описание курса')
    format_trainings = models.CharField(max_length=250,verbose_name='формат тренинга')
    count_lesson = models.CharField(max_length=100,blank=True,verbose_name='сколько материала')
    time = models.CharField(max_length=20,blank=True,verbose_name='длительность курса')
    video = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True,verbose_name='видео')
    about_course = models.TextField(verbose_name='о курсе описание курса',blank=True)
    about_course2 = models.TextField(verbose_name='о курсе описание курса2',blank=True)
    about_course3 = models.TextField(verbose_name='о курсе описание курса3',blank=True)
    for_who = models.TextField(verbose_name='для кого это',blank=True)
    for_who2 = models.TextField(verbose_name='для кого это2',blank=True)
    for_who3 = models.TextField(verbose_name='для кого это3',blank=True)
    will_know = models.TextField(verbose_name='Вы узнаете',blank=True)
    will_know2 = models.TextField(verbose_name='Вы узнаете',blank=True)
    will_know3 = models.TextField(verbose_name='Вы узнаете',blank=True)
    result_you = models.TextField(verbose_name='в результате вы',blank=True)
    result_you2 = models.TextField(verbose_name='в результате вы2',blank=True)
    result_you3 = models.TextField(verbose_name='в результате вы3',blank=True)
    result_you4 = models.TextField(verbose_name='в результате вы4',blank=True)
    result_you5 = models.TextField(verbose_name='в результате вы5',blank=True)
    block_question = models.CharField(max_length=250,verbose_name='первый блок вопрос')
    data_block1 = models.CharField(max_length=100,verbose_name='время первого блока',blank=True)
    description_block1 = models.TextField(verbose_name='ответ первого блока1')
    description_block2 = models.TextField(verbose_name='ответ первого блока2')
    description_block3 = models.TextField(verbose_name='ответ первого блока3')
    description_block4 = models.TextField(verbose_name='ответ первого блока4')
    description_block5 = models.TextField(verbose_name='ответ первого блока5')
    block_question2 = models.CharField(max_length=250,verbose_name='второй блок вопрос')
    data_block2 = models.CharField(max_length=100,verbose_name='время второго блока',blank=True)
    description_block21 = models.TextField(verbose_name='ответ второго блока21')
    description_block22 = models.TextField(verbose_name='ответ второго блока22')
    description_block23 = models.TextField(verbose_name='ответ второго блока23')
    description_block24 = models.TextField(verbose_name='ответ второго блока24')
    description_block25 = models.TextField(verbose_name='ответ второго блока25')
    block_question3 = models.CharField(max_length=250,verbose_name='третий блок вопрос')
    data_block3 = models.CharField(max_length=100,verbose_name='время третьего блока',blank=True)
    description_block31 = models.TextField(verbose_name='ответ третьего блока')
    description_block32 = models.TextField(verbose_name='ответ третьего блока2')
    description_block33 = models.TextField(verbose_name='ответ третьего блока3')
    description_block34 = models.TextField(verbose_name='ответ третьего блока4')
    description_block35 = models.TextField(verbose_name='ответ третьего блока5')
    what_give_course1 = models.TextField(verbose_name='на курсе вы научитесь ?')
    what_give_course2 = models.TextField(verbose_name='на курсе вы научитесь2 ?')
    what_give_course3 = models.TextField(verbose_name='на курсе вы научитесь3 ?')
    what_give_course4 = models.TextField(verbose_name='на курсе вы научитесь4 ?')
    what_give_course5 = models.TextField(verbose_name='на курсе вы научитесь5 ?')
    what_give_course6 = models.TextField(verbose_name='на курсе вы научитесь6 ?')
    what_give_course7 = models.TextField(verbose_name='на курсе вы научитесь7 ?')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Изображение')
    name_mentor = models.CharField(max_length=100,verbose_name='имя тренера')
    description_mentor = models.CharField(max_length=250,verbose_name='опишите тренера, кейсы',blank=True)
    description_mentor21 = models.TextField(verbose_name='биография тренера')
    description_mentor22 = models.TextField(verbose_name='биография тренера')
    description_mentor23 = models.TextField(verbose_name='биография тренера')
    description_mentor24 = models.TextField(verbose_name='биография тренера')
    category = models.ForeignKey(Category_trainings,on_delete=models.PROTECT)

class Buissines(models.Model):
    title_name = models.CharField(max_length=100,verbose_name='Название курса')
    description_title_name = models.TextField(verbose_name='описание курса')
    format_trainings = models.CharField(max_length=250,verbose_name='формат тренинга')
    count_lesson = models.CharField(max_length=100,blank=True,verbose_name='сколько материала')
    time = models.CharField(max_length=20,blank=True,verbose_name='длительность курса')
    video = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True,verbose_name='видео')
    about_course = models.TextField(verbose_name='о курсе описание курса',blank=True)
    about_course2 = models.TextField(verbose_name='о курсе описание курса2',blank=True)
    about_course3 = models.TextField(verbose_name='о курсе описание курса3',blank=True)
    for_who = models.TextField(verbose_name='для кого это',blank=True)
    for_who2 = models.TextField(verbose_name='для кого это2',blank=True)
    for_who3 = models.TextField(verbose_name='для кого это3',blank=True)
    will_know = models.TextField(verbose_name='Вы узнаете',blank=True)
    will_know2 = models.TextField(verbose_name='Вы узнаете',blank=True)
    will_know3 = models.TextField(verbose_name='Вы узнаете',blank=True)
    result_you = models.TextField(verbose_name='в результате вы',blank=True)
    result_you2 = models.TextField(verbose_name='в результате вы2',blank=True)
    result_you3 = models.TextField(verbose_name='в результате вы3',blank=True)
    result_you4 = models.TextField(verbose_name='в результате вы4',blank=True)
    result_you5 = models.TextField(verbose_name='в результате вы5',blank=True)
    block_question = models.CharField(max_length=250,verbose_name='первый блок вопрос')
    data_block1 = models.CharField(max_length=100,verbose_name='время первого блока',blank=True)
    description_block1 = models.TextField(verbose_name='ответ первого блока1')
    description_block2 = models.TextField(verbose_name='ответ первого блока2')
    description_block3 = models.TextField(verbose_name='ответ первого блока3')
    description_block4 = models.TextField(verbose_name='ответ первого блока4')
    description_block5 = models.TextField(verbose_name='ответ первого блока5')
    block_question2 = models.CharField(max_length=250,verbose_name='второй блок вопрос')
    data_block2 = models.CharField(max_length=100,verbose_name='время второго блока',blank=True)
    description_block21 = models.TextField(verbose_name='ответ второго блока21')
    description_block22 = models.TextField(verbose_name='ответ второго блока22')
    description_block23 = models.TextField(verbose_name='ответ второго блока23')
    description_block24 = models.TextField(verbose_name='ответ второго блока24')
    description_block25 = models.TextField(verbose_name='ответ второго блока25')
    block_question3 = models.CharField(max_length=250,verbose_name='третий блок вопрос')
    data_block3 = models.CharField(max_length=100,verbose_name='время третьего блока',blank=True)
    description_block31 = models.TextField(verbose_name='ответ третьего блока')
    description_block32 = models.TextField(verbose_name='ответ третьего блока2')
    description_block33 = models.TextField(verbose_name='ответ третьего блока3')
    description_block34 = models.TextField(verbose_name='ответ третьего блока4')
    description_block35 = models.TextField(verbose_name='ответ третьего блока5')
    what_give_course1 = models.TextField(verbose_name='на курсе вы научитесь ?')
    what_give_course2 = models.TextField(verbose_name='на курсе вы научитесь2 ?')
    what_give_course3 = models.TextField(verbose_name='на курсе вы научитесь3 ?')
    what_give_course4 = models.TextField(verbose_name='на курсе вы научитесь4 ?')
    what_give_course5 = models.TextField(verbose_name='на курсе вы научитесь5 ?')
    what_give_course6 = models.TextField(verbose_name='на курсе вы научитесь6 ?')
    what_give_course7 = models.TextField(verbose_name='на курсе вы научитесь7 ?')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Изображение')
    name_mentor = models.CharField(max_length=100,verbose_name='имя тренера')
    description_mentor = models.CharField(max_length=250,verbose_name='опишите тренера, кейсы',blank=True)
    description_mentor21 = models.TextField(verbose_name='биография тренера')
    description_mentor22 = models.TextField(verbose_name='биография тренера')
    description_mentor23 = models.TextField(verbose_name='биография тренера')
    description_mentor24 = models.TextField(verbose_name='биография тренера')


    def __str__(self):
        return f'{self.title_name}'

class Mentor(models.Model):
    name = models.CharField(max_length=100)
    about_mentor = models.CharField(max_length=250,verbose_name='описание тренера кейсы',blank=True)
    description = models.TextField(verbose_name='описать о курсе')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Изображение')

class Application(models.Model):
    name = models.CharField(max_length=150,verbose_name='Аты-жөнүңүз',blank=True)
    phone = models.CharField(max_length=150,verbose_name='Телефон номериңиз *',blank=True)
    email_adress = models.EmailField(verbose_name='E-mail почтаңыз *',blank=True)
    comment = models.TextField(verbose_name='Сиздин өтүнүчүңүз',blank=True)

    def __str__(self):
        return f'{self.name}'


# class Account(AbstractUser):
#     payed = models.BooleanField(blank=True, null=True)























