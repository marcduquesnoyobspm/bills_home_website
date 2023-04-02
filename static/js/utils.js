var value = document.getElementById("mens").value;

window.onload = displayTwoDigits();

function displayTwoDigits() {
  if (value != ""){

    var second_numbers_regex = /^\d+[\.\,]+\d{2}$/;

    if (!second_numbers_regex.test(value)) {
        document.getElementById("mens").value = parseFloat(value).toFixed(2);
    }
  }
}
  
function testDecimalNumber() {
  let new_value = document.getElementById("mens").value;
  console.log(value, new_value);
  // var regexpression = /^\d+[\.\,]?\d{1,2}$/;
  var first_numbers_regex = /^\d+$/;
  var dot_regex = /^\d+[\.\,]$/;
  var second_numbers_regex = /^\d+[\.\,]+\d{1,2}$/;

  if (!second_numbers_regex.test(new_value)){

    if (!dot_regex.test(new_value)){

      if (!first_numbers_regex.test(new_value)){

        if (new_value == ""){
          document.getElementById("mens").value = new_value;
          value = new_value;

        } else {
          document.getElementById("mens").value = value;
        }

      } else  {
        document.getElementById("mens").value = new_value;
        value = new_value;
      }

    } else {
      document.getElementById("mens").value = new_value;
      value = new_value;
    }

  } else {
    document.getElementById("mens").value = new_value;
    value = new_value;
  }

};
