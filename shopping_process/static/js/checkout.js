async function getCart() {
    var base_url = window.location.origin;
    console.log(base_url)
    $.ajax({
        type: 'GET',
        url: base_url + '/get-cart/',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function (response) {
            const cart = document.getElementsByClassName("container summery");
            let total_cost = 0;
            Object.keys(response).forEach((name) => {
                if (!['quantity', 'cost'].includes(name)){
                const p = document.createElement('p')
                const link = document.createElement('a')
                link.className = 'products'
                link.id = name
                link.setAttribute("onclick", "ProductCardClicked(event)");
                link.innerHTML = name;
                p.append(link)
                const span = document.createElement('span');
                span.className = 'quantity'
                const butt1 = document.createElement('button');
                butt1.className = "minus-btn";
                butt1.type = "button";
                butt1.name = "button";
                butt1.setAttribute("onclick", "decreaseQuantity(event)");
                const i1 = document.createElement('i');
                i1.className = "fa fa-minus";
                butt1.append(i1);
                span.append(butt1);
                const inp = document.createElement('input');
                inp.className = "input-text price_quantity";
                inp.type = 'number';
                inp.id = "price_quantity";
                inp.name = 'name';
                inp.value = response[name]['quantity'];
                span.append(inp);
                const butt2 = document.createElement('button');
                butt2.className = "plus-btn";
                butt2.type = "button";
                butt2.name = "button";
                butt2.setAttribute("onclick", "increaseQuantity(event)");
                const i2 = document.createElement('i');
                i2.className = "fa fa-plus";
                butt2.append(i2);
                span.append(butt2);
                p.append(span);
                const span2 = document.createElement('span');
                span2.className = 'price';
                span2.id = 'price';
                span2.title = response[name]['cost'];
                const cost =  response[name]['quantity'] * response[name]['cost'];
                total_cost =total_cost + cost;
                span2.innerHTML = cost + ' PLN';
                p.append(span2);
                const butt3 = document.createElement('button');
                butt3.className = "remove-btn";
                butt3.type = "button";
                butt3.name = "button";
                butt3.setAttribute("onclick", "removeItem(event)");
                butt3.innerHTML = 'Remove';
                p.append(butt3);
                cart[0].append(p)
            }});
            const p_f = document.createElement('p')
            const b_1 = document.createElement('b');
            b_1.innerHTML = 'Total'
            p_f.append(b_1)
            const span_2 = document.createElement('span')
            span_2.className = "price"
            span_2.style = "color:black"
            const b_2 = document.createElement('b')
            b_2.innerHTML = response['cost'] + ' PLN'
            b_2.title = response['cost'];
            b_2.id = 'total_price';
            span_2.append(b_2)
            p_f.append(span_2)
            cart[0].append(p_f)
        },
        failure: function (response) {
            alert(response)
        },
        error: function (response) {
            alert(response)
        }
    })
}

getCart();

// Get all the plus and minus buttons
// let plusButtons = document.querySelectorAll('.plus-btn');
// let minusButtons = document.querySelectorAll('.minus-btn');

// // Add click event listeners to the buttons
// for (let i = 0; i < plusButtons.length; i++) {
//     plusButtons[i].addEventListener('click', increaseQuantity);
//     minusButtons[i].addEventListener('click', decreaseQuantity);
// }

// Function to increase the quantity
async function increaseQuantity(event) {
    let quantityInput = event.target.parentElement.querySelector('input');
    let quantity = parseInt(quantityInput.value);
    if (quantity) {
        quantityInput.value = quantity + 1;
        let price = event.target.parentElement.parentElement.querySelector('#price')
        price.innerHTML = parseInt(price.title) * quantityInput.value + ' PLN'
        let total_price = event.target.parentElement.parentElement.parentElement.querySelector('#total_price')
        let priv_price = parseInt(total_price.title)
        total_price.title = priv_price + parseInt(price.title)
        total_price.innerHTML = total_price.title + ' PLN'
    }
}

// Function to decrease the quantity
async function decreaseQuantity(event) {
    let quantityInput = event.target.parentElement.querySelector('input');
    let quantity = parseInt(quantityInput.value);
    console.log(quantity)
    if (quantity > 1) {
        quantityInput.value = quantity - 1;
        let price = event.target.parentElement.parentElement.querySelector('#price')
        let dec_price =  parseInt(price.title) * quantityInput.value
        price.innerHTML = dec_price + ' PLN'
        let total_price = event.target.parentElement.parentElement.parentElement.querySelector('#total_price')
        let priv_price = parseInt(total_price.title)
        total_price.title = priv_price - parseInt(price.title)
        total_price.innerHTML =  total_price.title + ' PLN'
    }
}

// // Function to update the total price
// function updateTotalPrice(event) {
//     let quantityInput = event.target.parentElement.querySelector('input');
//     let quantity = parseInt(quantityInput.value);
//     let price = event.target.parentElement.parentElement.querySelector('#price')
//     price.innerHTML = parseInt(price.title) * quantityInput.value + ' PLN'
//     totalPrice.innerHTML = total.toFixed(2) + ' PLN';
// }

async function removeItem(event) {
  const itemElement = event.target.parentElement;
  itemElement.remove();
}

const _form = document.querySelector('#payment_summery');
_form.addEventListener('submit', handleFormSubmit);
function handleFormSubmit(event) {
  event.preventDefault(); // prevent the form from submitting
  const cart_div = document.getElementsByClassName("summery");
  const p_elements = cart_div[0].getElementsByTagName("p");
  let data = {}
  for (let i = 0; i < p_elements.length - 1 ; i++) {
      const p_element = p_elements[i];
      // Do something with each p_element, e.g. console.log its text content
      const a_tag = p_element.querySelector("a")
      data[a_tag.id] = {}
      const quant = p_element.querySelector('#price_quantity');
      data[a_tag.id] = {'quantity':parseInt(quant.value), 'name' : a_tag.id}
    }
  const total_price =  cart_div[0].querySelector("#total_price");
  data['total_price'] = parseInt(total_price.title)
     var base_url = window.location.origin;
     $.ajax({
        type: 'GET',
        url: base_url + '/submit-checkout/',
        contentType: 'application/json; charset=utf-8',
        // dataType: 'json',
         headers: {
        'Accept': 'application/json',
    },
        data: data,
        success: function (response) {
            window.location.href = "fsummery/" + response['order_id'];
        },
        failure: function (response) {
             console.log("f")
            alert(response.text)
        },
        error: function(jqXHR, textStatus, errorThrown) {
    // Handle the error
    console.log("Error: " + textStatus);
    console.log("Status code: " + jqXHR.status);
    console.log("Error thrown: " + errorThrown);
  }
    })
}
