
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

