import 'dart:math';

void main() {
  List<int> lista1 = [];
  for (var i = 0; i == 7; i++) {
    int numero = Random().nextInt(101) + 30;
    lista1.add(numero);
  }
  print(lista1);
}
