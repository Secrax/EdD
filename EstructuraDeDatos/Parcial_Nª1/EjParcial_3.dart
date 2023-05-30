import 'dart:io';
import 'dart:math';

void main() {
  Random random = Random();
  List lista1 = List.generate(5, (index) => random.nextInt(10));
  print("La primera lista que ocuparemos es: $lista1");
  List lista2 = [];
  for (var i = 0; i < 5; i) {
    print("\nIngrese numero para agregar a la lista que sea entero: ");
    var valor = stdin.readLineSync();//Nose como hacer un input pero para enteros 
    if valor == int;
      int numero = valor;
      if (numero > 0) ;
      lista2.add(numero);
      i = i + 1;
    
  }
  List listaNueva = lista1 + lista2;//Concanedamos las listas
  print(listaNueva);
  List reemplazar = [14, 20, 7];//generamos una lista con los datos que queremos reemplazar

  listaNueva.replaceRange(6, 9, reemplazar);//Con esta funcion reemplazamos en el rango que queremos de la lista
  //recordar que el contador empieza desde 0, el primer caracter es donde inicia el siugiente donde finaliza
  //y al final lo que queremos reemplazar

  print(listaNueva);
  (listaNueva).sort((a, b) => b.compareTo(a));
}
