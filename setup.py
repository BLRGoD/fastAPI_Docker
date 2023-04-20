from setuptools import setup

setup(
    name='rest_api_app',
    version='0.0.1',
    author='Ivan A.',
    author_email='ya.aif2002@yandex.ru',
    description='for kaspersky',
    install_requires=[
        'fastapi==0.70.0',
        'uvicorn==0.15.0',
        'SQLAlchemy==1.4.26',
        'pytest==6.2.5',
        'requests==2.26.0'
    ],
    script=['app/main.py', 'scripts/create_db.py']
)