from django.db import models

from account.models import User


class Post(models.Model):
    STAR = (
        ('Star: 1', 'Star: 1'),
        ('Star: 2', 'Star: 2'),
        ('Star: 3', 'Star: 3'),
        ('Star: 4', 'Star: 4'),
        ('Star: 5', 'Star: 5'),
    )
    CHOOSE = (
        ('free Wi-Fi', 'free Wi-Fi'),
        ('No Wi-Fi', 'No Wi-Fi'),
    )
    CHOOSE1 = (
        ('Osh', 'Osh'),
        ('Bishkek', 'Bishkek'),
        ('Talas', 'Talas'),
        ('Batken', 'Batken'),
        ('Djalal-Abad', 'Djalal-Abad'),
        ('Naryn', 'Naryn'),
        ('I-K', 'I-K')

    )
    name = models.CharField(max_length=80)
    text = models.TextField(default='more...')
    min_price = models.PositiveSmallIntegerField(default=70)
    wi_fi = models.CharField(max_length=20, choices=CHOOSE, default='free Wi-Fi')
    city = models.CharField(max_length=20, choices=CHOOSE1, default='Bishkek')
    star = models.CharField(default=1, max_length=20, choices=STAR)
    address = models.TextField(default='Bishkek')

    def __str__(self):
        return f'{self.name}'


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    problem = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')


class Saved(models.Model):
    user = models.ForeignKey(User, related_name='saved_p', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='saved', on_delete=models.CASCADE)
    saved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.saved}'


class Likes(models.Model):
    liked_ads = models.ForeignKey(Post, on_delete=models.CASCADE,
                                  related_name='ads_likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_likes')


class RatingStar(models.Model):
    value = models.SmallIntegerField('value', default=0)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Rating Star'
        verbose_name_plural = 'Rating Stars'
        ordering = ['-value']


class Rating(models.Model):
    ads = models.ForeignKey(Post, on_delete=models.CASCADE,
                            related_name='rating')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='rating')
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE,
                             related_name='rating')

    def __str__(self):
        return f'{self.star} - {self.ads}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'