import json
import os
import argparse

def argumentos() -> argparse.Namespace:
  """
  Parsea los argumentos de línea de comando y los devuelve como un objeto Namespace.

  Returns:
      argparse.Namespace: Un objeto que contiene los argumentos de línea de comando.
  """
  parser = argparse.ArgumentParser(description='Script para corregir y modificar archivos S4RiS JSON')
  parser.add_argument('--p', type=str, required=True, help='Ruta al archivo S4RiS JSON.')
  parser.add_argument('--n', type=str, default='Maratón', help='Nuevo nombre de la maratón.')
  parser.add_argument('--e', type=str, default='', help='Secuencia de caracteres a eliminar de los nombres.')
  parser.add_argument('--f', choices=range(301), type=int, default=240, help='Tiempo (en minutos) a congelar el tablero.')
  return parser.parse_args()


def main() -> None:
  """
  Abre el archivo S4RiS JSON especificado, realiza las correcciones y modificaciones correspondientes
  y guarda el resultado en el mismo archivo.
  """
  args = argumentos()

  if not os.path.isfile(args.p):
    print(f"Error: no se puede acceder al archivo en {args.p}")
    exit(0)

  with open(args.p, 'r') as file:
    data = json.load(file)

  data['contestName'] = args.n
  data['freezeTimeMinutesFromStart'] = args.f
  data['problemLetters'].sort()
  for i in range(len(data['contestants'])):
    data['contestants'][i] = data['contestants'][i].replace(args.e, '')
  for i in range(len(data['runs'])):
    data['runs'][i]['contestant'] = data['runs'][i]['contestant'].replace(args.e, '')

  with open(args.p, 'w') as file:
    json.dump(data, file, indent=4)


if __name__ == '__main__':
  main()