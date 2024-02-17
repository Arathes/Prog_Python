setup_string = f'''
"""
setup file for project {project_name}
"""

from pathlib import Path
from setuptools import setup

def read(fname):
    f_path = Path(__file__).parent / fname
    return f_path.read_text()


setup(
    name="{package_name}",
    version="{project_version}",
    # replace underline characters by spaces
    author="{author_name.replace('_', ' ')}",
    author_email="Vorname.Nachname@gmail.com",
    description=("A very simple setup.py file"),
    license="GPL",
    keywords="example",
    url="http://myUrl.com",
    packages=["{package_name}"],
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Demonstration",
        "License :: GPL License",
    ],
    python_requires=">=3.10, <4",
    install_requires=["setuptools>=60"],
    entry_points=dict(console_scripts= [
            "add_float={package_name}.add_sub:add_main",
        ]
    ),
)
'''

with open(project_path / "setup.py", "w") as setup_file:
    setup_file.write(setup_string)