#  Copyright (C) 2020  Consiglio Nazionale delle Ricerche
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU Affero General Public License as
#      published by the Free Software Foundation, either version 3 of the
#      License, or (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU Affero General Public License for more details.
#
#      You should have received a copy of the GNU Affero General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.

import docs_cnr_theme

project = 'Progetti Software - Ufficio ICT'
release = '1.0.0'
author = u'Consiglio Nazionale delle Ricerche'

show_authors = True
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'Progetti_Software_CNR.tex', project, author, 'manual'),
]
latex_elements = {
    'extraclassoptions': 'openany,oneside'
}
epub_basename = u'Progetti_Software_CNR'

html_theme = "docs_cnr_theme"
html_theme_path = [docs_cnr_theme.get_html_theme_path()]

copyright = "2020 Consiglio Nazionale delle Ricerche"
html_title = "Progetti Software - Ufficio ICT"
html_show_sourcelink = False
html_favicon = "favicon.ico"
html_logo = "logo.png"
latex_logo = 'logo.png'
html_baseurl = 'docs'
smartquotes = False
language = "it"
numfig = True
# The master toctree document.
master_doc = 'index'
source_suffix = '.rst'


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'docs_cnr_theme'
]