function showArr(arr){
    var arrStr= "";
    for(var i=0; i< arr.length; i++)
    {
        arrStr += arr[i] + " <br />";
    }
    document.getElementById("arrayOutput").innerHTML = arrStr;
}

function deleteItem()
{
    var itemToDelete = document.getElementById("itemToDelete").value;

    for(var i=0; i < names.length; i++)
    {
        if(names[i] === itemToDelete)
        {
            names.splice(i,1);
            console.log(names);
            showArr(names);
            return;
        }
    }
    alert("Item does not exist in current array");
}

function addItem() 
{
    var itemToAdd = document.getElementById("itemToAdd").value;
    names.push(itemToAdd);
    showArr(names);
}

function sortArray()
{
    names.sort();
    showArr(names);
}
    var names = [];

    showArr(names);


    