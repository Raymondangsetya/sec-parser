from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from sec_parser.parsing_engine.abstract_parser import AbstractSemanticElementParser
from sec_parser.parsing_engine.html_parsers.root_tag_parser import (
    AbstractHtmlTagParser,
    RootTagParser,
)
from sec_parser.parsing_plugins.footnote_and_bulletpoint_plugin import (
    FootnoteAndBulletpointPlugin,
)
from sec_parser.parsing_plugins.highlighted_text_plugin import HighlightedTextPlugin
from sec_parser.parsing_plugins.image_plugin import ImagePlugin
from sec_parser.parsing_plugins.root_section_plugin import RootSectionPlugin
from sec_parser.parsing_plugins.table_plugin import TablePlugin
from sec_parser.parsing_plugins.text_plugin import TextPlugin
from sec_parser.parsing_plugins.title_plugin import TitlePlugin
from sec_parser.semantic_elements.semantic_elements import (
    TextElement,
    UndeterminedElement,
)

from sec_parser.company_strategies.strategies_map import strategies

if TYPE_CHECKING:
    from sec_parser.parsing_plugins.abstract_parsing_plugin import AbstractParsingPlugin
    from sec_parser.semantic_elements.abstract_semantic_element import (
        AbstractSemanticElement,
    )

class SecParser(AbstractSemanticElementParser):
    def __init__(
        self,
        company_identifier = None,
        create_plugins: Callable[[], list[AbstractParsingPlugin]] | None = None,
        *,
        root_tag_parser: AbstractHtmlTagParser | None = None,
    ) -> None:
        self.create_plugins: Callable = create_plugins or self.create_default_plugins
        self._root_tag_parser = root_tag_parser or RootTagParser()
        self.company_identifier = company_identifier

    def create_default_plugins(
        self,
    ) -> list[AbstractParsingPlugin]:
        return [
            ImagePlugin(),
            TablePlugin(process_only={UndeterminedElement}),
            TextPlugin(process_only={UndeterminedElement}),
            FootnoteAndBulletpointPlugin(process_only={TextElement}),
            HighlightedTextPlugin(process_only={TextElement}),
            TitlePlugin(),
            RootSectionPlugin(),
        ]

    def parse(self, html: str) -> list[AbstractSemanticElement]:
        plugins = self.create_plugins()

        # The parsing process is designed to handle the primarily
        # flat HTML structure of SEC filings. Hence, our focus is on
        # the root tags of the HTML document.
        root_tags = self._root_tag_parser.parse(html)

        elements: list[AbstractSemanticElement] = [
            UndeterminedElement(tag, inner_elements=[]) for tag in root_tags
        ]

        for plugin in plugins:
            elements = plugin.transform(elements)
            strategy = strategies.get(self.company_identifier)
            for element in elements:
               if strategy:
                  strategy.process(element)
        return elements


# dar um jeito de saber quando usar cada estrategia
# ideias:
# aceitar parametro no SecParser passando o nome da empresa ou algum identificador
  # o if iria verificar se esse parametro existe
    # caso sim mete a strategy, caso nao nao
