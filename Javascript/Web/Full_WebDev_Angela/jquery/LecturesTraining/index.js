
//jQuery() or $ are the same


//Look if the document is loaded and then execute code
//This is the same as placing the HTML script tags in the body.
//Use it when the HTML script tags are placed in the head of the document
//Then all the code goes inside this function
//Can be also done in javascript by changing $ for document.blablabla
//$(document).ready(function () {
//    //Access h1 and change color
//    //$("h1").css("color", "red");

//})

/*JQ works basically with methods*/

//change style
$("h1").addClass("big-title margin-50");
//Setting a timeout so we can see what has happened
setTimeout(function () {
    $("h1").removeClass("big-title margin-50");
}, 500);

//Manipulating text
$("h1").text("Good bye!"); //All the elements that fit this criteria
$("button").html("<em>Hey</em>");
//$("button").text("<em>Hey</em>"); //Different than the previous

//Manipulating attributes
console.log($("img").attr("src")); //Getting the value
$("a").attr("href", "https://www.yahoo.com"); //Getting the value

//Add event listener
$("button").click(function() {
    $("h1").css("color", "purple");
});
$("input").keypress(function(e) {
    var palabra = "";
    palabra.concat(e.key);
    $("h1").text(palabra);
    console.log("Key: ", e.key);
    console.log("Palabra: ", palabra);
});

$("a").on("mouseover", function() {
    $("a").css("color", "yellow");
});

//Adding and removing elements
$("h1").before("<button>Before!</button>");
$("h1").after("<button>After!</button>");
$("h1").prepend("<button>Prepend!</button>");
$("h1").append("<button>Append!</button>");
$("h1").remove("<button>Before!</button>");
