from django.core.management import BaseCommand

from .load_category_data import Command as LoadCategories
from .load_genre_data import Command as LoadGenres
from .load_users_data import Command as LoadUsers
from .load_title_data import Command as LoadTitles
from .load_genretitle_data import Command as LoadGenresTitles
from .load_comment_data import Command as LoadComments
from .load_review_data import Command as LoadReviews


class Command(BaseCommand):
    def handle(self, *args, **options):
        LoadUsers().handle()
        LoadCategories().handle()
        LoadGenres().handle()
        LoadTitles().handle()
        LoadGenresTitles().handle()
        LoadReviews().handle()
        LoadComments().handle()
