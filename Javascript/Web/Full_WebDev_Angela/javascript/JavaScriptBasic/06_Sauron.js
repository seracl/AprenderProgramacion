//Ejercicio, juego del Señor de los anillos. Un simulador de combate
// Esta funcion comienza con mayuscula porque indica que es como una funcion de primera clase

function Jugador ( nombre ){ // Funcion en mayuscula para que tranaje como una clase
	
	this.nombre = nombre; // Parametro tipo construction que chequea el nombre que entramos
	this.pv = 100;
	this.sp = 100;
	
	// Este es tambien el primer metodo que recive un jugador por referencia y cambia sus propiedades
	// Con esta funcion los jugadores pueden curar (Una accion). 
	this.curar = function  (jugadorObjetivo) {
		
		if  ( this.sp >= 40 ){
			this.sp -= 40;
			// Forma larga: jugadorObjetivo.pv = jugadorObjetivo.pv + 20
			jugadorObjetivo.pv += 20;		
			
		} else {
			
			console.info ( this.nombre + "  no tiene SP" );	
			
		}
		
		this.estado ( jugadorObjetivo);	  
	}
	
	this.tirarFlecha = function (jugadorObjetivo){
		
		if ( jugadorObjetivo.pv > 40 ){
			
			jugadorObjetivo.pv -= 40;
			
		}else{
			jugadorObjetivo.pv = 0;
			console.error ( jugadorObjetivo.nombre + " murio!!!" );
		}
		
		this.estado ( jugadorObjetivo);
	}
	
	this.golpeEspada = function ( jugadorObjetivo) {
		
		if ( jugadorObjetivo.pv > 40 ){
			
			jugadorObjetivo.pv -= 40;
			
		}else{
			jugadorObjetivo.pv = 0;
			console.error ( jugadorObjetivo.nombre + " murio!!!" );
		}
		
		this.estado ( jugadorObjetivo);
		
	}
	
	// Con esta funcion abarco los consoleLogs excepto los dos primeros
	this.estado = function (jugadorObjetivo){
		
		console.info ( this );
		console.info ( jugadorObjetivo );
		
	}
};

// Definicion de las variables del objeto
var gandalf = new Jugador ("Gandalf"); 
var legolas = new Jugador ("Legolas");
var aragorn = new Jugador ("Aragorn");

console.log( gandalf );
console.log( legolas );
console.log( aragorn );


gandalf.curar ( legolas );
