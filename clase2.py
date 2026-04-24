import requests

def buscar_en_api(categoria_endpoint, nombre_item):
    # Fíjate cómo ahora la URL se arma dinámicamente usando la categoría elegida
    url = f"https://eldenring.fanapis.com/api/{categoria_endpoint}"
    
    parametros = {
        "name": nombre_item
    }
    
    try:
        print(f"\nBuscando en la base de datos de {categoria_endpoint}...")
        respuesta = requests.get(url, params=parametros)
        respuesta.raise_for_status()
        
        datos_json = respuesta.json()
        
        if datos_json.get('data') and len(datos_json['data']) > 0:
            item = datos_json['data'][0]
            
            print("\n--- ¡Resultado Encontrado! ---")
            print(f"🔹 Nombre: {item.get('name')}")
            # Casi todos los items tienen una descripción, así que la mostramos siempre
            if item.get('description'):
                print(f"📝 Descripción: {item.get('description')}")
            
            # --- DATOS ESPECÍFICOS SEGÚN LA CATEGORÍA ---
            # Como un arma no tiene los mismos datos que un jefe, separamos la lógica
            if categoria_endpoint == "weapons":
                ataque = item.get('attack', [])
                daño_fisico = next((i['amount'] for i in ataque if i['name'] == 'Phy'), 'N/A')
                print(f"⚔️ Daño Físico Base: {daño_fisico}")
                print(f"⚖️ Peso: {item.get('weight')}")
                
            elif categoria_endpoint == "armors":
                print(f"🛡️ Categoría de Armadura: {item.get('category')}")
                print(f"⚖️ Peso: {item.get('weight')}")
                
            elif categoria_endpoint == "bosses":
                print(f"❤️ Puntos de Vida: {item.get('healthPoints')}")
                print(f"📍 Ubicación: {item.get('location')}")
                
            elif categoria_endpoint == "talismans":
                print(f"✨ Efecto: {item.get('effect')}")

        else:
            print(f"\nNo se encontraron resultados para '{nombre_item}'. (Recuerda usar los nombres en inglés)")
            
    except requests.exceptions.RequestException as e:
        print(f"\nError al conectar con la API: {e}")

# Bloque principal de ejecución
if __name__ == "__main__":
    # Este diccionario conecta la opción del menú con la palabra exacta que necesita la URL
    opciones_api = {
        "1": "weapons",
        "2": "armors",
        "3": "talismans",
        "4": "bosses",
        "5": "ashes"
    }

    print("Bienvenido a la Terminal de las Tierras Intermedias 📜")
    
    while True:
        # Mostramos el menú
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Buscar Armas")
        print("2. Buscar Armaduras")
        print("3. Buscar Talismanes")
        print("4. Buscar Jefes")
        print("5. Buscar Cenizas de Guerra")
        print("0. Salir")
        
        opcion_elegida = input("\nElige una categoría (0-5): ")
        
        if opcion_elegida == "0":
            print("¡Cerrando sistema!")
            break
            
        # Si la opción es válida (está dentro del diccionario)
        if opcion_elegida in opciones_api:
            endpoint = opciones_api[opcion_elegida]
            
            nombre_a_buscar = input("Escribe el nombre exacto de lo que buscas: ")
            
            if nombre_a_buscar.strip() != "":
                # Ejecutamos la función pasándole la categoría y el nombre
                buscar_en_api(endpoint, nombre_a_buscar)
            else:
                print("No escribiste ningún nombre. Intenta de nuevo.")
        else:
            print("Opción no válida. Por favor escribe un número del 0 al 5.")