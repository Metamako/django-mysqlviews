from setuptools import setup, find_packages

LONG_DESCRIPTION = ''

try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass

setup(
    name='django-postgresviews',
    version='0.0.1',
    description="Define PostgreSQL Views with Django models.",
    long_description=LONG_DESCRIPTION,
    author='Eric Man',
    author_email='meric.au@gmail.com',
    license='BSD',
    packages=find_packages(),
    url='https://github.com/meric/django-postgresviews',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
    ]
)
