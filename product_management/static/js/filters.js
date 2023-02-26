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
                const link = document.createElement('a')
                link.className = 'productlink'
                link.id = name
                link.setAttribute("onclick", "ProductCardClicked(event)");
                const col = document.createElement("div");
                const cate = response[name]['categories']
                const subcate = response[name]['subcategories']
                col.className = 'col-lg-4 col-md-6 col-sm-10 offset-md-0 offset-sm-1 all ' + cate + ' ' + subcate + ' ' + response[name]['price']
                col.id = 'true,true,true,true'
                const card = document.createElement("div");
                card.className = 'card'
                const img = document.createElement("img");
                img.className = 'card-img-top'
                img.src = "media/" + response[name]['images'][0]
                img.id = response[name]['id']
                const card_body = document.createElement("div");
                card_body.className = 'card-body'
                const h5_tag = document.createElement("h5");
                const b_tag = document.createElement("b");
                const rating = document.createElement("b");
                b_tag.innerText = name
                b_tag.id = name
                rating.className = 'rating'
                rating.innerText = response[name]['rating']
                rating.style.display = 'none'
                h5_tag.append(b_tag)
                h5_tag.append(rating)
                const popularity = document.createElement("b");
                popularity.className = 'popularity'
                popularity.innerText = response[name]['popularity']
                popularity.style.display = 'none'
                h5_tag.append(popularity)
                const d_flex = document.createElement("div");
                d_flex.className = 'd-flex flex-row my-2'
                const price = document.createElement("div");
                price.className = 'text-muted'
                price.id = 'price'
                price.price = response[name]['price']
                price.innerText = response[name]['price'] + ' zl'
                const ml_auto = document.createElement("div");
                ml_auto.className = 'ml-auto'
                const button1 = document.createElement("button");
                button1.className = 'border rounded bg-white sign'
                // const span1 = document.createElement("span");
                // span1.className = 'fa fa-plus'
                // span1.id = 'orange'
                // button1.append(span1)
                // const span2 = document.createElement("span");
                // span2.className = 'px-sm-1'
                // span2.innerText = '  ' + String(response[name]['quantity']) + '  '
                // const button2 = document.createElement("button");
                // button2.className = 'border rounded bg-white sign'
                // const span3 = document.createElement("span");
                // span3.className = 'fa fa-minus'
                // span3.id = 'orange'
                // button2.append(span3)
                // ml_auto.append(button1,button2)
                d_flex.append(price)
                // const button3 = document.createElement("button");
                // button3.className = 'btn w-100 rounded my-2'
                // button3.innerText = 'Add to cart'
                card_body.append(h5_tag, d_flex)
                card.append(img, card_body)
                link.append(card)
                col.append(link)
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
const select_sort = document.getElementById('sort')

function FilterProdUct() {
    const row = document.getElementsByClassName("row")
    let divs = row[0].children
    for (let i = 0; i < divs.length; i++) {
        id = divs[i].id.split(',')
        if (id.every((elem) => elem === 'true')){
            divs[i].style.display = "block";
        }
        else {
            divs[i].style.display = "none";
        }

    }
        // if (!selectedValue) {
        //     selectedValue = 'all'
        // }
        // if (divs[i].classList.contains(selectedValue)) {
        //     divs[i].style.display = "block";
        // } else {
        //     divs[i].style.display = "none";
        // }
}

function PriceSort() {
    const row = document.getElementsByClassName("row")

    let divs = row[0].children
    let prices = [];

// Extract prices from innerHTML of each div and store in prices array
    for (let i = 0; i < divs.length; i++) {
        let price = divs[i].getElementsByClassName('text-muted')[0].innerHTML.slice(0, -3)
        prices.push(parseFloat(price));
    }

// Sort prices array
    prices.sort(function (a, b) {
        return a - b;
    });

// Reorder divs based on sorted prices array
    for (let i = 0; i < divs.length; i++) {
        let price = divs[i].getElementsByClassName('text-muted')[0].innerHTML.slice(0, -3)
        divs[i].style.order = prices.indexOf(parseFloat(price))
    }
}

function RatingSort() {
    const row = document.getElementsByClassName("row")

    let divs = row[0].children
    let ratings = [];
    for (let i = 0; i < divs.length; i++) {
        let rating = divs[i].getElementsByClassName('rating')[0].innerHTML
        ratings.push(parseFloat(rating));
    }

// Sort prices array
    ratings.sort(function (a, b) {
        return b - a;
    });

// Reorder divs based on sorted prices array
    for (let i = 0; i < divs.length; i++) {
        let rating = divs[i].getElementsByClassName('rating')[0].innerHTML
        divs[i].style.order = ratings.indexOf(parseFloat(rating))
    }
}

function PopularitySort() {
    const row = document.getElementsByClassName("row")

    let divs = row[0].children
    let populars = [];
    for (let i = 0; i < divs.length; i++) {
        let popular = divs[i].getElementsByClassName('popularity')[0].innerHTML
        populars.push(parseFloat(popular));
    }

// Sort prices arra
    populars.sort(function (a, b) {
        return a - b;
    });

// Reorder divs based on sorted prices array
    for (let i = 0; i < divs.length; i++) {
        let popular = divs[i].getElementsByClassName('popularity')[0].innerHTML
        divs[i].style.order = populars.indexOf(parseFloat(popular))
    }
}

