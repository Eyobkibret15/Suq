
 const passwordField = document.getElementById("password");
  const passwordToggle = document.getElementById("passwordToggle");

  // Add event listener to the toggle button
  passwordToggle.addEventListener("click", function() {
    // Toggle the visibility of the password field
    if (passwordField.type === "password") {
      passwordField.type = "text";
      passwordToggle.innerHTML = '<i class="fa fa-eye-slash"></i>';
    } else {
      passwordField.type = "password";
      passwordToggle.innerHTML = '<i class="fa fa-eye"></i>';
    }
  });

  // Get the password confirmation field and toggle button elements
  const passwordConfirmationField = document.getElementById("passwordConfirmation");
  const passwordConfirmationToggle = document.getElementById("passwordConfirmationToggle");

  // Add event listener to the toggle button
  passwordConfirmationToggle.addEventListener("click", function() {
    // Toggle the visibility of the password confirmation field
    if (passwordConfirmationField.type === "password") {
      passwordConfirmationField.type = "text";
      passwordConfirmationToggle.innerHTML = '<i class="fa fa-eye-slash"></i>';
    } else {
      passwordConfirmationField.type = "password";
      passwordConfirmationToggle.innerHTML = '<i class="fa fa-eye"></i>';
    }
  });

  // Get the password fields and form element
passwordConfirmationField.addEventListener("input", function() {
  if (passwordField.value !== passwordConfirmationField.value) {
    passwordConfirmationField.setCustomValidity("Passwords do not match.");
  } else {
    passwordConfirmationField.setCustomValidity("");
  }
});
function chnageinputgroup() {
     $('input, select').on('focus', function () {
        $(this).parent().find('.input-group-text').css('border-color', '#80bdff');
    });
    $('input, select').on('blur', function () {
        $(this).parent().find('.input-group-text').css('border-color', '#ced4da');
    });
}

function login() {
    var base_url = window.location.origin;
    $.ajax({
        type: 'GET',
        url: base_url + '/login/',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function (response) {
            const sidebar = document.getElementById("sidebar")
            const mobile_filter = document.getElementById("mobile-filter")
            const divs = [sidebar, mobile_filter]
            divs.forEach((div) => {
                response.name.forEach((element) => {
                    const bars = document.createElement("div");
                    bars.className = 'py-2  ml-3'
                    const categories = document.createElement("h6");
                    categories.className = "font-weight-bold"
                    categories.innerText = element
                    bars.append(categories)
                    div.append(bars)
                });
            })

        },
        failure: function (response) {
            alert(response)
        },
        error: function (response) {
            alert(response)
        }
    })
}

function register() {
    var base_url = window.location.origin;
    $.ajax({
        type: 'GET',
        url: base_url + '/user/register/',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function (response){

        },
        failure: function (response) {
            alert(response)
        },
        error: function (response) {
            alert(response)
        }
    })
}

chnageinputgroup()

