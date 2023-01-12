

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
                col.className = 'col-lg-4 col-md-6 col-sm-10 offset-md-0 offset-sm-1'
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
                ml_auto.append(button1,span2,button2)
                d_flex.append(price,ml_auto)

                const button3 = document.createElement("button");
                button3.className = 'btn w-100 rounded my-2'
                button3.innerText = 'Add to cart'
                card_body.append(h5_tag,d_flex,button3)
                card.append(img,card_body)
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