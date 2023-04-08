function toggleForm(id){
    form = document.getElementById(id);
    if (form.style.display == "block"){
        form.style.display = "none"
    } else {
        form.style.display = "block"
    }
};

function loadImageInput(){
    document.getElementById("image").click();
}

function send_infos_form_data(event){
    event.preventDefault();
    let form = document.getElementById("changeInfosForm");
    let formData = new FormData(form);

    fetch(update_infos_url, {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
        if (data.success) {
            first_name = data.first_name
            last_name = data.last_name
            document.getElementById("first_name").value = first_name;
            document.getElementById("last_name").value = last_name;
            document.getElementById("user_name").innerHTML = first_name + " " + last_name;
            toggleForm("changeInfosFormDiv");
        }
    });
}

function send_image_form_data(event){
    event.preventDefault();
    let form = document.getElementById("changeImageForm");
    let formData = new FormData(form);

    fetch(update_image_url, {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
        if (data.success) {
            document.getElementById("profile_pic").src= data.profile_picture + '?' + Date.now();
        }
    });
}

function send_identifiant_form_data(event){
    event.preventDefault();
    let form = document.getElementById("changeIdentifiantForm");
    let formData = new FormData(form);

    fetch(update_identifiant_url, {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
        if (data.success) {
            document.getElementById("user_identifiant").innerHTML = data.identifiant;
            toggleForm("changeIdentifiantFormDiv");
        }
    });
}

function send_email_form_data(event){
    event.preventDefault();
    let form = document.getElementById("changeEmailForm");
    let formData = new FormData(form);

    fetch(update_email_url, {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
        if (data.success) {
            document.getElementById("user_email").innerHTML = data.email;
            toggleForm("changeEmailFormDiv");
        }
    });
}

function send_password_form_data(event){
    event.preventDefault();
    let form = document.getElementById("changePasswordForm");
    let formData = new FormData(form);
    
    fetch(update_password_url, {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
        if (data.success) {
            toggleForm("changePasswordFormDiv");
        }
    });
}