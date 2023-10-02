from sec_parser.data_sources.secapio_data_retriever import SecapioDataRetriever
from sec_parser.parsing_engine.sec_parser import SecParser
from sec_parser.parsing_plugins import TextPlugin
from sec_parser.semantic_tree.tree_builder import TreeBuilder
# quero q chame o sec_parser.parse primeiro
# depois quero passar o plugin table
# depois quero saber se da para alterar
# depois quero tentar mapear para empresas diferentes

def test_company_identifier_for_sec_parser():
    html = """<!DOCTYPE html>
<html>
<head>
<title>My Basic HTML Page</title>
</head>
<body>
<h1>Welcome to my basic HTML page!</h1>
<p>This is a simple HTML page.</p>
<table>table q ta escrita dentro da table</table>
</body>
</html>"""
    # o retriver daria o metada
    parser = SecParser("company_identifier")
    elements = parser.parse(html)
    print("parser company", parser.company_identifier)
    tree_builder = TreeBuilder()
    print("tree_builder", tree_builder.build(elements).render())


def test_strategy_identifier_for_sec_parser():
    html = """<!DOCTYPE html>
<html>
<head>
<title>My Basic HTML Page</title>
</head>
<body>
<h1>Welcome to my basic HTML page!</h1>
<p>This is a simple HTML page.</p>
<table>table q ta escrita dentro da table</table>
</body>
</html>"""
    # o retriver daria o metada
    parser = SecParser("Alphabet")
    elements = parser.parse(html)
    print("elements", elements)
    tree_builder = TreeBuilder()
    print("tree_builder", tree_builder.build(elements).render())

