// Palabra reserbada new

function persona(){
	this.nombre = "Juan";
	this.apellido = "Clark";
	this.edad = 30;
	
	//console.log("Paso por aqui")
	// New permite crear metodos
	this.nombreCompleto = function(){
		return this.nombre + " " + this.apellido + ": " + "(" + this.edad + ")";
		
	}
	
	
}


var juan =  new persona ();
// Esto  es como crear un objeto vacio (var juan = {};), pero sin el new no funciona
// Lo que hace es asignar espacio al objeto vacio persona() que se crea al agregar new
// La variable de tipo persona creada en el objeto vacio va a responder a la funcion persona
// Con en concepto new la funcion toma una forma parecida a una clase y por lo tanto se pueden agregar cualidades al objeto desde la funcion
// "persona()" es una invocacion de funcion por lo que cuando se hace esa invocacion en la variable no solo se crean los attributos del objeto sino tambien el consol.log dentro de la funcion

console.log( juan );
// New permite hacer pases por referencia
console.log( juan.nombre ); 
// Llamar la funcion incluida en el metodo dentro del console.log
console.log( juan.nombreCompleto() ); 


// Sin el new 

// "persona()" es una invocacion de funcion por lo que cuando se hace esa invocacion en la variable no solo se crean los attributos del objeto sino tambien el consol.log dentro de la funcion
// De quitar el new de la variable la funcion normal, no da error pero es solo una invocacion de funcion normal, no la creacion del objeto persona 
// Al quitar el new los this. dentro de la funcion caen dentro del this u objeto global windows
// EL new reserva espacio de memoria, crea el thsi y el contexto del objeto al que la funcion pertenece

// En resumen, con el new se pueden meter metodos (this.nombreCompleto), peopiedades (this.nombre)


//Todos estos valores se pueden mandar por parametro
// Esto es mandar por parametro: var juan =  new persona ("Juan", "Clark", 30);

function personas(nombre, apellido, edad){
	this.nombre = nombre;
	this.apellido = apellido;
	this.edad = edad;
	
		this.imprimirPersona = function(){
		return this.nombre + " " + this.apellido + ": " + "(" + this.edad + ")";
		
	}
	
	
}

var juan =  new personas ("Juan", "Clark", 31);

console.log( juan.imprimirPersona() ); 

// En otros lenguajes de programacion esto es lo que llamamos un constructor
// Un constructor es cuando a un funcion u objeto etc. se crean con valores por defecto y se pasan por referencia
