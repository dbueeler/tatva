project = 'tatva'

extensions = [
    'sphinx.ext.apidoc',
    'sphinx.ext.napoleon',
]

html_theme = 'sphinx_book_theme'
html_title = 'Lego-like building blocks for FEM'
html_logo = '../../assets/logo.png'
html_favicon = '../../assets/favicon.png'

html_theme_options = {
    "repository_url": "https://gitlab.ethz.ch/smec/software/tatva",
    "use_repository_button": True,
    "use_source_button": True,
}
