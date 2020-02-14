



var num = 10;      // tipos primitivos
var str = 'texto';
var bol = true;
var und = undefined;
var nul = null;

console.log( num);
num = str;         // Escritura dinamica, variables no sujetas a sus valores originales
console.log( num);

bol = 10;
console.log( bol );

// Objetos
// var obj = {}; Objeto vacio
// Cada objeto puede tener tipos primitivos u objetos

var obj = {
    numero: 10, // Nomeclatura de pares, cada nomeclatura se separa por coma excepto la ultima
    texto: 'Nuevo Texto', 
    
    objHijo: {
        numero2: 20,
        texto2: 'amargo'
               
    }
    
};    

// Por valor y por referencia

var a = 10;
var b = a;

console.log('a: ', a);
console.log('b: ', b);

a = 20; // pasar por valor, ellos poseen distintos espacios de memoria

console.log('a: ', a);
console.log('b: ', b);

// Variable primitivas siempre se pasan por valor, objetois por referencia

var c = {
    nombre:'Juana'
};

var d = c; // c es la raiz al ser donde se aloja el objeto

console.log('c: ', c); //d adquiere el valor de c tambien
console.log('d: ', d);

c.nombre = 'Maria';

console.log('c: ', c); // Ambos cambian de nombre ahora
console.log('d: ', d);

d.nombre = 'Pedro';

console.log('c: ', c); // ambas cambian, ambas variables estan amarradas
console.log('d: ', d); // eso se llama pasar por referencia. ambos    tienen mismo espacio de memoria





