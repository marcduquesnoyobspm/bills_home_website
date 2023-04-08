const entrepriseSelect = document.getElementById("entreprise");
const firstForm = document.getElementById("first-form"); 
const secondForm = document.getElementById("second-form"); 
const finalForm = document.getElementById("final-form"); 

function categorySelected() {
    "use strict";
    let form = document.querySelector("form");
    let formData = new FormData(form);
    
    fetch(load_entreprises_by_category_url, {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
        if (data.success) {
            removeAll(entrepriseSelect)
            let entreprisesList = data.entreprises;
            let newOption = new Option("");
            entrepriseSelect.add(newOption,undefined);
            for (const entreprise of entreprisesList) {
                let newOption = new Option(entreprise);
                entrepriseSelect.add(newOption,undefined);
            };
            firstForm.style.display = "block";
            secondForm.style.display = "block";
            finalForm.style.display = "none";
        }
    });
};

function entrepriseSelected(){
    firstForm.style.display = "block";
    secondForm.style.display = "block";
    finalForm.style.display = "block";
}

function removeAll(selectBox) {
    while (selectBox.options.length > 0) {
        selectBox.remove(0);
    }
}

function resetForm(form){
    let children = form.querySelectorAll("input");

    for (child of children) {
        child.value = ""
    }
}
