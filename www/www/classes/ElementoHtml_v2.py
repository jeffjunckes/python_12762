

class ElementoHtml_v2:

    __tag = ""
    is_empty = False
    __id = ""
    css_class = ""

    is_defined = False

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, nova_tag):
        self.__tag = nova_tag

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

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