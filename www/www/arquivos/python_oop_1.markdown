# Orientação a Objetos - Parte I

[docs.python.org - Classes](https://docs.python.org/pt-br/3/tutorial/classes.html)

## Como criar uma nova classe

#### Código:

        class ElementoHtml:

            tag = ""
            is_empty = false
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

## Como utilizar esta classe em outro arquivo

1. Utilizando os comandos 'from' e 'import' inclua esse módulo no início do arquivo onde vai utilizar objetos da classe ElementoHtml
2. Crie um objeto:
3. Atribua valores para os atributos:
4. Execute o método montarHtml armazenando seu resultado em uma variável:

#### Código:

            from classes.ElementoHtml import ElementoHtml
            ...
            class AppWeb:
                ...
                def paginaDeTeste(self):

                    ...
                    html_1 = ElementoHtml()
                    html_1.tag = "div"
                    html_1.id = "divHtml_1"
                    resTeste = html_1.montarHtml("Resultado do teste 'OOP - ElementoHtml'")
                    ...

5. Clique no link para ver o resultado: [Objeto ElementoHtml](paginaDeTestes?teste=2)

## Encapsulamento

Observe no exemplo acima que estamos alterando o valor dos atributos do objeto atribuindo valores diretamente a eles.
Esta prática, apesar de muito utilizada, fere um dos pilares da Orientação a Objetos, **o Encapsulamento**.

A ideia fundamental do encapsulamento é **proteger os dados dos objetos**, definindo como cada propriedade pode ser acessada pelos usuários (entende-se aqui por **usuário** o programa (módulo, função ou método)) que faz uso dos objetos;

Em linguagens como C/C++ podemos qualificar as propriedades (e também os métodos) como sendo PRIVATE ou PROTECTED ou PUBLIC determinando dessa forma quem pode acessar esses recursos;

Infelizmente em PYTHON não temos esses qualificadores. Em Python todos os elemntos de um objeto são PÚBLICOS.
***Mas é possível restringir o acesso a um determinado atributo?***
Podemos utilizar algumas convenções para 'camuflar' uma propriedade, mas ela continuará sendo PÚBLICA.

1. Por convenção, começamos o nome de uma propriedade com '__' (sublinhado sublinhado); então sabemos que ela deve ser tratada como PRIVATE;
2. Criamos métodos de acesso para ela; uma para ler (get) o seu valor e outro para alterar (set) o seu valor. Estes métodos são chamados de 'setters' and 'getters'
3. Para defnirmos um método como sendo um setter ou um getter utilizamos *'decorators'*;

Veja como ficaria nossa classe ElementoHtml:

#### Código:

        class ElementoHtml:

            __tag = ""
            is_empty = false
            __id = ""
            css_class = ""

            is_defined = False

            @property
            def tag(self):
                return self.__tag

            @salario.setter
            def tag(self, nova_tag):
                self.__tag = nova_tag

            @property
            def id(self):
                return self.__id

            @id.setter
            def id(self, novo_id):
                self.__id = novo_id
                #raise ValueError("Erro: não é possível alterar o valor do atributo")

            def definirElemento(self, tag, id, css_class = "", is_empty = False):
                self.__tag = tag
                self.is_empty = is_empty
                self.__id = id
                self.css_class = css_class

                self.is_defined = True

            def montarHtml(self, conteudo = ""):
                if (self.is_empty):
                    html = """
                        <%s id="%s" class="%s" />
                    """ % (self.__tag, self.__id, self.css_class)
                else:
                    html = """
                        <%s id="%s" class="%s">%s</%s>
                    """ % (self.__tag, self.__id, self.css_class, conteudo, self.__tag)

                return html

## Construtor (ou constructor)

É um método especial, algumas vezes chamado de 'mágico', que é executado automaticamente quando um novo objeto é criado;
Pode ser utilizado para atribuir valores iniciais para os atributos de um objeto;

1. Em Python definimos um contrutor para uma classe atrevés do método __init__;

#### Código:

        class ElementoHtml:

            __tag = ""
            is_empty = false
            __id = ""
            css_class = ""

            is_defined = False

            def __init__(self, tag, id):
                self.__tag = tag
                self.__id = id

            @property
            def tag(self):
                return self.__tag

            @salario.setter
            def tag(self, nova_tag):
                self.__tag = nova_tag

            @property
            def id(self):
                return self.__id

            @id.setter
            def id(self, novo_id):
                self.__id = novo_id
                #raise ValueError("Erro: não é possível alterar o valor do atributo")

            def definirElemento(self, tag, id, css_class = "", is_empty = False):
                self.__tag = tag
                self.is_empty = is_empty
                self.__id = id
                self.css_class = css_class

                self.is_defined = True

            def montarHtml(self, conteudo = ""):
                if (self.is_empty):
                    html = """
                        <%s id="%s" class="%s" />
                    """ % (self.__tag, self.__id, self.css_class)
                else:
                    html = """
                        <%s id="%s" class="%s">%s</%s>
                    """ % (self.__tag, self.__id, self.css_class, conteudo, self.__tag)

                return html



## Herança

1. Exemplo 1

        from classes.ElementoHtml_v3 import ElementoHtml_v3

        class HtmlForm_v1(ElementoHtml_v3):
            pass

2. Exemplo 2

        from classes.ElementoHtml_v3 import ElementoHtml_v3

        class HtmlForm_v2(ElementoHtml_v3):

            def __init__(self, id):
                ElementoHtml_v3.__init("form", id)
