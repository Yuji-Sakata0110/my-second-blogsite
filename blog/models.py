#from とか import で始まる行は全部、他のファイルから何かをちょこっとずつ追加する行
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
# これはおぶじぇくとだよ
# "models.Model"はポストがDjango ModelということをDjangoに伝える

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #ブログを公開するメソッド
    #パブリッシュする際にこのメソッドがどのように動くかわからんのやけど...
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #　ダブルアンダースコア
    # ちなみにこいつ何ができるんだ？？
    def __str__(self):
        return self.title
