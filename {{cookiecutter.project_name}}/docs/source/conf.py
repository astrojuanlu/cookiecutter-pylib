from importlib.metadata import metadata

# -- Project information

_metadata = metadata("{{ cookiecutter.project_name }}")

project = _metadata["Name"]
author = _metadata["Author-email"].split("<", 1)[0].strip()
copyright = f"2022, {author}"

version = _metadata["Version"]
release = ".".join(version.split(".")[:2])


# -- General configuration

extensions = [
    "myst_parser",
    "sphinx_copybutton",
]

templates_path = ["_templates"]

exclude_patterns = [
    "Thumbs.db",
    ".DS_Store",
    ".ipynb_checkpoints",
]

# -- Options for HTML output

html_theme = "furo"
html_static_path = ["_static"]
