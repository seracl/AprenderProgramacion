var obje = {};
function retObj(k, v) {
	
	if (obje === null) {
		obje[k] = v;
	} else {
		var nuevo = { k : v };
		obje = {...obje, ...nuevo};
	}
	console.log(obje);
	return obje;
}

retObj("mono", "baba");
retObj("moa", "baba");
retObj("moano", "baba");
retObj("moana", "baba");
