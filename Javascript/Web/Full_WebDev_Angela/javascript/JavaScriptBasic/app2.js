// La funcion typeof nos ayuda a conocer el tipo de dato que estamos recibiendo antes de hacer alguna accion

	function identifica ( param ) {
		
		// console.log( typeof param );
		console.log( param instanceof Persona );
		
		
		// if ( typeof param == "function" ) {
			
			//param();
			
		//}else{
			
			//console.log (  param );
			
		//}
		
	}
	
	// identifica(  10 ); // Aca tambien puedo mandar un string " ", o un objeto { }...
	
	function Persona ( ) {
		
		this.nombre = "Fernando";
		this.edad = 30:
		
		
	}
	
	var juan = new Persona( ); 
	
	identifica(  fernando ); // Aca mande una funcion que no hace nada
	
	// identifica ( function ( ) { console.log("soy anonima");  }  );
