from django.conf import settings #открывает доступ к коду из других файлов
from django.db import models
from django.utils import timezone

class Post(models.Model): # эта строка опредеделяет нашу модель (объект)
    #class - специальное ключевое слово для определения объектов
    #Post - имя модели, всегда с БОЛЬШОЙ буквы.
    #models.Model - означает, что модель Post является моделью Django, так Джанго поймёт что должен сохранить его в БД
    author = models.ForignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # ForeignKey - ccылка на другую модель
    title = models.CharField(max_length=200) #models.CharField - так мы определяем текстовое поле с ограничением на количество символов.
    text = models.TextField() # поле для неограниченно длинного текста.
    #created_date = models.DateTimeField(default=timezone.now()) - в конце со скобками
    created_date = models.DateTimeField(default=timezone.now) # дата и время
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self): #метод публикации для записи, def - создается функция/метод, publish - название этого метода.
        #!!!!!!!!!!! Для имён функции нужно использовать строчные буквы
        self.publish_date = timezone.now()
        self.save()

#методы часто что-то возвращают
    def __str__(self): #после вызова этого метода мы получим текст (строку) с заголовком записи
        return self.title




