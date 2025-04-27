import subprocess
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Format code using black and isort"

    def handle(self, *args, **kwargs):
        self.stdout.write("Formatting code with black...")
        black_result = subprocess.run(["black", "."], capture_output=True, text=True)
        self.stdout.write(black_result.stdout)
        
        self.stdout.write("Formatting imports with isort...")
        isort_result = subprocess.run(
            ["isort", "--profile", "black", "."], capture_output=True, text=True
        )
        self.stdout.write(isort_result.stdout)
        
        self.stdout.write(self.style.SUCCESS("Code formatting complete ✅")) 