// JavaScript source code

//Arrays used in next sequence.
var buttonColours = ["red", "blue", "green", "yellow"];

var gamePattern = [];
var userClickedPattern = [];

$(document).ready(function () {

    //Elements creator
    function createElement(target1, action, target2) {
        $(target1)[action](target2);
    }

    //Creating the title element
    createElement("<h1>Press A Key to Start</h1>", "appendTo", "body");
    $("h1").attr("id", "level-title");

    //Creating the squares container
    createElement('<div class="container"></div>', "appendTo", "body");

    //Creating the first row
    createElement('<div class="row row1"></div>', "appendTo", ".container");
    createElement('<div type="button" id="green" class="btn green"></div>', "appendTo", ".row1");
    createElement('<div type="button" id="red" class="btn red"></div>', "appendTo", ".row1");

    //Creating the second row
    createElement('<div class="row row2"></div>', "appendTo", ".container");
    createElement('<div type="button" id="yellow" class="btn yellow">', "appendTo", ".row2");
    createElement('<div type="button" id="blue" class="btn blue">', "appendTo", ".row2");

    ////Check pressed buttons
    //$(".btn").click(function () {

    //  //Variable to store the id of the button that got clicked.
    //    var userChosenColour = $(this).attr("id");

    //    //Add userChosenColour to the end of this new userClickedPattern
    //    userClickedPattern.push(userChosenColour);
    //    console.log(userClickedPattern);

    //    //Animate
    //    nextSequence();
    //});

    //Creating a pattern
    function nextSequence() {
        //Random number between 0 and 3, stored in a variable
        var randomNumber = Math.floor(Math.random() * 4);
        //console.log("This: " + randomNumber);

        //Select one of the colors from buttonColours using the randomNumber for the position.
        var randomChosenColour = buttonColours[randomNumber];
        //console.log("This: " + randomChosenColour);

        //Add the new randomChosenColour to the end gamePattern.
        gamePattern.push(randomChosenColour);

        //Select the button with the same id as the randomChosenColour
        $("#" + randomChosenColour).fadeIn(100).fadeOut(100).fadeIn(100);
        //console.log("This: " , $("#" + randomChosenColour));

        //Animate
        playSound(randomChosenColour);
        //animatePress(randomChosenColour);
    }

    //Check pressed buttons
    $(".btn").click(function () {

        //Variable to store the id of the button that got clicked.
        var userChosenColour = $(this).attr("id");
        //console.log(userChosenColour);

        //Add userChosenColour to the end of this new userClickedPattern
        userClickedPattern.push(userChosenColour);
        //console.log(userClickedPattern);

        //Animate
        nextSequence();
    });

    //Add sound to clicks
    function playSound(name) {
        //Play sound
        var audio = new Audio("sounds/" + name + ".mp3");
        audio.play();
    }

    //Box animation
    function animatePress(currentColor) {
        //Add animation class
        $("#" + currentColor).addClass("pressed");
        //Remove animation
        setTimeout(function () {
            $("#" + currentColor).removeClass("pressed");
        }, 100);
    }

    //Check Which Button is Pressed
    $("btn").on("click", function () {

        //$("a").css("color", "yellow");
        console.log(this);
    });

});
