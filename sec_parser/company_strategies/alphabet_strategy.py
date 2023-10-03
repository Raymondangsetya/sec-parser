from sec_parser.company_strategies.abstract_company_strategy import CompanyStrategy
from sec_parser.company_strategies.rules import add_string_to_table_element


class AlphabetStrategy(CompanyStrategy):
    def process(self, element):
      add_string_to_table_element(element)
