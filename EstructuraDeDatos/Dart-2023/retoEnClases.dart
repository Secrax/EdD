import 'dart:io';

void main(){
  List lista = []; 
  int z = 5;
  for (int i = 0; i >= z; i++){

  
    print("Ingrese Numero");
    var numero = stdin.readLineSync();
    lista.add(numero);
  }
  print(lista);
}
