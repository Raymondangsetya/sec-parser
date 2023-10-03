from sec_parser.company_strategies.rules import NEW_TEXT_INSIDE_ELEMENT
from sec_parser.data_sources.secapio_data_retriever import SecapioDataRetriever
from sec_parser.parsing_engine.sec_parser import SecParser
from sec_parser.parsing_plugins import TextPlugin
from sec_parser.semantic_tree.tree_builder import TreeBuilder

HTML = """<!DOCTYPE html>
<html>
<head>
<title>My Basic HTML Page</title>
</head>
<body>
<h1>Welcome to my basic HTML page!</h1>
<p>This is a simple HTML page.</p>
<table>something inside the table</table>
</body>
</html>"""


def test_parameter_is_class_attribute():
    company_identifier = "CompanyID"
    parser = SecParser(company_identifier)
    elements = parser.parse(HTML)
    tree_builder = TreeBuilder()
    print("\n")
    print(tree_builder.build(elements).render())
    print("\n")
    assert parser.company_identifier == company_identifier


def test_strategy_modifies_element_with_appropriate_strategy():
    expected = NEW_TEXT_INSIDE_ELEMENT

    parser = SecParser("Alphabet")
    elements = parser.parse(HTML)
    tree_builder = TreeBuilder()

    # visual feedback
    tree_builder = TreeBuilder()
    print(tree_builder.build(elements).render())
    print("\n")

    assert elements[2].html_tag.get_text() == expected



# teste para transformar um semantic element em outro
def test_semantic_element_to_another_semantic_element():
    company_identifier = "Alphanome"
    parser = SecParser(company_identifier)
    elements = parser.parse(HTML)
    tree_builder = TreeBuilder()
    print(tree_builder.build(elements).render())
    print("\n")
    assert parser.company_identifier == company_identifier



