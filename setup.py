from setuptools import setup, find_packages

setup(
    name='Alfooou',
    version='1.0.0',
    description='A maladeza package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Seu Nome',
    author_email='seuemail@example.com',
    url='https://github.com/seuuser/malware_package',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'psutil',
        'pyinjector',
        # Outras dependências, caso necessário
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
