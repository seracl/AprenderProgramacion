// JavaScript source code

//Dice 1
var randomNumberD1 = Math.floor(Math.random() * 6) + 1; //Generate random dice number
var diceImage1 = "dice" + randomNumberD1 + ".png"; //Get specific dice
var diceSource1 = "images/" + diceImage1;

var image1 = document.querySelectorAll("img")[0];
image1.setAttribute("src", diceSource1);

//Dice 2
var randomNumberD2 = Math.floor(Math.random() * 6) + 1; //Generate random dice number
var diceImage2 = "dice" + randomNumberD2 + ".png"; //Get specific dice
var diceSource2 = "images/" + diceImage2;
var image2 = document.querySelectorAll("img")[1];
image2.setAttribute("src", diceSource2);

if (randomNumberD1 > randomNumberD2) {
    document.querySelector("h1").textContent = "P1 Wins!!!";
} else if (randomNumberD1 < randomNumberD2) {
    document.querySelector("h1").textContent = "P2 Wins!!!";
} else {
    document.querySelector("h1").textContent = "It is Tie!!!"
}