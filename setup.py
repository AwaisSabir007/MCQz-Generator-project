from setuptools import find_packages,setup

setup(
    name='mcq_gen',
    version='0.0.1',
    author='Awais Sabir',
    author_email='awaissabir16@gamil.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)