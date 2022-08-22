import requests
import webbrowser

url = "https://rickandmortyapi.com/api/character/1"
r = requests.get(url)
response = r.json()
j = r.json()

name = j["name"]
status = j["status"]
gender = j["gender"]
species = j["species"]
image = j["image"]
print("Nombre: {} \nEstado: {} \nGenero: {} \nEspecie: {} \nImagen: {} \n".format(name, status, gender, species, image))


def abrir_imagen():
	a = input("Abrir imagen y/n: ")
	if a == "y":
		webbrowser.open(image)
	elif a == "n":
		quit()
	else:
		return print("Error!!!!!!!!!!!!")


abrir_imagen()
