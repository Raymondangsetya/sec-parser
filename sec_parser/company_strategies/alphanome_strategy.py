
from sec_parser.company_strategies.abstract_company_strategy import CompanyStrategy
from sec_parser.company_strategies.rules import add_string_to_table_element, erase_all_tables_less_than_100_chars


class AlphanomeStrategy(CompanyStrategy):
    def process(self, element):
      erase_all_tables_less_than_100_chars(element)
