from menuz.registry import menuz
from catalog.models import Category
from pages.models import Page

menuz.register(Category, Page)
