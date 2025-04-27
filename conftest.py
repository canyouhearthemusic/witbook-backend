import pytest
from django.conf import settings

# Configure Django to use our test settings
@pytest.fixture(scope="session", autouse=True)
def django_setup_for_tests():
    settings.DJANGO_SETTINGS_MODULE = "test_settings" 