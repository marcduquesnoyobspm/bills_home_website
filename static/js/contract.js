const entrepriseSelect = document.getElementById("entreprise");
const firstForm = document.getElementById("first-form"); 
const secondForm = document.getElementById("second-form"); 
const finalForm = document.getElementById("final-form"); 

var categoryAlreadySelected = false;
var entrepriseAlreadySelected = false;

function categorySelected() {
    "use strict";
    let form = document.querySelector("form");
    let formData = new FormData(form);
    let category = document.getElementById("category").value
    
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
            if (category.match(/^(Electricité|Gaz|Internet)$/)){
                document.getElementById("entreprises-label").innerText = "Fournisseur";
            } else if (category.match(/^(Assurance Auto|Assurance Habitation|Assurance Animaux)$/)){
                document.getElementById("entreprises-label").innerText = "Compagnie d'assurance";
            } else if (category == "Téléphone"){
                document.getElementById("entreprises-label").innerText = "Opérateur";
            }
            firstForm.style.display = "block";
            secondForm.style.display = "block";
            finalForm.style.display = "none";

            if (!categoryAlreadySelected){
                document.getElementById("category").remove(0);
                categoryAlreadySelected = true;
            };
            
            entrepriseAlreadySelected = false;
        }
    });
};

function entrepriseSelected(){
    firstForm.style.display = "block";
    secondForm.style.display = "block";
    finalForm.style.display = "block";

    if (!entrepriseAlreadySelected){
        entrepriseSelect.remove(0);
        entrepriseAlreadySelected = true;
    };
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
