import requests

import requests

# Reemplaza con la IP de tu controlador XClarity
xcc_ip = "tu_xcc_ip" 

# Reemplaza con tu nombre de usuario y contraseña
username = "tu_usuario"
password = "tu_contraseña"

# URL de la API para obtener información de garantía
api_url = f"https://{xcc_ip}/redfish/v1/Systems/1/Oem/Lenovo/Warranty"

# Autenticación básica
response = requests.get(api_url, auth=(username, password), verify=False)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    warranty_data = response.json()
    # Procesa la información de garantía
    print(warranty_data)
else:
    print(f"Error al obtener la información de garantía: {response.status_code}")


def obtener_fecha_inicio_garantia(serial_number):
  """
  Obtiene la fecha de inicio de la garantía de un dispositivo Lenovo 
  usando su número de serie.

  Args:
    serial_number: El número de serie del dispositivo.

  Returns:
    La fecha de inicio de la garantía en formato YYYY-MM-DD, o None 
    si no se encuentra información.
  """
  try:
    # URL de la API de garantía de Lenovo
    api_url = f"https://pcsupport.lenovo.com/api/v3/products?serial={serial_number}"

    # Hacer la solicitud a la API
    response = requests.get(api_url)
    response.raise_for_status()  # Lanza una excepción si hay un error HTTP

    # Extraer la fecha de inicio de la garantía de la respuesta JSON
    data = response.json()
    warranty_data = data.get('Warranty')
    if warranty_data:
      start_date = warranty_data.get('StartDate')
      return start_date
    else:
      return None

  except requests.exceptions.RequestException as e:
    print(f"Error al obtener la información de garantía: {e}")
    return None

# Ejemplo de uso
serial_number = "tu_serial_number"  # Reemplaza con el número de serie real
fecha_inicio = obtener_fecha_inicio_garantia(serial_number)

if fecha_inicio:
  print(f"La fecha de inicio de la garantía es: {fecha_inicio}")
else:
  print("No se encontró información de garantía para este número de serie.")
