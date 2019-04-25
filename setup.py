from setuptools import setup

setup(
    name='hebireki',
    version='0.2.0',
    packages=['hebireki'],
    package_dir={'': 'src'},
    url='https://github.com/akiyamn/hebireki',
    license='WTFPLv2',
    author='akiyamn',
    author_email='10993186+akiyamn@users.noreply.github.com',
    description='Simple implementation of the Traditional Japanese Calendar system (Wareki) by wrapping around an inbuilt datetime instance',
    keywords=["japanese", "calendar", "wareki", "era", "reiwa"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Localization',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: Public Domain',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Natural Language :: Japanese'
      ]
)
