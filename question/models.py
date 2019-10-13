from django.db import models
from django.utils.text import slugify
from pytz import timezone  # 현지 시각 출력을 위하여
from django.conf import settings
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField




def local_time(input_time):
    fmt = '%Y-%m-%d %H:%M'
    my_zone = timezone(settings.TIME_ZONE)
    my_local_time = input_time.astimezone(my_zone)
    return my_local_time.strftime(fmt)




class Question(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # 'auth.User'라고 쓰는 것보다 강추
        on_delete=models.CASCADE,
        related_name='question',
        db_column='author',
        default='',
        null=False,
    )
    title = models.CharField('', max_length=100, null=False)
    # content = models.TextField('내용', null=False)
    content = RichTextUploadingField('', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True)
    hit = models.PositiveIntegerField(default=0)

    def save(self):
        self.slug = slugify(self.title)
        super(Question, self).save()

    def __str__(self):
        return '%s' % self.title


    class Meta:
        ordering = ['-id']  # notice 객체의 기본 정렬 순서 지정

    def __str__(self):
        return self.title

    def short_content(self):
        if self.content:
            t = self.content[:20] + '...'   # content 속성의 일부만 반환
        else:
            t = '(내용 없음)'
        return t
    short_content.short_description = '간략 내용'

    @property
    def update_counter(self):
        self.hit = self.hit + 1
        self.save()
        return self.hit

    def get_absolute_url(self):
        # return reverse('notice:notice_detail', args=[self.pk])
        return reverse('question:question_detail', kwargs={'pk': self.pk}) # reverse 임포트 시켜주어야함.

class Comment(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Question, on_delete=models.CASCADE,
                             related_name='comments', verbose_name='게시물')
    message = models.TextField('댓글')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-post__id', '-id']  # '-post__id', '-id'

    def __str__(self):
        return self.message

    def updated(self):
        return local_time(self.updated_at)
    updated.short_description = '수정 일시'



