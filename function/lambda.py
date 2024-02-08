import requests

def lambda_handler(event, context):
  """
  Función Lambda que se ejecuta cada minuto para evitar la inactividad en un sitio web.
  """

  # Obtiene la dirección del sitio web del evento
  
  url = event["url"]
  #url = "https://www.google.com"
  
  # Realiza una solicitud GET a la página principal del sitio web
  try:
    response = requests.get(url)
    if response.status_code == 200:
      print(f"code:200, message:Solicitud exitosa al sitio: {url}")
      return {"code": 200, "message": f"Solicitud exitosa al sitio: {url}"}
    else:
      print(f"code:{response.status_code}, message:Solicitud fallida: {url}")
      return {"code": response.status_code, "message": f"Solicitud fallida: {url}"}
  except requests.HTTPError as e:
    if e.response.status_code == 404:
      print(f"code:400, message:Sitio web no encontrado: {url}")
      return {"code": 404, "message": f"Sitio web no encontrado: {url}"}
    else:
      print(f"code:500, message:Error interno del servidor: {url}")
      return {"code": 500, "message": f"Error interno del servidor: {url}"}
