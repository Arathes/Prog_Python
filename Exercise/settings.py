from pathlib import Path

# path where the project directory should be created
base_path = Path.home() / "tmp"

project_name = "exercises"

# Please don't use spaces in the author name:
# underlines will be automatically replaced by spaces
author_name = "Fabian"

project_version = "0.0.1"
project_release = "0.0.1"

package_name = "montypython"
# name of package modules
module_names = ["calc", "plot"]

test_dir_name = "tests"
doc_dir_name = "docs"

# theme for sphinx documentation
sphinx_html_theme = "classic"

# path of project directories
project_path = base_path / project_name
# names of directories to be created
subdir_names = [package_name, test_dir_name, doc_dir_name]

# check if project path exists
if project_path.exists():
    print(f"Project path {project_path} already exists")
    print(f"Please remove or rename {project_path}")
    print("and execute this cell again.")
else:
    # create parent directory including intermediate directories
    Path.mkdir(project_path)
    # create default subdirectories
    for subdir_name in subdir_names:
        Path.mkdir(project_path / subdir_name)
    # create empty module and test files
    package_path = project_path / package_name
    test_path = project_path / test_dir_name
    for module_name in module_names:
        module_file_path = package_path / (module_name + ".py")
        module_file_path.write_text(
            f'""" TODO: Enter docstring for module {module_name}"""\n'
        )
        test_file_path = test_path / ("test_" + module_name + ".py")
        test_file_path.write_text(f'""" Tests for module {module_name}"""\n')
    print("Project directory successfully created")

    def create_init_file(dir_path: Path, comment: str) -> None:
    init_file_path = dir_path / "__init__.py"
    init_file_path.write_text(f"{comment}")

create_init_file(package_path, f'"""\nPackage {package_name}\n"""')
create_init_file(test_path, f'"""\nTests for package {package_name}\n"""')

# create README.md
(project_path / "README.md").write_text(f"{project_name} is a great project\n")