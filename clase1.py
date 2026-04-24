import requests

def buscar_arma_elden_ring(nombre_arma):
    # La URL base para el endpoint de armas
    url = "https://eldenring.fanapis.com/api/weapons"
    
    # Parámetros de la consulta (query parameters)
    parametros = {
        "name": nombre_arma
    }
    
    try:
        # Realizamos la petición GET
        print(f"\nConsultando la API para: {nombre_arma}...")
        respuesta = requests.get(url, params=parametros)
        
        # Verificamos que la petición fue exitosa (Código HTTP 200)
        respuesta.raise_for_status()
        
        # Convertimos la respuesta a un diccionario de Python
        datos_json = respuesta.json()
        
        # La API devuelve los resultados dentro de una lista llamada 'data'
        if datos_json.get('data') and len(datos_json['data']) > 0:
            # Tomamos el primer resultado de la lista
            arma = datos_json['data'][0]
            
            print("\n--- ¡Arma Encontrada! ---")
            print(f"🗡️ Nombre: {arma.get('name')}")
            print(f"⚖️ Peso: {arma.get('weight')}")
            print(f"⚔️ Categoría: {arma.get('category')}")
            print(f"📝 Descripción: {arma.get('description')}")
            
            # Extraer estadísticas de ataque (ejemplo: daño físico)
            ataque = arma.get('attack', [])
            daño_fisico = next((item['amount'] for item in ataque if item['name'] == 'Phy'), 'N/A')
            print(f"💥 Daño Físico Base: {daño_fisico}")
            
        else:
            # Agregué un pequeño recordatorio de que la API está en inglés
            print(f"\nNo se encontraron resultados para '{nombre_arma}'. (Asegúrate de escribir el nombre en inglés)")
            
    except requests.exceptions.RequestException as e:
        print(f"\nError al conectar con la API: {e}")

# --- AQUÍ ESTÁ EL CAMBIO PRINCIPAL ---
if __name__ == "__main__":
    print("Bienvenido al buscador de armas de Elden Ring 🗡️")
    
    # El bucle 'while True' crea un ciclo infinito
    while True:
        # input() muestra el mensaje y guarda lo que escribas en la variable
        entrada_usuario = input("\nEscribe el nombre del arma a buscar (o 'salir' para cerrar): ")
        
        # Verificamos si el usuario quiere salir del programa
        if entrada_usuario.lower() == "salir":
            print("¡Cerrando el buscador. Nos vemos en las Tierras Intermedias!")
            break  # Esto rompe el bucle infinito y termina el script
            
        # Verificamos que el usuario no haya presionado "Enter" sin escribir nada
        elif entrada_usuario.strip() == "":
            print("Por favor, escribe un nombre válido.")
            
        # Si escribió algo válido, llamamos a la función con lo que escribió
        else:
            buscar_arma_elden_ring(entrada_usuario)