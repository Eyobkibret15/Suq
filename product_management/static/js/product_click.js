function ProductCardClicked(event) {
     id = event.target.id
     if ((id) && (!isNaN(id))){
          window.location.href = "product/" + id;
     }

}