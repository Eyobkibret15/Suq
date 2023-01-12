async function getFilters() {
    var base_url = window.location.origin;
    $.ajax({
        type: 'GET',
        url: base_url + '/product/filters',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function (response) {
            const select_categories = document.getElementsByClassName('filter categories')
            const select_subcategories = document.getElementsByClassName('filter subcategories')
            // const mobile_filter = document.getElementById("mobile-filter")
            // const divs = [sidebar, mobile_filter]
            Object.keys(response).forEach((name) => {
                Object.keys(response[name]).forEach((categories) => {
                    const cate = document.createElement("option");
                    cate.value = categories
                    cate.innerText = categories
                    select_categories[0].append(cate)
                    Object.keys(response[name][categories]).forEach((sub) => {
                        Object.keys(response[name][categories][sub]).forEach((subcategories) => {
                            const subcate = document.createElement("option");
                            console.log(response[name][categories][sub][subcategories])
                            subcate.value = response[name][categories][sub][subcategories]
                            subcate.innerText = response[name][categories][sub][subcategories]
                            subcate.className = categories + ' all'
                            select_subcategories[0].append(subcate)
                        })
                    })
                });
            });
        },
        failure: function (response) {
            alert(response)
        },
        error: function (response) {
            alert(response)
        }
    })
}

getFilters()


async function getProducts() {
    var base_url = window.location.origin;
    $.ajax({
        type: 'GET',
        url: base_url + '/product/',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function (response) {
            const row = document.getElementsByClassName("row")
            Object.keys(response).forEach((name) => {
                const col = document.createElement("div");
                const cate = response[name]['categories']
                const subcate = response[name]['subcategories']
                col.className = 'col-lg-4 col-md-6 col-sm-10 offset-md-0 offset-sm-1 all ' + cate + ' ' + subcate
                const card = document.createElement("div");
                card.className = 'card'
                const img = document.createElement("img");
                img.className = 'card-img-top'
                img.src = "media/" + response[name]['images'][0]
                const card_body = document.createElement("div");
                card_body.className = 'card-body'
                const h5_tag = document.createElement("h5");
                const b_tag = document.createElement("b");
                b_tag.innerText = name
                h5_tag.append(b_tag)
                const d_flex = document.createElement("div");
                d_flex.className = 'd-flex flex-row my-2'
                const price = document.createElement("div");
                price.className = 'text-muted'
                price.innerText = response[name]['price'] + ' zl'
                const ml_auto = document.createElement("div");
                ml_auto.className = 'ml-auto'
                const button1 = document.createElement("button");
                button1.className = 'border rounded bg-white sign'
                const span1 = document.createElement("span");
                span1.className = 'fa fa-plus'
                span1.id = 'orange'
                button1.append(span1)
                const span2 = document.createElement("span");
                span2.className = 'px-sm-1'
                span2.innerText = '  ' + String(response[name]['quantity']) + '  '
                const button2 = document.createElement("button");
                button2.className = 'border rounded bg-white sign'
                const span3 = document.createElement("span");
                span3.className = 'fa fa-minus'
                span3.id = 'orange'
                button2.append(span3)
                ml_auto.append(button1, span2, button2)
                d_flex.append(price, ml_auto)
                const button3 = document.createElement("button");
                button3.className = 'btn w-100 rounded my-2'
                button3.innerText = 'Add to cart'
                card_body.append(h5_tag, d_flex, button3)
                card.append(img, card_body)
                col.append(card)
                row[0].append(col)
            });

        },
        failure: function (response) {
            alert(response)
        },
        error: function (response) {
            alert(response)
        }
    })
}

getProducts();


const select_categories = document.getElementsByClassName('filter categories')
const select_subcategories = document.getElementsByClassName('filter subcategories')


// Attach an event listener to the first <select> element
select_categories[0].addEventListener("change", function () {
    const options = select_subcategories[0].getElementsByTagName("option");
    // Get the selected value of the first <select> element
    var selectedValue = select_categories[0].value;
    const row = document.getElementsByClassName("row")
    // loop through options and hide/show them based on their class
    for (let i = 0; i < options.length; i++) {
        if (!selectedValue) {
            selectedValue = 'all'
        }
        if (options[i].classList.contains(selectedValue)) {
            options[i].style.display = "block";
        } else {
            options[i].style.display = "none";
        }
    }
    let divs = row[0].children
    for (let i = 0; i < divs.length; i++) {
        if (!selectedValue) {
            selectedValue = 'all'
        }
        if (divs[i].classList.contains(selectedValue)) {
            divs[i].style.display = "block";
        } else {
            divs[i].style.display = "none";
        }
    }
});

select_subcategories[0].addEventListener("change", function () {
    const row = document.getElementsByClassName("row")
    var selectedValue = select_subcategories[0].value;
    let divs = row[0].children
    for (let i = 0; i < divs.length; i++) {
        if (!selectedValue) {
            selectedValue = 'all'
        }
        if (divs[i].classList.contains(selectedValue)) {
            divs[i].style.display = "block";
        } else {
            divs[i].style.display = "none";
        }
    }
})