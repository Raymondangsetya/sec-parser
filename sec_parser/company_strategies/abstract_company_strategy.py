from abc import ABC, abstractmethod

class AbstractSecStrategy(ABC):
    @abstractmethod
    def parse(
        self,
        document #TODO: checar tipagem
        ): # TODO: ver oq retorna
      raise NotImplementedError

class AppleSecDocumentParser(AbstractSecStrategy):
    def parse(self, document):
        print("strategy SEC document...")
        # Parse logic goes here

class AlphabetSecDocumentParser(AbstractSecStrategy):
    def parse(self, document):
      pass



# acho q a strategy deve ser aplicada do mount, pois vai evitar esforcos futuros
# obs: cada plugin retorna um element: AbstractSemanticElement (usar isso ao meu favor)

# obs: quero q as estrategias sejam automaticas, sem o dev ter q lembrar de botar

# CASO SecParser.parse: (ideia vencedora)
# dentro do loop de plugins
  # pega a lista de semantic elements, e se o doc for da empresa, aplica a strategia


