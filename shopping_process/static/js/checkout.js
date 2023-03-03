async function getCart() {
    var base_url = window.location.origin;
    console.log(base_url)
    $.ajax({
        type: 'GET',
        url: base_url + '/add-to-cart/',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function (response) {
            const cart = document.getElementsByClassName("container summery")
            const b1 = document.getElementById("total-quan")
            b1.innerHTML = response['quantity']
            Object.keys(response).forEach((name) => {
                if (!['quantity', 'cost'].includes(name)){
                const p = document.createElement('p')
                const link = document.createElement('a')
                link.className = 'products'
                link.id = name
                link.setAttribute("onclick", "ProductCardClicked(event)");
                link.innerHTML = name
                const span = document.createElement('span')
                span.className = 'price'
                span.innerHTML = response[name]['quantity'] + '* $' + response[name]['cost']
                p.append(link)
                p.append(span)
                cart[0].append(p)}

            });
            console.log(response)
            const p2 = document.createElement('p')
            p2.innerHTML = 'Total '
            const span2 = document.createElement('span')
            span2.className = "price"
            span2.style = "color:black"
            const hr = document.createElement('hr')
            const b2 = document.createElement('b')
            b2.innerHTML = '$' + response['cost']
            span2.append(b2)
            p2.append(span2)
            cart[0].append(hr)
            cart[0].append(p2)


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