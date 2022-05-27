import cherrypy
import os
#criando um modelo da app web.
class AppWeb: #object não é um parametro.
    @cherrypy.expose # permite que você acesse o metodo a partir de um navegador
    def index(self):#self faz referenca ao proprio objeto da classe(ele falando dele mesmo)
        texto = "olá 123"
        sListaArquivos = self.listaDeArquivos()
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
                    div{
                        backgound-color:lightblue;
                    }
                    #divListaDeArquivos{
                        backgound-color: rgb(200, 255, 200);
                    }
                </style>
            </head>
            <body>
                <div id="divPrincipal>
                <p> Curso programação em python -modulo web </p>
                <p> %s </p>
                    <div id="divListaDeArquivos>
                        %s
                    </div>
                </div>
            </body>
        </html>"""% (texto,sListaArquivos)
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
                <div id="divPrincipal>
                <p> Curso programação em python -modulo web </p>
    
                    <div id="divformLogin">
                        
                    </div>
                </div>
            </body>
        </html>"""
    def listaDeArquivos(self):
        lstArquivos = os.listdir()
        sListaDeArquivos = "lista de arquivos"
        return sListaDeArquivos
    def getHTMLHeader():
        return ""

cherrypy.quickstart(AppWeb()) #metodo que vai criar a app web, ele vai criar nosso objeto da classe app web
#



















