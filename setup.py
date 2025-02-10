from setuptools import setup, find_packages

setup(
    name="mcq_gen",
    version="0.0.1",
    author="Awais Sabir",
    author_email="awaissabir16@gmail.com",
    intall_requires=['openai', 'streamlit','langchain', 'python-dotenv', 'pyPDF2'],
    packages=find_packages(),
)