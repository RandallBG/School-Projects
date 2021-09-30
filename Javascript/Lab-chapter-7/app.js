
window.onload = () =>{
    document.getElementById("findPrimes").addEventListener('click', findPrimes);
}


let IsPrime = (num) =>{
    
    
    for(let i=2; i < num; i++)
    {
        if(num % i == 0)
        {
            return false
        }
    }
    return true;
}

let findPrimes = () =>{

document.getElementById("primeDisplay").innerHTML = "";

if(document.getElementById("maxPrime").value === null)
{
    alert("You must enter a number!");
}else if(document.getElementById("maxPrime") == 1)
{
    alert("1 is not a valid number to use when finding all primes");
}else{
        let maxPrime = parseInt(document.getElementById("maxPrime").value);

        for(let i=3; i <= maxPrime; i+=2)
        {
            if(IsPrime(i))
            {
                document.getElementById("primeDisplay").innerHTML += `<p>${i}</p>`;
            }
        }
    }   
}


