from django.db import models
from django.conf import settings

from books.models import Book

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)

class UserList(models.Model):
	name = models.CharField(max_length=150)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	book = models.ManyToManyField('books.Book', blank=True, through='UserListEntry', related_name='user_list_books')
	list_desc = models.TextField()
	list_image = models.ImageField(null=True, blank=True, upload_to='list_images')

	def __str__(self):
		return self.name

class UserListEntry(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	user_list = models.ForeignKey(UserList, related_name='userlist_author', on_delete=models.CASCADE)
	book = models.ForeignKey('books.Book', related_name='in_userlist', on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s in %s\'s list %s' % (self.book, self.user, self.user_list)


