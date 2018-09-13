from django.core.exceptions import PermissionDenied
from .models import UserList

class ViewPermissionsMixin(object):
	"""Base class for all custom permission mixins to inherit from"""
	def has_permissions(self):
		return True 

	def dispatch(self, request, *args, **kwargs):
		if not self.has_permissions():
			raise PermissionDenied
		return super(ViewPermissionsMixin, self).dispatch(
			request, *args, **kwargs)

class PrivatePermissionMixin(ViewPermissionsMixin):

	def has_permissions(self):
		# here you will have access to both
		# self.get_object() and self.request.user
		if not self.get_object().not_public == True:
			return self.request.user == self.request.user