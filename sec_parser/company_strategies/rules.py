from sec_parser.semantic_elements.abstract_semantic_element import AbstractSemanticElement
from sec_parser.semantic_elements.semantic_elements import TableElement

NEW_TEXT_INSIDE_ELEMENT = "rewrite it using a function inside the strategy"

def add_string_to_table_element(element: AbstractSemanticElement):
  if type(element) == TableElement:
    element.html_tag._text = NEW_TEXT_INSIDE_ELEMENT

def erase_all_tables_less_than_100_chars(element: AbstractSemanticElement):
  if type(element) == TableElement and len(element.html_tag.get_text()) < 100:
    element.html_tag._text = ""
