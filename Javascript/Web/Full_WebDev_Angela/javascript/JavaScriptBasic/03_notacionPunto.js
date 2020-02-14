

var persona = {
    nombre: 'Juana',
    apellido: 'Herrera',
    edad: 25,
    direccion: {
        pais: 'Costa Rica',
        ciudad: 'San Jose',
        edificio: {
            nombre: 'Edificio Principal',
            telefono: '2222-3333',
        }
    }
    
};


console.log( persona.nombre); //persona.nombre es notacion por punto
var callNombre = persona.nombre
console.log( callNombre );

// Cuando hay objetos dentro de objetos
console.log( persona.direccion.pais );
console.log( persona.direccion.ciudad );

// Cambiar el objetos usando notacion
persona.direccion.zipcode = 1101;
console.log( persona.direccion.zipcode );


console.log( persona.direccion.edificio.nombre ); // 0

var edificio = persona.direccion.edificio.nombre // ambos funcionan
console.log( edificio );

// agregar caracteristicas a objetos extensos
// Referencia a un objeto anterios
var edificio = persona.direccion.edificio 
edificio.nopiso = '8vo piso'; 
console.log( persona.direccion.edificio );


// Notacion de corchete [usa var = persona como referencia]
// si me equivoco aca retorna undefined. la notacion de punto tambien lo hace

var campo = ' edad '; 

console.log( persona['direccion']['pais'] );
console.log( persona['edad'] );










