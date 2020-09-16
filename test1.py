import random

# 1. Закончите функцию, которая создает генератор паролей для пользователя с учетом заданных параметров.

def pass_gen(min_length=5):
    a = ['a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3', '4']
    password_list = []
    random.shuffle(a)
    password_list = ''.join([random.choice(a) for x in range(min_length)])
    return password_list

pwd = pass_gen(min_length=5)
print(pwd)
# 1a. Используя данные списка a в первом задании, сколько комбинаций может быть выполнено при составлении простого двух-символьного пароля из элементов этого списка (например, "3b", "1d", "a2" и т.д.). Напишите логику выполнения и количество возможных комбинаций, учитывая, что варианты '13', '41', 'af', 'ec' и т.д. недопустимы.

# 2. Если вы написали функцию-генератор паролей чуть выше, выполните следующие действия с полученным паролем:

# a. получите 4-е значение из списка созданного пароля;
print(pwd[3])

# b. получите пароль из задания 1 в качестве строки, и добавьте в начало этой строки следующий текст: "Hello, your password is: "
print('Hello, your password is: ', pwd)
# c. создайте словарь со следующими ключами - "1st pass", "2nd pass" и придайте первому ключу значение полученного пароля, второму ключу - значение первого ключа в обратной последовательности.
dict = {'1st pass' : pwd, '2nd pass' : pwd[::-1]}
print(dict)
# d. создайте 3-й ключ "3rd pass", который содержит значения ключа 1 и ключа 2
dict['3rd pass'] = [dict['1st pass'] , dict['2nd pass']]
print(dict)
# e. Оставьте только уникальные значения из полученных ранее ключей 1 и 2
unique_values = set(' '.join(x if type(x) != list else ' '.join(y for y in x) for x in dict.values()).split())
print(unique_values)
# f. Обновите ваш словарь только одним ключем "unique" с полученными выше уникальнымы значениями из ключей 1 и 2
dict = {'unique' : unique_values}
print(dict)

# 3. У вас есть база данных приложения, в которой 2 таблицы: Clients & Engagements. В таблице Clients есть поле, которое содержит название клиента на англ. языке (client_name_engl). Используя Django ORM, напишите запрос в БД, который отобразит только тех клиентов на англ. языке, у кого название начинается с "Manage" и заканчивается на "ment".
SELECT * FROM Clients WHERE client_name_engl = "Manage" AND "ment";
# 4. Используя Django ORM, cделайте сортировку полученных данных (client_name_engl) по дате внесения в базу данных. Информация о дате внесения записи содержится в таблице Clients в поле entry_date.
SELECT * FROM Clients ORDER BY entry_date;

# 5. Таблицы Clients & Engagements связаны между собой через foreign_key. Используя Django ORM, напишите, как именно вы отобразите эту связь, предполагая, что поле foreign_key должно находиться в таблице Engagements.

from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
            return '%s' % (self.name)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Engagements(models.Model):
    something = models.ForeignKey(Clients, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
            return '%s' % (self.name)

    class Meta:
        verbose_name = 'Engagement'
        verbose_name_plural = 'Engagements'

# 6. В таблице Clients - 7 записей. Вам необходимо получить 5-ю запись из этой таблицы через foreign_key, который вы создали чуть выше. Напишите, как именно вы это сделаете.
from django.views.generic import ListView
class ProductListView(LoginRequiredMixin, ListView):
    model = models.Clients

    def get_context_data(self, **kwargs):
        key5 = self.request.GET.get('pk5')
        context = super().get_context_data(**kwargs)
        context['pk5'] = key5
        return context


# 7. Используя SQL-синтаксис, замените в таблице Clients только те записи, в которых есть "ment", на "test_name"
UPDATE Clients SET client_name_engl = 'test_name' WHERE client_name_engl = 'ment';
# 8. Опишите своими словами, как вы понимаете обычную структуру Django-приложения, и для чего в принципе нужен Django ORM?
#(Моими словами вкратце)... Структура Django приложения состоит из моделей, которые мигрируются в базу данных, все это через импорты модулей связано с views (где мы используем данные), и еще прописываем их через маршрут urls. Сам фронтэнд приложения отрисовывается в templates, который тоже связан с urls. Все это в совокупности связано и образует работающее приложение.
#Django ORM - нужен для того что бы с помощью ООП и подкапотного Django взаимодействовать с БД и быстро иметь прогресс в разработке приложения. Т.к. таблицы для базы данных пишуться в классах в разделе models.
# 9. У вас есть html-шаблон, в котором есть следующий <div>: <div id="results-id"></div>. При этом в этом же шаблоне есть поле <input type="text" id="input-id">, в котором пользователь может оставить любые символы. Используя jQuery, напишите функцию, которая обновит <div id="results-id"> после того, как пользователь напишет в поле <input type="text" id="input-id"> "please test"

#Очень редко сталкивался в jQuery

# 10. У вас есть доступ к удаленному git репозиторию test-repository.git, который является источником для отдельного web-проекта в production. Напишите чуть ниже, какие команды необходимо выполнить, чтобы реализовать следующие сценарии (можно написать только git-команды):

# а). получить точную копию репозитория на своей локальной машине в директорию С:\working_dir\;
git clone test-repository.git
# b). после внесения изменений в рабочей копии репозитория на локальной машине, необходимо обновить (записать) эти изменения в удаленный репозиторий. Все изменения были выполнены в master branch.
git status
git add .
git commit -m 'some changes'
git push
# c). вы обновили удаленный git-репозиторий test-repository.git, тем временем в рабочей папке web-проекта были внесены изменения. Вам необходимо временно сохранить их без внесения этих изменений в test-repository.git. Какую команду вы выполните?
git stash
# d). после того, как временные изменения были сохранены, вам необходимо полностью синхронизировать test-repository.git с содержимым рабочей папки web-проекта (получить все обновления из test-repository.git, master branch). Какую команду вы выполните для этого?
git pull
# 11. Найдите 2 ошибки в логике исполнения следующей функции, и объясните, в чем они заключаются. Импорты отдельных библиотек Django используются лишь справочно, выводить решение в интерпретатор (и подключать сторонние библиотеки) не нужно.

from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import FormBase


def submit(request):
    data = dict()

    if request.method == 'POST':
        form_a = FormBase(request.POST)

        if form_a.is_valid():
            base = form_a.save()
            base.type = 'Type A'
            base.type_id = base.id
            base.save()
            data['is_valid'] = True
        else:
            form_a = FormBase()

    else:
        data['is_valid'] = True

    context = {'form_a': form_a}
    data['html_form'] = render_to_string(
        'templates/form.html', context, request=request)
    return JsonResponse(data)
