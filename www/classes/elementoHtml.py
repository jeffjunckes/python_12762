"""
propriedades de um elemento html
    tag:  é o marcador do elemento 
    exemplo, sintaxe: <tag> </tag> para elementos que tem conteúdo.
                    ou<tag/> para elementos sem conteudo(elementos vazios)
    todo elemento html nao vazio tem um conteudo
    bVazio: para indicar se tem ou nao conteudo
    conteudo: pode ser um texto ou um (ou mais) elementos html.
    
    atributos do html:
        globais: id,class(classe de css (nao tem nada a ver com a class do python))
        todo elemento html tem

    atributos especificos:
        atributos que dependem do elemento ex: href(que é do elemento <a>
        "para criar hiperlink")
        action do elemento <form>
        <select></select> e <input/> tm o elemento type e name
     
     <tag id="id_da_tag" class="css_class"/>
     <tag id="id_da_tag" class="css_class"> CONTEUDO</tag>

"""


class elementoHtml:

    
     
    tag = ""
    b_vazio = False

    id = ""
    css_class = ""
    def montarHtml(self,conteudo):
        html = ""
        if (self.b_vazio):
            #<tag id="id_da_tag" class="css_class"/>
            html = """<%s id="%s" class="%s"/> """%(self.tag, self.id, self.css_class)
        else:
             #<tag id="id_da_tag" class="css_class"> CONTEUDO</tag>
            html = """<%s id="%s" class="%s">%s</%s> """%(self.tag, self.id, self.css_class,conteudo,self.tag)
        return html






















