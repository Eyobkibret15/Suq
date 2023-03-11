async function getOrder() {
    var base_url =window.location.href;
    console.log(base_url)
    $.ajax({
        type: 'GET',
        url: base_url + '/get-order',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function (response) {
            const b = document.getElementById('order_id')
            b.innerHTML = ' - ' + response['id']
            const cls = document.getElementsByClassName('description')
            Object.keys(response).forEach((name) => {
               if (!['id','total_price','sub_total','delivery_total'].includes(name)){
                   const h1 = document.createElement('h1')
                   h1.innerHTML = name
                   cls[0].append(h1)
                   const p1 = document.createElement('p')
                   p1.innerHTML = "Product code: " + response[name]['pnumber']
                   p1.className = "product-code small muted"
                   cls[0].append(p1)
                   const h3 = document.createElement('p')
                   h3.innerHTML = 'Price: ' +  response[name]['price'] + ' PLN'
                   cls[0].append(h3)
                   const p3 = document.createElement('p')
                   p3.innerHTML = 'Delivery: ' +  response[name]['delivery']
                   cls[0].append(p3)
                   const br = document.createElement('br')
                   cls[0].append(br)
               }
           })
            const sub_total = document.getElementsByClassName('subtotal')
            const p4 = document.createElement('p')
            p4.innerHTML = 'Price subtotal:'
            p4.className = 'small'
            const p5 = document.createElement('p')
            p5.innerHTML = response['sub_total'] + ' PLN'
            p5.className = 'small'
            sub_total[0].append(p4,p5)
            const delivery = document.getElementsByClassName('delivery')
            const p6 = document.createElement('p')
            p6.innerHTML = 'Delivery (Standard - 2 working days):'
            p6.className = 'small'
            const p7 = document.createElement('p')
            p7.innerHTML = response['delivery_total'] + ' PLN'
            p7.className = 'small'
            delivery[0].append(p6,p7)
            const total = document.getElementsByClassName('total')
            const h4 = document.createElement('h3')
            h4.innerHTML = 'Total:'
            const h5 = document.createElement('h3')
            h5.innerHTML = response['total_price'] + ' PLN'
            total[0].append(h4,h5)
        },
        failure: function (response) {
            alert(response)
        },
        error: function (response) {
            alert(response)
        }
    })
}

getOrder()