// Attach an event listener to the first <select> element
select_categories[0].addEventListener("change", function () {
    const options = select_subcategories[0].getElementsByTagName("option");
    // Get the selected value of the first <select> element
    var selectedValue = select_categories[0].value;

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
    const row = document.getElementsByClassName("row")
    let divs = row[0].children
    for (let i = 0; i < divs.length; i++) {
        id = divs[i].id.split(',')
        if (!selectedValue) {
            selectedValue = 'all'
        }
        if (divs[i].classList.contains(selectedValue)) {
            id[0] = 'true'
            id[1] = 'true'
        } else {
            id[0] = 'false'
            id[1] = 'false'
        }
        divs[i].id = id[0] +',' +  id[1] + ',' +  id[2] + ',' + id[3]

    }
    FilterProdUct()
});

select_subcategories[0].addEventListener("change", function () {
    var selectedValue = select_subcategories[0].value;
    const row = document.getElementsByClassName("row")
    let divs = row[0].children
     if (!selectedValue) {
            selectedValue = 'all'
        }
    for (let i = 0; i < divs.length; i++) {
        id = divs[i].id.split(',')
        console.log(divs[i].classList)
        if (divs[i].classList.contains(selectedValue)) {
            id[1] = 'true'
        } else {
            id[1] = 'false'
        }
        divs[i].id = id[0] +',' +  id[1] + ',' +  id[2] + ',' + id[3]
    }
    FilterProdUct()
})

select_sort.addEventListener('change', function () {
    const sortType = select_sort.value
    if (sortType === 'price') {
        PriceSort();
    } else if (sortType === 'rating') {
        RatingSort();
    } else if (sortType === 'popularity') {
        PopularitySort();
    }
})


const filterInputs = document.querySelectorAll('.filter');
const priceRadioInputs = document.querySelectorAll('input[name="price-f"]');
const fromInput = document.querySelector('.from');
const downInput = document.querySelector('.down');

// Attach an event listener to each input
filterInputs.forEach(function (input) {
    input.addEventListener('change', function () {
        let checkedValue = null;
        let fromValue = null;
        let downValue = null;

        // Check which filter option the user selected
        priceRadioInputs.forEach(function (radioInput) {
            if (radioInput.checked) {
                checkedValue = radioInput.value;
            }
        });

        // Check if the text input fields have a value
        if (fromInput.value.trim() !== '' && !isNaN(fromInput.value)) {
            fromValue = parseFloat(fromInput.value);
        }

        if (downInput.value.trim() !== '' && !isNaN(downInput.value)) {
            downValue = parseFloat(downInput.value);
        }

        console.log('Checked value:', checkedValue);
        // Clear the text input fields when the radio buttons are clicked
        priceRadioInputs.forEach(function (radioInput) {
            radioInput.addEventListener('click', function () {
                fromInput.value = '';
                downInput.value = '';
            });
        });

        // Uncheck the radio buttons when the text input fields are updated
        fromInput.addEventListener('input', function () {
            priceRadioInputs.forEach(function (radioInput) {
                radioInput.checked = false;
            });
        });

        downInput.addEventListener('input', function () {
            priceRadioInputs.forEach(function (radioInput) {
                radioInput.checked = false;
            });
        });

        // Update the fromValue and downValue if checkedValue has a '-' separator
        if (checkedValue && checkedValue.includes('-')) {
            const values = checkedValue.split('-');
            if (!isNaN(values[0])) {
                fromValue = parseFloat(values[0]);
            }
            if (!isNaN(values[1])) {
                downValue = parseFloat(values[1]);
            }
        }

        // Update the UI based on the selected values
        const row = document.getElementsByClassName("row")
        let divs = row[0].children
        if (!fromValue) {
            fromValue = 0
        }
        if (!downValue) {
            downValue = Infinity
        }
        console.log('From value:', fromValue);
        console.log('Down value:', downValue);
        for (let i = 0; i < divs.length; i++) {
            let priceElement = divs[i].querySelector('#price');
            priceTxt = priceElement.innerHTML
            let extracted = priceTxt.split(" ")[0]; // extract text until space

            if (!isNaN(extracted)) {
                extracted = Number(extracted); // convert to number if it is a number
            }
            console.log("extracted",extracted)
            console.log('a', extracted >= fromValue)
            console.log('l', extracted <= downValue)
            if (extracted && !isNaN(extracted)){
                id = divs[i].id.split(',')
                if (extracted >= fromValue && extracted <=downValue){
                   id[2] = 'true'
                }
                else {
                    id[2] = 'false'
                }
                 console.log(id)
                 divs[i].id = id[0] +',' +  id[1] + ',' +  id[2] + ',' + id[3]
                 console.log(divs[i].id)

            }

        }
        //
        FilterProdUct()
    });
});

