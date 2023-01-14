function getProductDetail() {
    var base_url = window.location.origin;
    var id = window.location.toString()
    let _id = id.charAt(id.length - 1);
    $.ajax({
        type: 'GET',
        url: base_url + '/product/detail/' + _id,
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function (response) {
            const main_img = document.getElementsByClassName('product-image-main')
            const img = document.createElement('img')
            img.src = "/media/" + response['images'][0]
            img.id = 'product-main-image'
            img.alt = ''
            main_img[0].append(img)
            const side_img = document.getElementsByClassName('product-image-slider')
            response['images'].forEach(function (element) {
                const img_1 = document.createElement('img')
                img_1.src = "/media/" + element
                img_1.className = 'image-list'
                img_1.alt = ''
                img_1.setAttribute("onclick", "ImgClick(event)");
                side_img[0].append(img_1)
            })


            const categorie = document.getElementsByClassName('active')
            categorie[0].innerHTML = response['name']
            if (response['discount'] && (response['discount'] > 0)) {
                const price = document.getElementsByClassName('offer-price')
                price[0].innerHTML = '$' + (response['price'] - (response['price'] * (response['discount'] / 100)))
                const sale_price = document.getElementsByClassName('sale-price')
                sale_price[0].innerHTML = '$' + response['price']
            } else {
                const price = document.getElementsByClassName('offer-price')
                price[0].innerHTML = '$' + response['price']
            }
            const title = document.getElementsByClassName('product-title')
            const title_name = document.createElement('h2')
            title_name.innerHTML = response['name']
            title[0].append(title_name)
            const description = document.getElementsByClassName('product-details')
            const description_detail = document.createElement('p')
            description_detail.innerHTML = response['description']
            description[0].append(description_detail)
        },
        failure: function (response) {
            alert(response)
        },
        error: function (response) {
            alert(response)
        }
    })
}

getProductDetail()

function ImgClick(event) {
    const sliderMainImage = document.getElementById("product-main-image");
    let src = event.target.src
    sliderMainImage.src = src
}