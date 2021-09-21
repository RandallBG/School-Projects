"use strict";
var counter =0;
var userInput;

var randomNum = Math.trunc(Math.random() *(100 - 1) + 1);

while(userInput != -999)
{
userInput = parseInt(prompt("guess a number between 1 and 100"));

if(userInput > 0 && userInput <= 100)
{
    counter++;

    if(counter == 1)
    {
        min = userInput;
        max= userInput;

    }else{
        if(userInput < min)
        {
            min = userInput;
        } 
        if(userInput > max)
        {
            max = userInput;
        }
    }

    

}
    document.write(`You guessed ${userInput} 
    Max value guessed: ${max}
    Min value guessed: ${min}`);
    document.write("</br>");
    
    if(userInput === randomNum)
    {
        alert(`Yay you got it in ${counter} tries`);
        break;
    }
    if(userInput > randomNum)
    {
        document.write("The number is lower");
        document.write("</br>");
    }
    if(userInput < randomNum)
    {
        document.write("The number is higher");
        document.write("</br>");
    }
}