var length = prompt("how many numbers of a fibbinachi sequence do you want?");
var fibSequence =[];
fibSequence[0] = 0;
fibSequence[1] = 1;
const GOLDENRATIO = 1.618034;



if(length > 3)
{
    for(var i=2; i < length; i++)
    {
        fibSequence[i] = (fibSequence[i-2] + fibSequence[i-1]);   
    }

    for(var x=0; x < fibSequence.length; x++)
    {
        document.write("<div class='numberBox'>");
        document.write(`${x + 1}: ${fibSequence[x]}`);
        document.write("</div>");
    }

    var lastTwoRatio = fibSequence[fibSequence.length - 1] / fibSequence[fibSequence.length - 2];

    document.write("<div class='resultsBox'>");
    document.write(`the ratio of the last two compared to the golden ratio${lastTwoRatio}, Golden Ratio: ${GOLDENRATIO}`);
    document.write("</div>");
}