import web
import json
urls = ('/personas?', 'edad_put_get')
app = web.application(urls, globals())


class edad_put_get():

	json_file = {}

	def read(self):
		try:
			with open("datos.json") as file:
				self.json_file = json.load(file)
			print(self.json_file)
			return json.dumps(self.json_file)

		except Exception as error:
			print("Error {}".format(error.args[0]))

	def writeedades(self, nombre, dia, mes, nacimiento, edad):
		dato = {
		    "Tu nombre es": nombre,
		    "Tu dia de nacimiento": dia,
		    "Tu mes de nacimiento": mes,
		    "Tu año de nacimiento": nacimiento,
		    "Tu edad de nacimiento": edad
		}

		with open("datos.json") as file:
			self.json_file = json.load(file)
		self.json_file["personas"].append(dato)
		with open("datos.json", "w") as file:
			json.dump(self.json_file, file)
		return self.read()

	def GET(self):
		try:
			informacion = web.input()
			action = informacion["action"]

			if action == "get":
				return self.read()

			elif action == "put":
				nombre = informacion.nombre
				dia = int(informacion.dia)
				mes = informacion.mes
				nacimiento = int(informacion.nacimiento)
				edad = 2021 - nacimiento
				self.writeedades(nombre, dia, mes, nacimiento, edad)
				texto = {}
				texto["texto"] = "Texto alamacenado"
				return json.dumps(texto)
		except:
			dato = {}
			dato["texto"] = "Algo esta mal en tus datos"
			return json.dumps(dato)


if __name__ == "__main__":
	app.run()