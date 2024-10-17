from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta

from list.models import Task, Tag


class Command(BaseCommand):
    help = 'Fill the database with sample data for Task and Tag models'

    def handle(self, *args, **kwargs):
        Task.objects.all().delete()
        Tag.objects.all().delete()

        tag1 = Tag.objects.create(name="Work")
        tag2 = Tag.objects.create(name="Personal")
        tag3 = Tag.objects.create(name="Urgent")

        self.stdout.write(self.style.SUCCESS('Tags created successfully.'))

        task1 = Task.objects.create(
            content="Finish Django project",
            date=timezone.now(),
            deadline=timezone.now() + timedelta(days=2),
            is_completed=False,
        )
        task1.tags.add(tag1, tag3)

        task2 = Task.objects.create(
            content="Buy groceries",
            date=timezone.now(),
            deadline=timezone.now() + timedelta(days=1),
            is_completed=False,
        )
        task2.tags.add(tag2)

        task3 = Task.objects.create(
            content="Plan weekend trip",
            date=timezone.now(),
            deadline=None,
            is_completed=True,
        )
        task3.tags.add(tag2)

        self.stdout.write(self.style.SUCCESS('Tasks created successfully.'))

        for task in Task.objects.all():
            tags = ', '.join([tag.name for tag in task.tags.all()])
            self.stdout.write(f'Task: {task.content}, Tags: {tags}')
