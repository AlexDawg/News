from django.core.management.base import BaseCommand, CommandError
from NewsPortal.models import Post, Category


class Command(BaseCommand):
    help = 'Удалить посты в категории!'

    def add_arguments(self, parser):
        parser.add_argument('name_category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["name_category"]}? yes/no')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return
        try:
            category = Category.objects.get(name_category=options['name_category'])
            Post.objects.filter(categories=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news from category {category.name_category}')) # в случае неправильного подтверждения говорим, что в доступе отказано
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category {category.name_category}'))