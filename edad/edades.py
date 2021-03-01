import web
import json
urls = (
    '/read?', 'edades'
)
app = web.application(urls, globals())

class edades:


    def _init_(self):
      pass
        
     
    def GET(self):
        try:
            edad = web.input() 
            nombre = edad.nombre
            dia = int(edad.dia)
            mes = edad.mes
            nacimiento = int(edad.nacimiento)
            edad = 2021 - nacimiento
            info={}
            info["Nombre:"] = nombre
            info["Dia de nacimineto"] = dia
            info["Mes de nacimiento"] = mes
            info["Año de nacimiento"] = nacimiento
            info["Edad"] = edad
            texto = open("static/datos.txt","a")
            texto.write("\n")
            texto.write(str(info))
            texto.close()
            return json.dumps(info)

        except:
          info = {}
          info["ERROR"] = "Verifica tus datos"
          return json.dumps(info)
       
            

if __name__ == "__main__":

  app.run()


