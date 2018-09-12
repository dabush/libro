from django.core.exceptions import PermissionDenied
from .models import UserList

class PermissionMixin(object):
	def dispatch(self, *args, **kwargs):
		userlist = UserList.objects.get(id=self.kwargs['userlist_id'])
		if userlist.not_public == True:
			if not self.request.user == userlist.user:
				raise PermissionDenied