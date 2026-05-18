import os
import sys
import requests

def buscar_en_api(categoria_endpoint, nombre_item):
    url_base = os.getenv("ELDEN_API_URL", "https://eldenring.fanapis.com/api")
    url = f"{url_base}/{categoria_endpoint}"
    
    parametros = {"name": nombre_item}
    
    try:
        print(f"🕵️ Buscando '{nombre_item}' en la categoría '{categoria_endpoint}'...")
        respuesta = requests.get(url, params=parametros, timeout=10)
        
        respuesta.raise_for_status() 
        
        datos_json = respuesta.json()
        
        if datos_json.get('data') and len(datos_json['data']) > 0:
            item = datos_json['data'][0]
            
            print("\n=============================================")
            print("📜 RESULTADO ENCONTRADO (STAKEHOLDER INFO)")
            print("=============================================")
            print(f"🔹 Nombre: {item.get('name')}")
            print(f"📝 Descripción: {item.get('description', 'Sin descripción disponible.')}")
            
            if categoria_endpoint == "weapons":
                ataque = item.get('attack', [])
                daño_fisico = next((i['amount'] for i in ataque if i['name'] == 'Phy'), 'N/A')
                print(f"⚔️ Daño Físico Base: {daño_fisico}")
            elif categoria_endpoint == "armors":
                peso = item.get('weight', 'N/A')
                print(f"🛡️ Peso de la Armadura: {peso}")
            else:
                print(f"🆔 ID del Objeto: {item.get('id')}")
                
            print("=============================================\n")
        else:
            print(f"⚠️ No se encontró ningún elemento que coincida con '{nombre_item}'.")

    except requests.exceptions.HTTPError as errh:
        print(f"❌ Error HTTP específico (Servidor respondió con error): {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"❌ Error de Conexión (Verifica tu entorno de red): {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"❌ Error de Tiempo de Espera (API agotó el tiempo): {errt}")
    except requests.exceptions.RequestException as err:
        print(f"❌ Error General de la solicitud/petición: {err}")
    except Exception as e:
        print(f"❌ Error inesperado en el procesamiento de datos: {e}")

if __name__ == "__main__":
    categoria = os.getenv("ELDEN_CATEGORIA", "weapons")
    item_a_buscar = os.getenv("ELDEN_ITEM", "Uchigatana")
    
    buscar_en_api(categoria, item_a_buscar)
    