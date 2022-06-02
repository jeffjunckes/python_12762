""" ********** ********** ********** ********** ********** ********** **********
    External Modules
********** ********** ********** ********** ********** ********** ********** """
import cherrypy
import os
import markdown

""" ********** ********** ********** ********** ********** ********** **********
    Project Modules
********** ********** ********** ********** ********** ********** ********** """
from classes.ElementoHtml_v1 import ElementoHtml_v1
from classes.ElementoHtml_v2 import ElementoHtml_v2
from classes.ElementoHtml_v3 import ElementoHtml_v3

from classes.FormHtml_v1 import FormHtml_v1
from classes.FormHtml_v2 import FormHtml_v2

from classes.ElementoHtml_v3 import ElementoHtml_v3 as ElementoHtml
from classes.FormHtml_v2 import FormHtml_v2 as FormHtml
""" ********** ********** ********** ********** ********** ********** **********
    Module: class AppWeb
********** ********** ********** ********** ********** ********** ********** """
class AppWeb:

    s_titulo_da_pagina = ""
    html_menu_navegacao = ""
    html_conteudo = ""

    """ ********** ********** ********** ********** ********** ********** **********
        Method: index
    ********** ********** ********** ********** ********** ********** ********** """
    @cherrypy.expose
    def index(self):
        self.s_titulo_da_pagina = "Curso de Python - 12762"
        self.html_menu_navegacao = self.menuDeNavegacao()
        self.html_conteudo_pagina = "<p>Conteúdo</p>"
        return self.montarPagina()

    """ ********** ********** ********** ********** ********** ********** **********
        Method: carregar_items_navegacao
    ********** ********** ********** ********** ********** ********** ********** """
    def carregar_items_navegacao(self):
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
        self.s_titulo_da_pagina = "Curso de Python - Trilhas de Conhecimento"
        self.html_menu_navegacao = self.menuDeNavegacao()
        self.html_conteudo_pagina = "<h3>Trilhas de Conhecimento</h3>"
        return self.montarPagina()

    """ ********** ********** ********** ********** ********** ********** **********
        Method: trilhaDePython
    ********** ********** ********** ********** ********** ********** ********** """
    @cherrypy.expose
    def trilhaDePython(self, modulo = 0):

        s_modulo = modulo

        html_conteudo_trilha = """
            <form action="trilhaDePython">
                <label>Selecione um módulo:</label><br />
                <select id="selectModulo" name="modulo">
                    <option value="1">Orientação a objetos - I</option>
                    <option value="2">Orientação a objetos - II</option>
                    <option value="3">MVC</option>
                    <option value="5">Arquivos</option>
                </select><br />
                <hr />
                <input type="submit" value="Carregar módulo" /><br />
            </form><br />
        """

        html_conteudo_modulo = "Nenhum módulo selecionado."
        if (s_modulo != "0"):
            if (s_modulo == "1"):
                str_conteudo_arquivo = self.lerArquivo_read("arquivos/python_oop_1.markdown")
                # html = markdown.markdown(your_text_string)
                html_conteudo_modulo = markdown.markdown(str_conteudo_arquivo)
            elif (s_modulo == "2"):
                str_conteudo_arquivo = self.lerArquivo_read("arquivos/python_oop_2.markdown")
                # html = markdown.markdown(your_text_string)
                html_conteudo_modulo = markdown.markdown(str_conteudo_arquivo)
            elif (s_modulo == "3"):
                html_conteudo_modulo = "Módulo MVC"
            elif (s_modulo == "5"):
                str_conteudo_arquivo = self.lerArquivo_read("arquivos/arquivo_teste.txt")
                html_conteudo_modulo = self.lerArquivo_read("arquivos/trilha_de_python.html") % str_conteudo_arquivo
            else:
                html_conteudo_modulo = "Módulo não encontrado"

        html_conteudo_trilha = html_conteudo_trilha + """
            <hr />
            <div id="divModuloPython">
                %s
            </div>
            <hr />
        """ % html_conteudo_modulo

        self.s_titulo_da_pagina = "Curso de Python - Trilhas de Python"
        self.html_menu_navegacao = self.menuDeNavegacao()
        self.html_conteudo_pagina =  """
                        <style>
                            code {
                                color: rgb(255, 255, 100);
                                font-size: 16px;

                                margin: 15px;
                            }
                        </style>
                        <div id="divTrilhaDePython">
                            %s
                        </div>
        """  % (html_conteudo_trilha)
        return self.montarPagina()

    """ ********** ********** ********** ********** ********** ********** **********
        Method: lerArquivo_read
    ********** ********** ********** ********** ********** ********** ********** """
    def lerArquivo_read(self, s_nome_arquivo):
        str_conteudo_arquivo = ""
        arquivo = open(s_nome_arquivo, "r")
        str_conteudo_arquivo = arquivo.read()
        arquivo.close()
        return str_conteudo_arquivo

    """ ********** ********** ********** ********** ********** ********** **********
        Method: lerArquivo_readlines
    ********** ********** ********** ********** ********** ********** ********** """
    def lerArquivo_readlines(self, s_nome_arquivo):
        lst_conteudo_arquivo = []
        arquivo = open(s_nome_arquivo, "r")
        lst_conteudo_arquivo = arquivo.readlines()
        arquivo.close()
        return lst_conteudo_arquivo

    """ ********** ********** ********** ********** ********** ********** **********
        Method: trilhaDeHtml
    ********** ********** ********** ********** ********** ********** ********** """
    @cherrypy.expose
    def trilhaDeHtml(self):
        str_conteudo_trilha = self.lerArquivo_read("arquivos/trilha_de_html.txt")
        # html = markdown.markdown(your_text_string)
        html_conteudo_trilha = markdown.markdown(str_conteudo_trilha)

        self.s_titulo_da_pagina = "Curso de Python - Trilhas de HTML"
        self.html_menu_navegacao = self.menuDeNavegacao()
        self.html_conteudo_pagina = """
                        <div id="divTrilhaDeHtml">
                            %s
                        </div>
        """  % (html_conteudo_trilha)
        return self.montarPagina()

    """ ********** ********** ********** ********** ********** ********** **********
        Method: linksExternos
    ********** ********** ********** ********** ********** ********** ********** """
    @cherrypy.expose
    def linksExternos(self):
        str_links_externos = self.lerArquivo_read("arquivos/links_externos.markdown")
        # html = markdown.markdown(your_text_string)
        html_conteudo = markdown.markdown(str_links_externos)

        self.s_titulo_da_pagina = "Curso de Python - Links Externos"
        self.html_menu_navegacao = self.menuDeNavegacao()
        self.html_conteudo_pagina = """
                        <div id="divLinksExternos">
                            %s
                        </div>
        """  % (html_conteudo)
        return self.montarPagina()

    """ ********** ********** ********** ********** ********** ********** **********
        Method: paginaEmBranco
    ********** ********** ********** ********** ********** ********** ********** """
    @cherrypy.expose
    def paginaDeTestes(self, teste = "0"):

        s_teste_id = teste

        html_conteudo = """
            <form action="paginaDeTestes">
                <label>Selecione um teste:</label><br />
                <select id="selectTeste" name="teste">
                    <option value="1">Teste 1</option>
                    <option value="2">OOP - ElementoHtml (v1)</option>
                    <option value="3">OOP - ElementoHtml (v2)</option>
                    <option value="4">OOP - ElementoHtml (v3) - com erro</option>
                    <option value="5">OOP - ElementoHtml (v3) - sem erro</option>
                    <option value="6">OOP - FormHtml (v1)</option>
                    <option value="7">OOP - FormHtml (v2)</option>
                </select><br />
                <hr />
                <input type="submit" value="Executar teste" /><br />
            </form><br />
        """

        resultado_teste = "Nenhum teste selecionado."
        if (s_teste_id != "0"):
            if (s_teste_id == "1"):
                resultado_teste = "Resultado Teste 1"
            elif (s_teste_id == "2"):
                html_1 = ElementoHtml_v1()
                html_1.tag = "div"
                html_1.id = "divHtml_1"

                htmlCodigo = html_1.montarHtml("Resultado do teste 'OOP - ElementoHtml_v1' - {}".format(html_1))
                resultado_teste = html_1.montarHtml(markdown.markdown(htmlCodigo))
            elif (s_teste_id == "3"):
                html_2 = ElementoHtml_v2()
                html_2.tag = "div"
                html_2.id = "divHtml_2"
                resultado_teste = html_2.montarHtml("Resultado do teste 'OOP - ElementoHtml_v2' - {}".format(html_2))
            elif (s_teste_id == "4"):
                html_3 = ElementoHtml_v3()
                #html_3 = ElementoHtml_v3("div", "divHtml_3")
                html_3.tag = "div"
                html_3.id = "divHtml_3"
                resultado_teste = html_3.montarHtml("Resultado do teste 'OOP - ElementoHtml_v3' - {}".format(html_3))
            elif (s_teste_id == "5"):
                html_3 = ElementoHtml_v3("div", "divHtml_3")
                resultado_teste = html_3.montarHtml("Resultado do teste 'OOP - ElementoHtml_v3' - {}".format(html_3))
            elif (s_teste_id == "6"):
                form_html_1 = FormHtml_v1("form", "form_1")
                resultado_teste = form_html_1.montarHtml("Resultado do teste 'OOP - FormHtml_v1' - {}".format(form_html_1))
            elif (s_teste_id == "7"):
                form_html_2 = FormHtml_v2("form_2")
                resultado_teste = form_html_2.montarHtml("Resultado do teste 'OOP - FormHtml_v1' - {}".format(form_html_2))
            else:
                resultado_teste = "Teste não encontrado"

        html_conteudo = html_conteudo + """
            <hr />
            <div id="divResultadoDoTeste">
                %s
            </div>
            <hr />
        """ % resultado_teste

        self.s_titulo_da_pagina = "Curso de Python - Página de Testes"
        self.html_menu_navegacao = self.menuDeNavegacao()
        self.html_conteudo_pagina = """
                        <div id="divPaginaDeTestes">
                            %s
                        </div>
        """  % (html_conteudo)
        return self.montarPagina()

    """ ********** ********** ********** ********** ********** ********** **********
        Method: paginaEmBranco
    ********** ********** ********** ********** ********** ********** ********** """
    @cherrypy.expose
    def paginaEmBranco(self):
        str_conteudo = self.lerArquivo_read("arquivos/pagina_em_branco.markdown")
        # html = markdown.markdown(your_text_string)
        html_conteudo = markdown.markdown(str_conteudo)

        self.s_titulo_da_pagina = "Curso de Python - Página em Branco"
        self.html_menu_navegacao = self.menuDeNavegacao()
        self.html_conteudo_pagina = """
                        <div id="divPaginaEmBranco">
                            %s
                        </div>
        """  % (html_conteudo)
        return self.montarPagina()

    """ ********** ********** ********** ********** ********** ********** **********
        Method: montarPagina
    ********** ********** ********** ********** ********** ********** ********** """
    def montarPagina(self):
        html_cabecalho_pagina = self.montarCabecalhoDePagina()
        html_corpo_pagina = self.montarCorpoDePagina()
        html_rodape_pagina = self.montarRodapeDePagina()
        return """
        %s
        %s
        %s
        """ % (html_cabecalho_pagina, html_corpo_pagina, html_rodape_pagina)

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
                            background-color: rgba(50, 50, 100, 0.9);

                            flex-grow: 1;
                            flex-shrink: 1;
                            flex-basis: auto;

                            padding: 10px;
                        }

                        #divMenuDeNavegacao {
                            background-color: rgba(50, 50, 100, 0.4);
                        }

                        #divLinksExternos {
                            background-color: rgba(50, 100, 50, 0.4);
                        }

                        li {
                            font-size: 14px;
                            padding: 5px;
                        }

                        li a {
                            font-size: 14px;
                            padding: 5px;
                        }

                        a:link {
                            color: white;
                        }

                        a:visited {
                            color: navajowhite;
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
        """ % (self.s_titulo_da_pagina, self.html_menu_navegacao, self.html_conteudo_pagina)

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

        lst_items_navegacao = [
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
        lst_items_navegacao = self.carregar_items_navegacao()

        html_items_navegacao = ""
        for dic_item in lst_items_navegacao:
            html_items_navegacao = html_items_navegacao + """
                <li>
                    <a id="%s" href="%s" target="%s">%s</a>
                </li>
            """ % (dic_item["id"], dic_item["href"], dic_item["target"], dic_item["text"])

        # FINALIZA O CÓDIGO HTML DA LISTA MENU DE NAVEGAÇÃO E RETORNA
        return """
            <ul>
                %s
            </ul>
        """ % html_items_navegacao

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