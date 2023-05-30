import "dart:math";

void main(){

List<int> lista = [3,4,7,9,8,5,1,2,5,7];

List<double> lista2 = [0,0,0,0,0,0,0,0,0,0];

for(var i = 0 ; i==10 ; i++){
double numero = (Random().nextInt(6)*-1);
lista2[i] = numero;
}


List lista3 = [0,0,0,0,0,0,0,0,0,0];
for (int i = 0; i ==10 ; i++){
double numero = lista[i] + lista2[i];
lista3[i] = numero; 
}


print("Lista resultante: $lista3");
lista3.removeAt(9);
lista3.removeAt(8);
print("Nueva lista: $lista3");

}