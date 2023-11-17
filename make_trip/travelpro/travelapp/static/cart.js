window.addEventListener("load", function(event) {

var updateBtns = document.getElementsByClassName('update-cart');
console.log("sdfdfsdffsdfsdfdff", updateBtns.length);
for(var i = 0; i < updateBtns.length; i++){
    console.log("zx/czxc/zxc/c/zxc/c/c/c/c/c/c/cc/");
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log("cxczx.czc.xczx.cz.cxc.zxc.c.xc..c", productId);
        console.log("USER:", user)
        if(user === 'AnonymousUser'){
              console.log('Not logged in')
        }else{
             console.log('user is logged in, sending data..')
        }
    });
}
});


function updateUserOrder(productId, action){
     console.log('user is logged in, sending data')
     var url = '/update_item/'
     fetch(url,{
         method:'POST',
         headers:{
             'Content-type':'application/json',
             'X-CSRFToken':csrftoken,
         },
         body:JSON.stringify({'productId':productId, 'action':action})
     })

     .then((response) =>{
           return response.json()
     })
     .then((data) =>{
           console.log('data', data)
           location.reload()
     })
}