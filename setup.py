from setuptools import setup
from sys import path

path.insert(0, '.')

NAME = "portui"

if __name__ == "__main__":

    setup(
        name=NAME,
        version="0.1.0",
        author="Tony Rogers",
        author_email="tony.rogers@rackspace.com",
        url="https://github.com/teriyakichild/portui",
        license='internal use',
        packages=[NAME, 'portui/controllers'],
        package_dir={NAME: NAME},
        package_data={
                  'portui': ['portui/*'],
                     },
        include_package_data=True,
        description="PortUI - UI for PORT",

        install_requires=['tornado==3.2'],
        entry_points={
            'console_scripts': ['portui = portui:main'],
        }
    )
