


let validateForm = () =>{
    //create an array of form inputs
    let collection = Array.from(document.forms[0]);
    //create validated bool
    let isValidated = true;

    //loop through all elements in form
    for(let i=0; i< collection.length; i++)
    {
        //ignore fieldset elements
        if(collection[i].tagName != "FIELDSET" && collection[i].tagName != "BUTTON")
        {
            //if the item is not empty continue
            if(collection[i].value != "")
            {
                continue;
                //if the element is empty but is for spouse name and form is set to single continue
            }else if(collection[i].id === "sname" && document.getElementById("mstatus").value === "Single")
            {
                continue;
                //else add error class to empty fields and set isValidated to false
            }else
            {
                
                isValidated = false;
                collection[i].classList.add("error");
            }
        }
    }
    //grab gender radio buttons
    let gender = document.getElementsByName("gender");

    //see if one of them are checked
    if(gender[0].checked == true || gender[1].checked == true)
    {
        //if not throw error
    }else{
        document.getElementById("genderContainer").classList.add("error");
    }
    
    //check to see if passwords match
    if(document.getElementById("password").value === document.getElementById("password2").value)
    {
        //throw error if not
    }else{
        isValidated = false;
        document.getElementById("password").classList.add("error");
        document.getElementById("password2").classList.add("error");
    }
    //if all checks panned out and isValidated is still true submit the form
    return isValidated;
}

//function to grey out spouse name if single
let isSingle = () =>
{
    if(document.getElementById("mstatus").value == "Single")
    {
        document.getElementById("sname").disabled = true;
        document.getElementById("sname").value = null;
    }else{
        document.getElementById("sname").disabled = false;
    }
}


