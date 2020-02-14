
// Metodos y objetos

// Los objetos tienen propiedades y metodos
// Propiedades ya vistas 
// Metodos = funciones dentro de objeto


// Ejemplo simple

var persona = {
	
	nombre: "Maria",
	apellido: "VIllares",
	imprimirNombre: function(){
		console.log("Nombre Completo"); // En este case la funcion busca nombre en el objeto global por lo cualk
	}
}
persona.imprimirNombre();

// Ejemplo con error de referencia 
// En este case la funcion busca nombre en el objeto global por lo cual da error

//var persona = {
	
	//nombre: "Maria",
	//apellido: "VIllares",
	//imprimirNombre: function(){
		//console.log(nombre); 
	//}
//}
//persona.imprimirNombre();


// Ejemplo con error de referencia arreglado 
var nombre = "Juan Raul";
var persona = {
	
	nombre: "Maria",
	apellido: "VIllares",
	imprimirNombre: function(){
		console.log(nombre); // Este busca en el objeto global la variable nombre
	}
}
persona.imprimirNombre();

// THIS
// Se crea cuando se crean objetos, como el "Objeto Windows". 
// Inicialmente tiene la referencia del objeto windows 

var nombre = "Juan Raul";
var persona = {
	
	nombre: "Maria",
	apellido: "VIllares",
	imprimirNombre: function(){
		console.log(this.nombre + " " + this.apellido); 
		// Este hace referencia ahora al objeto en cuestion
		// Apellido da undefined porque no esta definida dentro de la variable, pero la funcion de abajo puede acceder a caracteristicas fuera de la variable
	},
	direccion:{
		pais: "Costa Rica",
		obtenerPais: function (){
			console.log( "La direccion es en " + this.apellido ); // apunta al objeto direccion, no al objeto persona ni al global
			
			var self = this;  // Esto es para que this apunte dentro de la funcion
			
			var nuevaDireccion = function(){
				console.log(self);
				console.log("La direccion es en " + self.pais);
			}
			nuevaDireccion(); // Obtener pais ejecutara esto
			// Esta funcion apunta al objeto global
			// de este puedo acceder a cualquier variable en el entorno global excepto en la que esta funcion se encuentra
			// Para apuntar dentro de direccion sustituyo ´this por self 
		}
	}
}

persona.nombre = "Andres"; // Cambiar valores desde fuera del objeto
// LA instruccion de arriba ca,bia la propiedad nombre desde fuera del objeto
// This en este case hace referencia al valor de la propiedad en el momento en que es llamada

persona.imprimirNombre();
persona.direccion.obtenerPais();
