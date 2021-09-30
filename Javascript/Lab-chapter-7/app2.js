window.onload = () =>{
    document.getElementById("findPrimes").addEventListener('click', findPrimes);
}

let findPrimes = () =>{
    let maxPrimes = document.getElementById("maxPrime").value;
    isPrime = true;
    document.getElementById("primeDisplay").innerHTML = "";

    for(let i=3; i < maxPrimes; i+=2)
    {
        for(let j=3; j < Math.sqrt(i); j++)
        {
            if(i%j == 0)
            {
                isPrime = false;
                break;
            }
        }
        if(isPrime)
        {
            document.getElementById("primeDisplay").innerHTML += `<p>${i}</p>`;
        }else
        {
            isPrime = true;
        }
    }
}