from setuptools import setup,find_packages
#from distutils.core import setup

setup(
    name = "py_bin_wrapper",
    version = "0.1.1",
    author = "MDalai",
    author_email = "mingat.dalai@gmail.com",
    description='A sample Python project',
    long_description='A sample Python project',
    #long_description_content_type='text/x-rst',
    url = 'http://www.google.com',
    license = "MIT",


    packages=['hello'],
    package_dir={'hello': 'hello'},
    package_data={'hello': ['third_party/config/catlog.json', 'third_party/bin/print_json']},


    #py_modules=["hello/hello"],
    #install_requires=['peppercorn'],
    python_requires='>=3.6',

    entry_points={
        'console_scripts': [
            'hello=hello.hello:main',
        ],
    },

    #scripts=['src/startPotato'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
    ],
)