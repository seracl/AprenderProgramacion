
//Length of buttons
var drumButtonsLength = document.querySelectorAll(".drum").length;

//Buttons extensions
var soundExtension = {
    q: "tom-1.mp3",
    w: "tom-2.mp3",
    e: "tom-3.mp3",
    r: "tom-4.mp3",
    t: "snare.mp3",
    y: "crash.mp3",
    u: "kick-bass.mp3"  
}

//Buttons captured on click
for (var i = 0; i < drumButtonsLength; i++) {
    document.querySelectorAll(".drum")[i].addEventListener("click", function () {
        makeSound(this.innerHTML);
        buttonAnimation(this.innerHTML);
    })
}

//Buttons captured by keyboard press
document.addEventListener("keypress", function (e) {
    makeSound(e.key);
    buttonAnimation(e.key);
});

//Attach sound to events
function makeSound(key) {
    var soundFolder1 = "sounds/" + soundExtension[key];
    var audio1 = new Audio(soundFolder1);
    audio1.play();
}

//Attach animation to both events
function buttonAnimation(currentKey) {
    //Select what is to be animated
    var activeButton = document.querySelector("." + currentKey + ".drum");
    
    //Add animation after clicking
    activeButton.classList.add("pressed");
    activeButton.setAttribute('style', 'color: white');

    //Remove the class after 3 seconds
    setTimeout(function () {
        activeButton.classList.remove("pressed");
        activeButton.removeAttribute('style', 'color: white');
    }, 500)
}