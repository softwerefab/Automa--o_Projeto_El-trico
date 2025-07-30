from setuptools import setup, find_packages

setup(
    name='ai-electrical-project-generator',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='An application that uses AI to generate electrical projects from natural language prompts.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'ezdxf',
        'svgwrite',
        'transformers',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)