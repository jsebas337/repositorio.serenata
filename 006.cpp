#include <iostream>
#include <string>
 
using namespace std;
 
struct Alumno
{
    string nombre;
    string apellido;
    float nota1;
    float nota2;
    float nota3;
    float promedio;
};
 
void introducirDatos(Alumno a[], const int x);
void imprimir(const Alumno a[], const int x);
 
int main()
{
    const int x = 3;
    Alumno a[x];
 
    introducirDatos(a, x);
    imprimir(a, x);
 
    return 0;
}
 
void introducirDatos(Alumno a[], const int x)
{
    for (int i = 0; i < x; i++)
    {
        cout << endl;
        cout << "Alumno " << i + 1 << ":" << endl;
        cout << "Nombre: "; getline(cin, a[i].nombre);
        cout << "Apellido: "; getline(cin, a[i].apellido);
        cout << "Nota 1: "; cin >> a[i].nota1;
        cout << "Nota 2: "; cin >> a[i].nota2;
        cout << "Nota 3: "; cin >> a[i].nota3;
        a[i].promedio = (a[i].nota1 + a[i].nota2 + a[i].nota3) / 3;
        cin.ignore(80, '\n');
    }
}
 
void imprimir(const Alumno a[], const int x)
{
    cout << endl;
    for (int i = 0; i < x; i++)
    {
        cout << a[i].nombre << " " << a[i].apellido << endl;
           cout << "nota1: " << a[i].nota1 << endl;
           cout << "nota2: " << a[i].nota2 << endl;
           cout << "nota3: " << a[i].nota3 << endl;
           cout << "promedio: " << a[i].promedio << endl << endl;
        cout << "siguente" << endl;
       
    }
    cout << "GRACIAS POR UTILIZAR MI PROGRAMA";
}