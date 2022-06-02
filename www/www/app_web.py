import cherrypy
import os
import markdown

class AppWeb:

    sTituloDaPagina = ""
    htmlMenuDeNavegacao = ""
    htmlConteudo = ""

    """ ********** ********** ********** ********** ********** ********** **********
        Method: index
    ********** ********** ********** ********** ********** ********** ********** """
    @cherrypy.expose
    def index(self):
        self.sTituloDaPagina = "Curso de Python - 12762"
        self.htmlMenuDeNavegacao = self.menuDeNavegacao()
        self.htmlConteudo = "<p>Conteúdo</p>"
        return self.montarPagina()

    """ ********** ********** ********** ********** ********** ********** **********
        Method: carregarItemsDeNavegacao
    ********** ********** ********** ********** ********** ********** ********** """
    def carregarItemsDeNavegacao(self):
        return [{
                "id": "linkTrilhasDeConhecimento",
                "href": "trilhasDeConhecimento",
                "target": "",
                "text": "Trilhas de Conhecimento",
            }, {
                "id": "linkTrilhaDePython",
                "href": "trilhaDePython",
                "target": "",
                "text": "Trilha de Python",
            }, {
                "id": "linkTrilhaDeHtml",
                "href": "trilhaDeHtml",
                "target": "",
                "text": "Trilha de Html",
            }, {
                "id": "linkLinksExternos",
                "href": "linksExternos",
                "target": "",
                "text": "Links de Referência",
            }, {
                "id": "linkPaginaDeTestes",
                "href": "paginaDeTestes",
                "target": "",
                "text": "Página de Testes",
            }, {
                "id": "linkPaginaEmBranco",
                "href": "paginaEmBranco",
                "target": "",
                "text": "Página em Branco",
            }
        ]

    """ ********** ********** ********** ********** ********** ********** **********
        Method: trilhasDeConhecimento
    ********** ********** ********** ********** ********** ********** ********** """
    @cherrypy.expose
    def trilhasDeConhecimento(self):
        self.sTituloDaPagina = "Curso de Python - Trilhas de Conhecimento"
        self.htmlMenuDeNavegacao = self.menuDeNavegacao()
        self.htmlConteudo = "<h3>Trilhas de Conhecimento</h3>"
        return self.montarPagina()

    """ ********** ********** ********** ********** ********** ********** **********
        Method: trilhaDePython
    ********** ********** ********** ********** ********** ********** ********** """
    @cherrypy.expose
    def trilhaDePython(self):

        strConteudoDoArquivo = self.lerArquivo_read("arquivos/arquivo_teste.txt")

        htmlConteudoTrilhaDePython = self.lerArquivo_read("arquivos/trilha_de_python.html") % strConteudoDoArquivo

        self.sTituloDaPagina = "Curso de Python - Trilhas de Python"
        self.htmlMenuDeNavegacao = self.menuDeNavegacao()
        self.htmlConteudo =  """
                        <div id="divTrilhaDePython">
                            %s
                        </div>
        """  % (htmlConteudoTrilhaDePython)
        return self.montarPagina()

    """ ********** ********** ********** ********** ********** ********** **********
        Method: lerArquivo_read
    ********** ********** ********** ********** ********** ********** ********** """
    def lerArquivo_read(self, sNomeDoArquivo):
        strConteudo = ""
        arquivo = open(sNomeDoArquivo, "r")
        strConteudo = arquivo.read()
        arquivo.close()
        return strConteudo

    """ ********** ********** ********** ********** ********** ********** **********
        Method: lerArquivo_readlines
    ********** ********** ********** ********** ********** ********** ********** """
    def lerArquivo_readlines(self):
        lstConteudo = []
        return lstConteudo

    """ ********** ********** ********** ********** ********** ********** **********
        Method: trilhaDeHtml
    ********** ********** ********** ********** ********** ********** ********** """
    @cherrypy.expose
    def trilhaDeHtml(self):
        strTrilhaDeHtml = self.lerArquivo_read("arquivos/trilha_de_html.txt")
        # html = markdown.markdown(your_text_string)
        htmlConteudoTrilhaDeHtml = markdown.markdown(strTrilhaDeHtml)

        self.sTituloDaPagina = "Curso de Python - Trilhas de HTML"
        self.htmlMenuDeNavegacao = self.menuDeNavegacao()
        self.htmlConteudo = """
                        <div id="divTrilhaDeHtml">
                            %s
                        </div>
        """  % (htmlConteudoTrilhaDeHtml)
        return self.montarPagina()

    """ ********** ********** ********** ********** ********** ********** **********
        Method: linksExternos
    ********** ********** ********** ********** ********** ********** ********** """
    @cherrypy.expose
    def linksExternos(self):
        strLinksExternos = self.lerArquivo_read("arquivos/links_externos.markdown")
        # html = markdown.markdown(your_text_string)
        htmlConteudoLinksExternos = markdown.markdown(strLinksExternos)

        self.sTituloDaPagina = "Curso de Python - Links Externos"
        self.htmlMenuDeNavegacao = self.menuDeNavegacao()
        self.htmlConteudo = """
                        <div id="divLinksExternos">
                            %s
                        </div>
        """  % (htmlConteudoLinksExternos)
        return self.montarPagina()

    """ ********** ********** ********** ********** ********** ********** **********
        Method: paginaEmBranco
    ********** ********** ********** ********** ********** ********** ********** """
    @cherrypy.expose
    def paginaDeTestes(self, teste = "0"):

        sTeste = teste

        if (sTeste == "0"):
                htmlConteudo = """
                    <form action="paginaDeTestes">
                        <label>Selecione um teste:</label><br />
                        <select id="selectTeste" name="teste">
                            <option value="1">Teste 1</option>
                            <option value="2">Teste 2</option>
                            <option value="3">Teste 3</option>
                        </select><br />
                        <hr />
                        <input type="submit" value="Executar teste" /><br />
                    </form>
                """
        else:
            if (sTeste == "1"):
                resTeste = "Resultado Teste 1"
            elif (sTeste == "2"):
                resTeste = "Resultado Teste 2"
            elif (sTeste == "3"):
                resTeste = "Resultado Teste 3"
            else:
                resTeste = "Teste não encontrado"

            htmlConteudo = """
                <div id="divResultadoDoTeste">
                    %s
                </div>
            """ % resTeste

        self.sTituloDaPagina = "Curso de Python - Página de Testes"
        self.htmlMenuDeNavegacao = self.menuDeNavegacao()
        self.htmlConteudo = """
                        <div id="divPaginaDeTestes">
                            %s
                        </div>
        """  % (htmlConteudo)
        return self.montarPagina()

    """ ********** ********** ********** ********** ********** ********** **********
        Method: paginaEmBranco
    ********** ********** ********** ********** ********** ********** ********** """
    @cherrypy.expose
    def paginaEmBranco(self):
        strConteudo = self.lerArquivo_read("arquivos/pagina_em_branco.markdown")
        # html = markdown.markdown(your_text_string)
        htmlConteudo = markdown.markdown(strConteudo)

        self.sTituloDaPagina = "Curso de Python - Página em Branco"
        self.htmlMenuDeNavegacao = self.menuDeNavegacao()
        self.htmlConteudo = """
                        <div id="divPaginaEmBranco">
                            %s
                        </div>
        """  % (htmlConteudo)
        return self.montarPagina()

    """ ********** ********** ********** ********** ********** ********** **********
        Method: montarPagina
    ********** ********** ********** ********** ********** ********** ********** """
    def montarPagina(self):
        htmlCabecalhoDePagina = self.montarCabecalhoDePagina()
        htmlCorpoDePagina = self.montarCorpoDePagina()
        htmlRodapeDePagina = self.montarRodapeDePagina()
        return """
        %s
        %s
        %s
        """ % (htmlCabecalhoDePagina, htmlCorpoDePagina, htmlRodapeDePagina)

    """ ********** ********** ********** ********** ********** ********** **********
        Method: montarCabecalhoDePagina
    ********** ********** ********** ********** ********** ********** ********** """
    def montarCabecalhoDePagina(self):
        return """
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Python 12762</title>
                    <style>
                        body {
                            width: 100%;
                            height: 100%;
                        }

                        #divPrincipal {
                            position: absolute;
                            top: 0;
                            left: 0;
                            width: 100%;
                            height: 100%;

                            display: flex;
                            flex-direction: column;
                        }

                        header, footer {
                            background-color: rgba(50, 50, 100, 0.7);
                            padding: 10px;
                        }

                        header {
                            text-align: center;
                        }

                        main {
                            background-color: rgba(50, 50, 100, 0.9);
                            flex-grow: 1;
                            flex-shrink: 1;
                            flex-basis: auto;

                            display: flex;
                            flex-direction: row;

                            padding: 10px;
                        }

                        #divOpcoes {
                            height: calc(100% - 20px);
                            width: 15%;
                            background-color: rgba(50, 100, 50, 0.9);

                            padding: 10px;
                        }

                        #divConteudo {
                            height: calc(100% - 20px);
                            background-color: rgba(50, 50, 100, 0.8);

                            flex-grow: 1;
                            flex-shrink: 1;
                            flex-basis: auto;

                            padding: 10px;
                        }

                        #divMenuDeNavegacao {
                            background-color: rgb(200, 255, 200);
                        }

                        #divLinksExternos {
                            background-color: rgba(200, 255, 200, 0.8);
                        }
                    </style>
                </head>
        """

    """ ********** ********** ********** ********** ********** ********** **********
        Method: montarCorpoDePagina
    ********** ********** ********** ********** ********** ********** ********** """
    def montarCorpoDePagina(self):
        return """
                <body>
                    <div id="divPrincipal">
                        <header>
                            <h2>%s</h2>
                        </header>
                        <main>
                            <div id="divOpcoes">
                                %s
                            </div>
                            <div id="divConteudo">
                                %s
                            </div>
                        </main>
                        <footer>
                            <p>Rodapé</p>
                        </footer>
                    </div>
                </body>
        """ % (self.sTituloDaPagina, self.htmlMenuDeNavegacao, self.htmlConteudo)

    """ ********** ********** ********** ********** ********** ********** **********
        Method: montarRodapeDePagina
    ********** ********** ********** ********** ********** ********** ********** """
    def montarRodapeDePagina(self):
        return """
            </html>
        """

    """ ********** ********** ********** ********** ********** ********** **********
        Method: menuDeNavegacao

        <ul> <!-- ul: unordered list -->
            <li> <!-- li: list item -->
                <a id="aAlgumaCoisa" href="www.algumacoisa.com">Alguma Coisa</a>
            </li>
            <li>
                <a id="aOutraCoisa" href="www.outracoisa.com">Outra Coisa</a>
            </li>
        </ul>

        lstItemsDeNavegacao = [
            {
                "id": "",
                "href": "",
                "target": "",
                "text": "",
            }
        ]
    ********** ********** ********** ********** ********** ********** ********** """
    def menuDeNavegacao(self):
        # MONTAGEM DO CÓDIGO HTML DOS ITENS DE NAVEGAÇÃO
        lstItemsDeNavegacao = self.carregarItemsDeNavegacao()

        htmlItemsDeNavegacao = ""
        for dicItem in lstItemsDeNavegacao:
            htmlItemsDeNavegacao = htmlItemsDeNavegacao + """
                <li>
                    <a id="%s" href="%s" target="%s">%s</a>
                </li>
            """ % (dicItem["id"], dicItem["href"], dicItem["target"], dicItem["text"])

        # FINALIZA O CÓDIGO HTML DA LISTA MENU DE NAVEGAÇÃO E RETORNA
        return """
            <ul>
                %s
            </ul>
        """ % htmlItemsDeNavegacao

    """ ********** ********** ********** ********** ********** ********** **********
        Method: formLogin
    ********** ********** ********** ********** ********** ********** ********** """
    @cherrypy.expose
    def formLogin(self):
        return """
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Python 12762</title>
                    <style>
                        p {
                            color: darkred;
                        }

                        div {
                            background-color: lightblue;
                        }

                        #divFormLogin {
                            background-color: rgb(200, 255, 200);
                        }
                    </style>
                </head>
                <body>
                    <div id="divPrincipal">
                        <p>Curso Programação em Python - módulo web</p>
                        <div id="divFormLogin">
                            <form>
                                ...
                            </form>
                        </div>
                    </div>
                </body>
            </html>
        """

    """ ********** ********** ********** ********** ********** ********** **********
        Method: listaDeArquivos
    ********** ********** ********** ********** ********** ********** ********** """
    def listaDeArquivos(self):

        lstArquivos = os.listdir("../")

        htmlListaDeArquivos = "\n<ul>\n"

        for sArquivo in lstArquivos:
            htmlListaDeArquivos = htmlListaDeArquivos + "\t<li>%s</li>\n" % sArquivo

        htmlListaDeArquivos = htmlListaDeArquivos + "</ul>\n"

        return htmlListaDeArquivos




cherrypy.quickstart(AppWeb())