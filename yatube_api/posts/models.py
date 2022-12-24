from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
NUMBER_OF_LETTERS: int = 15


class Group(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=200
    )
    slug = models.SlugField(
        verbose_name='путь',
        unique=True
    )
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Группа"


class Post(models.Model):
    text = models.TextField(verbose_name='Текст поста')
    pub_date = models.DateTimeField(
        verbose_name='дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='posts'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='картинка'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.text[:NUMBER_OF_LETTERS]

    class Meta:
        verbose_name = "Пост"


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Текст поста'
    )
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(
        verbose_name='дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = "Комментарии"


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        related_name='follower',
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        User,
        related_name='following',
        verbose_name='Автор',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Подписки"
        constraints = [
            models.UniqueConstraint(
                fields=("user", "following"),
                name="unique_name_user_following"
            )
        ]
