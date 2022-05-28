import cherrypy
import os
#criando um modelo da app web.
class AppWeb: #object não é um parametro.
    @cherrypy.expose # permite que você acesse o metodo a partir de um navegador
    def index(self):#self faz referenca ao proprio objeto da classe(ele falando dele mesmo)
        htmlNomeDaTrilha = "<h5>Inicio</h5>"
        htmlMenuDeNavegacao = self.menuDeNavegacao()
        return """"<!DOCTYPE html>
        <html>
            <head>
                <title>Python 12762</title>
                <style>
                    p{
                        color: darkred;
                    }
                    p{
                        
                        }
                    #divMenuDeNavegacao{
                        backgound-color:lightblue;
                    }
                    
                </style>
            </head>
            <body>
                <div id="divPrincipal">
                    <div id= "divCabecalho">
                
                         <h4> trilhas de conhecimento </h4>
                         <p>%s</p>
                
                    </div>

              
                    <div id="divMenuDeNavegacao">
                        %s
                    </div>
                </div>
            </body>
        </html>"""%(htmlNomeDaTrilha, htmlMenuDeNavegacao)

    @cherrypy.expose
    def trilhasDeConhecimento(self):
        return """
                <h3> Trilhas de conhecimento </h3>
        """

    @cherrypy.expose
    def trilhaDePython(self):
        htmlNomeDaTrilha = "<h5>Trilha de python</h5>"
        htmlMenuDeNavegacao = self.menuDeNavegacao()
        
        strConteudoDoArquivo = self.lerArquivo_read()
        return """
<!DOCTYPE html>
        <html>
            <head>
                <title>Python 12762</title>
                <style>
                    p{
                        color: darkred;
                    }
                    p{
                        
                        }
                    #divMenuDeNavegacao{
                        backgound-color:lightblue;
                    }
                    
                </style>
            </head>
            <body>
                <div id="divPrincipal">
                    <div id= "divCabecalho">
                
                         <h4> trilhas de conhecimento </h4>
                         %s
                
                    </div>

              
                    <div id="divMenuDeNavegacao">
                        %s
                    </div>,
                    <div id="divTrilhaDePython"> 
                        <div id="divArquivosEmPython"> 
                            <h5> abrindo um arquivo</h5>
                            <ol>
                                <li> 
                                " a função open [e utilizado para realizar operações com arquivos python
                                </li>
                                <li> 
                                    um arquivo pode ser aberto para leitura (read), escreita(write) ou acrescentar(append) conteudo                            
                                </li>
                                <li> 
                                    apos utilizado , um arquivo sempre deve ser fechado.
                                </li>
                            </ol>
                            <p>
                                sintaxe da função open- modo leitura: 
                            </p>
                            <pre>
                                arquivo = open("nomeDoArquivo.txt", "r")
                                onde nomeDoArquivo.txt é o nome do arquivo que esta sendo aberto 
                                e "r" indica que o arquivo está sendo aberto em modo leitura somente. 
                                esta função nao lê o conteudo do arquivo, abre o arquivo
                            </pre>
                            <hr/>
                                <p>
                                sintaxe da função open- modo leitura: 
                            </p>
                            <pre>
                                arquivo = open("nomeDoArquivo.txt", "r")
                                onde nomeDoArquivo.txt é o nome do arquivo que esta sendo aberto 
                                e "w" indica que o arquivo está sendo aberto em modo escrita. 
                                
                            </pre>
                            <hr/>
                            <h5> lendo os dados do arquivo </h5>
                            <ol>
                                <li>Funçao <em>read</em></li>
                                <li> função read() le dados como string</li>
                                <li>função readlines()le dados como lista</li>   

                            </ol>
                            <p> sintaxe da função <em>read</em></p>
                           
                            
                        </div>

                    </div>
                </div>
            </body>
        </html>""" %(htmlNomeDaTrilha, htmlMenuDeNavegacao,strConteudoDoArquivo)

    def lerArquivo_read(self):
        strConteudo = ""
        arquivo = open("arquivos/arquivo_teste.txt", "r") 
        strConteudo = arquivo.read() #vai ler o que tem no arquivo e armazenar na variavel
        arquivo.close()#vai fechar o arquivo

        return strConteudo


    def lerArquivo_readlines(self):
        lstConteudo = ""


        return lstConteudo


    @cherrypy.expose
    def trilhaDeHtml(self):
        return """%(htmlNomeDaTrilha, htmlMenuDeNavegacao
        """
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
                        backgound-color:lightblue;
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

                }

        ]

    #quando chamo uma pagina dentro do meu servidor nao preciso colocar o dominio so o nome da pag

cherrypy.quickstart(AppWeb()) #metodo que vai criar a app web, ele vai criar nosso objeto da classe app web
#



















