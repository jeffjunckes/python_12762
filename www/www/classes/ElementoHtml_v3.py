

class ElementoHtml_v3:

    __tag = ""
    is_empty = False
    __id = ""
    css_class = ""

    is_defined = False

    def __init__(self, tag, id):
        self.__tag = tag
        self.__id = id

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, nova_tag):
        raise ValueError("Erro: não é possível alterar o valor do atributo")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, novo_id):
        raise ValueError("Erro: não é possível alterar o valor do atributo")

    def definirElemento(self, tag, id, css_class = "", is_empty = False):
        self.tag = tag
        self.is_empty = is_empty
        self.id = id
        self.css_class = css_class

        self.is_defined = True

    def montarHtml(self, conteudo = ""):
        if (self.is_empty):
            html = """
                <%s id="%s" class="%s" />
            """ % (self.tag, self.id, self.css_class)
        else:
            html = """
                <%s id="%s" class="%s">%s</%s>
            """ % (self.tag, self.id, self.css_class, conteudo, self.tag)

        return html
