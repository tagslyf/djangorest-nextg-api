# Source: https://qbox.io/blog/elasticsearch-python-django-database
from django.core.management.base import BaseCommand

from core.accounts.models import UserType

class Command(BaseCommand):
	title = "User Type"
	help = "My command for filling up the "+title+" Model"
	def handle(self, *args, **options):
		print "Deleting Current "+self.title+"s"
		self.clear()
		print "Creating "+self.title+"s"
		self.make_data()
		print "done"
	def make_data(self):
		UserType.objects.create(name="Student")
		UserType.objects.create(name="Assessor")
		UserType.objects.create(name="Supervisor")

	def clear(self):
		UserType.objects.all().delete()