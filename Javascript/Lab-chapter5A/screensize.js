let screenWidth = window.innerWidth;
let screenHeight = window.innerHeight;

document.getElementById("screenWidth").innerText = screenWidth;
document.getElementById("screenHeight").innerText = screenHeight;


window.onresize = () => {
     screenWidth = window.innerWidth;
     screenHeight = window.innerHeight;

    document.getElementById("screenWidth").innerText = screenWidth;
    document.getElementById("screenHeight").innerText = screenHeight;
}