

class ElementoHtml_v1:

    tag = ""
    is_empty = False
    id = ""
    css_class = ""

    is_defined = False

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