// Las funciones anonimas previenen que el codigo sea accidentalmente manipulado por otras secciones o usuarios de nuestro programa

// La variable a continuacion se encuentra en el objeto global y puede ser manipulada por cualquier parte del programa
// Para evitar eso utilizo las funciones aninomas, que no son mas que funciones sin nombre
// Eso lo hace la funcion entre parentesis, esconde la variable dentro de los parentesis del objeto global

( function() {
	
var a = 10;

console.log ( a );

// La siguiente funcion por ejemplo puede manipular la variable anterior
	function cambiarA () {
		
		a = 20;
		
	}
	
	cambiarA ();
	
	console.log ( a );
})

(); // invocacion de la funcion anonima


// OTRO TIPO DE FUNCIONES ANONIMAS

	function ejecutarFuncion ( fn ) {
		
		if (  fn () === 1  ){
			
			return true;
			
		}else{
			
			return false;
			
		}
		
	};

// La funcion console.log permite que se ejecute todo el codigo
// SI la ejecucion de funcion se hace afuera de la fuincion anonima console.log solo se ejecuta lo que le entras como parametro a la funcion peo casi nada del IF statement...

console.log( 
	
	ejecutarFuncion(
		
		function(){
			console.log("Funcion anonima ejecutada!!!");
			return 2;
			
		}
		
	)
	
	  );
	
	