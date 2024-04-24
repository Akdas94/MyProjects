/*
// Event Lintener                              // click is a event type that it lintense to
document.querySelector("button").addEventListener("click", handleClick);
                                                            here if we use handleChick() than direct pop up will,
                                                            we don't want that
function handleClick()
{
    alert("I got clicked");
}

using above code if we click button I got clicked messeage is pop up

// OR other way:


document.querySelector("button").addEventListener("click", function(){
    alert("I got clicked!");
});

*/

// var numberOfDrumButton = document.querySelectorAll(".drum").length; //total num of buttons

// for(i = 0; i<numberOfDrumButton; i++)
// {
//     document.querySelectorAll(".drum")[i].addEventListener("click",function(){
//         alert("I got clicked");
//     });
// }

// while(i<numberOfDrumButton){
//     document.querySelectorAll(".drum")[i].addEventListener("click",function(){
//         alert("hdsfhkldlvjl");
//         i++;
//     });
// }



// var numberOfDrumButton = document.querySelectorAll(".drum").length; //total num of buttons

// for(i = 0; i<numberOfDrumButton; i++)
// {
//     document.querySelectorAll(".drum")[i].addEventListener("click",function(){
//     //    To add audio
//         var audio = new Audio("./sounds/tom-1.mp3")
//         audio.play();
//     });
// }



// var numberOfDrumButton = document.querySelectorAll(".drum").length; //total num of buttons

// for(i = 0; i<numberOfDrumButton; i++)
// {
//     document.querySelectorAll(".drum")[i].addEventListener("click",function(){
//     // 'this' is a identity of a button which is called
//     // this.style.color = "white";//to change button color to white

        
//     });
// }


var numberOfDrumButton = document.querySelectorAll(".drum").length; //total num of buttons

for(i = 0; i<numberOfDrumButton; i++)
{
    document.querySelectorAll(".drum")[i].addEventListener("click",function(){
    // 'this' is a identity of a button which is called
    // this.style.color = "white";//to change button color to white
    
    var buttonInnerHTML = this.innerHTML;

    switch(buttonInnerHTML){
        case "w":
            var audio = new Audio("./sounds/tom-1.mp3");
            audio.play();
        break;

        case "a":
            var audio = new Audio("./sounds/tom-2.mp3");
            audio.play();
        break;

        case "s":
            var audio = new Audio("./sounds/tom-3.mp3");
            audio.play();
        break;

        case "d":
            var audio = new Audio("./sounds/tom-4.mp3");
            audio.play();
        break;

        case "j":
            var snare = new Audio("./sounds/snare.mp3");
            snare.play();
        break;

        case "k":
            var crash = new Audio("./sounds/crash.mp3");
            crash.play();
        break;

        case "l":
            var kick_bass = new Audio("./sounds/kick-bass.mp3");
            kick_bass.play();
        break;
    }

        makeSound(buttonInnerHTML);
        buttonAnimation(buttonInnerHTML)
    });

    /**
     * Make event happen by just key
   
    document.addEventListener("keypress", function(event){
        console.log(event);
    });

    */

    //for Keys on keyboard:
    document.addEventListener("keypress", function(event){
        makeSound(event.key);

        buttonAnimation(event.key);
    });

    function makeSound(key)
    {
        switch(key){
            case "w":
                var audio = new Audio("./sounds/tom-1.mp3");
                audio.play();
            break;
    
            case "a":
                var audio = new Audio("./sounds/tom-2.mp3");
                audio.play();
            break;
    
            case "s":
                var audio = new Audio("./sounds/tom-3.mp3");
                audio.play();
            break;
    
            case "d":
                var audio = new Audio("./sounds/tom-4.mp3");
                audio.play();
            break;
    
            case "j":
                var snare = new Audio("./sounds/snare.mp3");
                snare.play();
            break;
    
            case "k":
                var crash = new Audio("./sounds/crash.mp3");
                crash.play();
            break;
    
            case "l":
                var kick_bass = new Audio("./sounds/kick-bass.mp3");
                kick_bass.play();
            break;

            default: console.log(buttonInnerHTML)
        }
    }

    function buttonAnimation(currentKey){
        var activeButton = document.querySelector("."+currentKey);

        activeButton.classList.add("pressed");

        setTimeout(function(){
            activeButton.classList.remove("pressed");
        }, '200');
    } 


}