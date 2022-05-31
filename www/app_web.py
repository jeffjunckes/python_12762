import cherrypy
import os
import markdown
#criando um modelo da app web.
class AppWeb: #object não é um parametro.

    sTituloDaPagina = ""
    htmlMenuDeNavegacao = ""
    htmlConteudo = ""


    @cherrypy.expose # permite que você acesse o metodo a partir de um navegador
    def index(self):#self faz referenca ao proprio objeto da classe(ele falando dele mesmo)
       
        self.htmlMenuDeNavegacao = self.menuDeNavegacao()
        self.htmlConteudo = "<p>conteúdo</p>"
        self.sTituloDaPagina = "Curso De Python - 12762"
    
        htmlCabecalhoDePagina = self.montarCabecalhoDePagina()
        htmlCorpoDePagina = self.montarCorpoDePagina()
        htmlRodapeDePagina = self.montarRodapeDePagina()
        return self.montarPagina()


    def montarPagina(self):
        htmlCabecalhoDePagina = self.montarCabecalhoDePagina()
        htmlCorpoDePagina = self.montarCorpoDePagina()
        htmlRodapeDePagina = self.montarRodapeDePagina()
        return"""
        %s
        %s
        %s
        
        
        """% (htmlCabecalhoDePagina, htmlCorpoDePagina, htmlRodapeDePagina)

    @cherrypy.expose
    def trilhasDeConhecimento(self):
        self.htmlMenuDeNavegacao = self.menuDeNavegacao()
        self.htmlConteudo = "<p>conteúdo</p>"
        self.sTituloDaPagina = "Curso De Python - trilhas de conhecimento"
        return self.montarPagina()

    @cherrypy.expose
    def trilhaDePython(self):
     
        
        strConteudoDoArquivo = self.lerArquivo_read("arquivos/teste_teste.txt")

        htmlConteudoTrilhaDePython = self.lerArquivo_read("arquivos/trilha_de_python.html") % (strConteudoDoArquivo)


        self.sTituloDaPagina = "curso de python - Trilhas de Python"
        self.htmlMenuDeNavegacao = self.menuDeNavegacao()
        self.htmlConteudo=  """
                    <div id="divTrilhaDePython"> 
                        %s
                    </div>""" %(htmlConteudoTrilhaDePython)
        return self.montarPagina()

    def lerArquivo_read(self,sNomeDoARquivo):
        strConteudo = ""
        arquivo = open(sNomeDoARquivo, "r") 
        strConteudo = arquivo.read() #vai ler o que tem no arquivo e armazenar na variavel
        arquivo.close()#vai fechar o arquivo

        return strConteudo


    def lerArquivo_readlines(self):
        lstConteudo = ""


        return lstConteudo


    @cherrypy.expose
    def trilhaDeHtml(self):
        strTrilhaDehtml = self.lerArquivo_read("arquivos/trilha_de_html.txt")
        # html = markdown.markdown(your_text_string)
        htmlConteudoTrilhahtml = markdown.markdown(strTrilhaDehtml)
        self.htmlMenuDeNavegacao = self.menuDeNavegacao()
        self.htmlConteudo = "<p>conteúdo</p>"
        self.sTituloDaPagina = "Curso De Python - Trilha De HTML"
        self.htmlConteudo = """
                    <div id="divTrilhaDePython"> 
                        %s
                    </div>""" %(htmlConteudoTrilhahtml )

        return self.montarPagina()
    @cherrypy.expose
    def linksExternos(self):
        strlinksExternos = self.lerArquivo_read("arquivos/links_externos.txt")
        # html = markdown.markdown(your_text_string)
        htmlConteudolinksExternos = markdown.markdown(strlinksExternos)
        self.htmlMenuDeNavegacao = self.menuDeNavegacao()
        self.htmlConteudo = "<p>conteúdo</p>"
        self.sTituloDaPagina = "Curso De Python - links externos"
        self.htmlConteudo = """
                    <div id="divlinks externos"> 
                        %s
                    </div>""" %(htmlConteudolinksExternos )

        return self.montarPagina()

