var mens_contracts = document.getElementsByClassName("mens");

window.onload = toggleNav(tab);
window.onload = toggleForm("off");
window.onload = displayTwoDigits();

function toggleNav(tab) {
  document.getElementById("overview_div").style.display = "none";
  document.getElementById("contracts_div").style.display = "none";
  document.getElementById(tab + "_div").style.display = "block";
}

function navigateInOverviewTabs(event) {
  event.preventDefault();
  let tab = event.target;
  test_url = tab.getAttribute("href");
  window.history.pushState(null, "", test_url);
  toggleNav(tab.id);
}

function refreshUserData(first_name, last_name) {
  document.getElementById("first_name").value = first_name;
  document.getElementById("last_name").value = last_name;
  document.getElementById("user_name").innerHTML =
    "<p>" + first_name + " " + last_name + "</p>";
}

function toggleForm(state) {
  if (state == "on") {
    document.getElementById("profile_form_div").style.display = "block";
    document.getElementById("user_infos").style.display = "none";
  } else {
    document.getElementById("profile_form_div").style.display = "none";
    document.getElementById("user_infos").style.display = "block";
  }
}

function submitOverviewUpdateProfileForm(event) {
  event.preventDefault();
  let form = document.getElementById("profile_form");
  let formData = new FormData(form);
  let csrf_token = document.getElementById("csrf_token").value;
  formData.append("csrf_token", csrf_token);

  fetch(form_url, {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        toggleForm("off");
      } else {
        toggleForm("on");
      }
      refreshUserData(data.first_name, data.last_name);
    });
}

function displayTwoDigits() {
  for (mens of mens_contracts) {
    let value = mens.innerHTML;
    var second_numbers_regex = /^\d+[\.\,]+\d{2}$/;

    if (!second_numbers_regex.test(value)) {
      mens.innerHTML = parseFloat(value).toFixed(2) + "<span>€</span>";
    }
  }
}
