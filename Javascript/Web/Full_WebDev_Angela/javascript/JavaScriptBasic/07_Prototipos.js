// prototipos de javascript
// Prototipos: para gregar propiedades o metodos a un objeto de funcion de primera clase
//                   agregar propiedades o metodos a nuestro objeto pero no los puedo agregar en los primeros 3 this.
//                   Los prototipos permiten expandir este tipo de objetos y agregarle propiedades.
// Su objetivo es hacer mas eficiente el uso de objetos y se usa mejor en las propiedades de estos que no varian


// Function de primera clase
function Persona ( ) {
	
	this.nombre   = "Fernando";
	this.edad       = 30;
	this.apellido  = "Herrera";
	this.pais       = "Costa Rica";
	
	// Metodo para imprimir info
	//this.imprimirInfo = function ( ){
		
		//console.log ( this.nombre + " " + this.apellido + "(" + this.edad + ")");
		
	}
	


// Persona.prototype. pais = "Costa Rica"; Pero el proto no se utiliza mucho para propiedades
// El proto se utiliza mejor en metodos, funciones u otros que se repitan mucho en diferentes situaciones como objetos derivados de un objeto madre

Persona.prototype.imprimirInfo = function ( ){
		
		console.log ( this.nombre + " " + this.apellido + "(" + this.edad + ")");
		
	}

// Variable que inicializa la funcion Persona
var fer = new Persona ( );

// Inicializacion de la funcion imprimirInfo
//fer.imprimirInfo(); 

// Cuando uso solo este console.log me sale el objeto con sus propiedades excepto las agregadas por el prototipo: Persona {nombre: "Fernando", edad: 30, apellido: "Herrera", imprimirInfo: ƒ}
// Cuando utilizo la inicializacion anterior de imprimirInfo me sale lo que esta dentro de esa funcion: Fernando Herrera(30)
console.log ( fer ); 
console.log ( fer.pais ); 
console.log ( fer.imprimirInfo() );  // Aca se inicializa el prototipo



Number.prototype.esPositivo = function () {
	if ( this > 0){
		return true;
	}else{
		return false;
	}
}

// No es recomendable meter prototipos a las variables nativas, principales. Lo mejor en ese case es hacer un archivo para ellas
// Tambien es bueno meter prot en clases u objetos personalizados