#para diferenciar um elemento do outro , você pode pensar nas tags como objetos. 
# se é um objeto tem atributos e metodos. no caso do html tem propriedades
#todo objeto html tem um ID que usa para identificar o elemento dentro da pagina
#para colocar um ID dentro do marcador dea bertura colocamos is = "divPrincipal"
    @cherrypy.expose
    def formLogin(self):
        return  """"<!DOCTYPE html>
        <html>
            <head>
                <title>Python 12762</title>
                <style>
                    p{
                        color: darkred;
                    }
                    p{
                        
                        }
                    div{
                        background-color:lightblue;
                    }
                    #divformLogin{
                        backgound-color: rgb(200, 255, 200);
                    }
                </style>
            </head>
            <body>
                
                <div id="divPrincipal">
                <p> Curso programação em python -modulo web </p>
    
                    <div id="divformLogin">
                        
                    </div>
                </div>
            </body>
        </html>"""
    def listaDeArquivos(self):
        lstArquivos = os.listdir()
        sListaDeArquivos = "lista de arquivos"
        return lstArquivos
    def getHTMLHeader():
        return ""
        """
            <ul> <!-- ul significa unordered list -->
                <li>
                     <a href="www.algumacoisa.com"> alguma coisa </a>
                </li> <!-- li significa list item -->

                <li> 
                    <a href - "www.algumaoutracoisa.com"> alguma outra coisa </a>
                </li>

            </ul>
            lstItemDeNavegacao=[

                {
                    "id": "",
                    "href" : "",
                    "target" : "",
                    "capition": "",

                }
            ]
        """

    def menuDeNavegacao(self):
        #montagem o codigo HTML dos itens de navegação.
        lstItemsDeNavegacao = self.carregarItemsDeNavegacao()
        htmlItemsDeNavegacao = ""
        for dicItem in lstItemsDeNavegacao:
            htmlItemsDeNavegacao = htmlItemsDeNavegacao + """
                <li>
                    <a id="%s" href="%s" target="%s">%s</a>
                </li>
            
            """ %(dicItem["id"], dicItem["href"], dicItem["target"], dicItem["text"])
        #finaliza o codigo html da lista menu de navegação e retorna 
        return """
            <ul>
                %s
            </ul>
        """ % (htmlItemsDeNavegacao)

    def carregarItemsDeNavegacao(self):
        return [{
                    "id": "linkTrilhasDeConhecimento",
                    "href" : "trilhasDeConhecimento",
                    "target" : "",
                    "text": "Trilhas de conhecimento",

                },
                {
                    "id": "linkTrilhasDePython",
                    "href" : "trilhaDePython",
                    "target" : "",
                    "text": "trilha de pyhon",

                },
                {
                    "id": "linkTrilhasDeHTML",
                    "href" : "trilhaDeHtml",
                    "target" : "",
                    "text": "Trilhas de HTML",

                },
                {
                    "id": "linkLinkExterno",
                    "href" : "linksExternos",
                    "target" : "_blank",
                    "text": "links de referencia"
                    
                    
                    
               }

        ]


    def montarCabecalhoDePagina(self):
        return """
                    <!DOCTYPE html>
                            <html>
                                <head>
                                    <title>Python 12762</title>
                                    <style>
                                        body{
                                            width: 100%;
                                            height: 100%;

                                        }
                                        #divPrincipal{
                                            position: absolute;
                                            top: 0;
                                            left: 0;
                                            width: 100%;
                                            height: 100%;
                                            display: flex;
                                            flex-direction: column;
                                        }

                                        header, footer{
                                            background-color: rgba(50, 50, 100, 0.7);
                                            padding: 10px;
                                        
                                        }

                                        header{
                                            text-align: center;

                                        }
                                        main{
                                            background-color: rgba(50, 50, 100, 0.9);
                                            flex-grow: 1;
                                            flex-shrink: 1;
                                            flex-basis: auto;
                                            
                                            display: flex;
                                            flex-direction: row;

                                            padding: 10px;

                                        }
                                        #divOpcoes{
                                            height: calc(100% - 20px);
                                            width: 15%;
                                            backgound-color: rgba(50, 100, 50, 0.9);
                                            padding: 10px;
                                         }
                                        #divConteudo{
                                            height: calc(100% - 20px);
                                            background-color: rgba(50, 50, 100, 0.8);
                                            padding: 10px;

                                            flex-grow: 1;
                                            flex-shrink: 1;
                                            flex-basis: auto;
                                            padding: 10px;
                                            
                                         }
                                         #divOpcoes{
                                            height: calc(100% - 20px);
                                            width: 15%;
                                            backgound-color: rgba(250, 100, 50, 0.9);
                                            padding: 10px;}
                                        #divMenuDeNavegacao{
                                            backgound-color: rgb(200,255,200);
                                        }
                                        
                                    </style>
                                </head>
                                
                                    """

    def montarCorpoDePagina(self):

        return  """             <body>
                                     <div id="divPrincipal">
                                        <header>
                                            <h2>%s</h2>
                                    
                                        </header>
                                        <main>
                                            <div id="divOpcoes"> 
                                                <p> 
                                                   %s
                                                </p>
                                            </div>
                                            <div id="divConteudo"> 
                                                <p>
                                                    %s
                                                </p>
                                            </div>
                                
                                        </main>
                                        <footer>
                                            <p> Rodapé </p>
                                        </footer>
                                     </div>
                                </body>
            
                """ % (self.sTituloDaPagina, self.htmlMenuDeNavegacao, self.htmlConteudo)
            
    def montarRodapeDePagina(self):
        return """             
                        </html>       
        
                 """            
    
    
        



    #quando chamo uma pagina dentro do meu servidor nao preciso colocar o dominio so o nome da pag

cherrypy.quickstart(AppWeb()) #metodo que vai criar a app web, ele vai criar nosso objeto da classe app web
#



















