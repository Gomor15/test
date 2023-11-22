from django.test import RequestFactory, TestCase
from tree_menu.models import Menu
from tree_menu.views import IndexPageView


class IndexPageViewTests(TestCase):
    def setUp(self) -> None:

        self.factory = RequestFactory()
        self.menu = Menu.objects.create(title="main_menu", slug="main_menu")

    def test_get_context_data(self) -> None:

        request = self.factory.get('/')
        response = IndexPageView.as_view()(request)
        menu = response.context_data['menu']

        self.assertEqual(menu, self.menu)

    def test_get_response_status_code(self) -> None:

        request = self.factory.get('/')
        response = IndexPageView.as_view()(request)

        self.assertEqual(response.status_code, 200)