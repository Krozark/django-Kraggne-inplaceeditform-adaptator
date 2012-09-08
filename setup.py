from setuptools import setup, find_packages

setup(
    name='Kraggne_inplaceeditform_adaptator',
    version='0.1',
    description='À module that custom Kraggne template to auto work with inplaceeditform',
    long_description=open('README.md').read(),
    author='Maxime Barbier',
    author_email='maxime.barbier1991@gmail.com',
    url='https://github.com/Krozark/Krozark/django-Kraggne-inplaceeditform-adaptator/tree/master',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 0 ',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires = [
        "django-Kraggne",
        "django-inplaceeditform"
    ],
    zip_safe=False,
)
