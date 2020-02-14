// var a = 30; // Variable de entorno global


function primeraFuncion() {
    //var a = 20;   // Entorno de la funcion
    console.log( a )
}

primeraFuncion();

// Sin variables da error y con variable en entorno global debajo de funcion da undefined
var a = 40;


// Funciones y procedimientos en javascript are the same
// FUnciones siempre retornan algo, ya sea resultados, undefined o la funcion en si...

// Las funciones siempre al inicio de archivo


// Funcion que retorna objetos
function imprimir(persona){
	var apellido = persona.apellido || 'Doe';
	console.log(persona.nombre + " " + apellido);
	
}


imprimir({
	nombre: 'Juan', 
	apellido: 'Padilla'
	});



imprimir({
	nombre: 'Maria', 
	apellido: 'Padilla'
	});
	

// Funcion que retorna funcion

//Con funcion anonima
function imprimir(fn){
		fn();
	
}

imprimir ( function(){ 
	
	console.log('Funcion anonima')
	
});


// Con funcion explicita
function imprimir(fn){
	
	fn();
	
}

var persona = {
	nombre: 'Juan', 
	apellido: 'Padilla'
	};

var myFuncion = function(){
	
	var apellido = persona.apellido || 'Doe';
	console.log(persona.nombre + " " + apellido);
	
};

imprimir(myFuncion);

// Funciones con valores de retorno
// Tipos de retornos: tipo primitivo, undefined, objetos, funciones o nulos
// Palabra reservada para retorno es return

// Retorna numero
function obtenerAleatorio (){
	
	return Math.random();
	
}

console.log(obtenerAleatorio() + 10);

//Retorna nombre
function obtenerNombre (){
	
	return "Juan";
	
}

console.log(obtenerNombre() + "Padilla");
var nombre = obtenerNombre();
console.log(nombre);


// Retorna boolean

function esMayor05(){
		
	if (obtenerAleatorio () > 0.5){
		return true;
		
	}else{
		return false;
	}
}

console.log( esMayor05() );


if ( esMayor05() ){
	console.log("Es Mayor 0.5");
	
}else{
	console.log("Es Menor 0.5");
}

// Retorna objeto

function crearPersona (nombre, apellido){
	// var obj = {	}; Objeto explicito
	// return {}; objeto anonimo
	return {
		nombre: nombre,
		apellido: apellido
	}
}

var persona = crearPersona("Raul", "Clark");
console.log(persona);
console.log(persona.nombre);
console.log(persona.apellido);
var persona2 = persona.nombre + " " + persona.apellido;

// Retorna funcion

function creaFunction(){
	return function(persona){
		console.log("Me creo " + persona);
		return function (){
			console.log("Segunda funcion");
		}
		
	}
}

// Cuando no tengo segunda funcion dentro
//var nuevaFuncion = creaFunction(); Si no creo variable el resultado no se ve en el console.log
//nuevaFuncion(persona2);


var nuevaFuncion = creaFunction();
var segundaFuncion = nuevaFuncion (persona2);
segundaFuncion();

// Funciones de primera clase

function a(){
	console.log("Funcion a");
}

a();

a.nombre = "Maria";
a.direccion = {
	pais: "Costa Rica",
	ciudad: "San Jose",
	edificio: {
		piso: "8vo",
		nombre: "Edificion Principal"
		
	}
}
