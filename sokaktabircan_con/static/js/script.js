

console.log("running");
// ************************************************
// Shopping Cart API
// ************************************************
var shoppingCart = (function() {
    // =============================
    // Private methods and propeties
    // =============================
    cart = [];

    // Constructor
    function Item(pic,name, price, count) {
        this.pic = pic;
        this.name = name;
        this.price = price;
        this.count = count;
    }

    // Save cart
    function saveCart() {
        sessionStorage.setItem('shoppingCart', JSON.stringify(cart));
    }

    // Load cart
    function loadCart() {
        cart = JSON.parse(sessionStorage.getItem('shoppingCart'));
    }
    if (sessionStorage.getItem("shoppingCart") != null) {
        loadCart();
    }


    // =============================
    // Public methods and propeties
    // =============================
    var obj = {};

    // Add to cart
    obj.addItemToCart = function(pic,name, price, count) {
        for(var item in cart) {
            if(cart[item].name === name) {
                cart[item].count ++;
                saveCart();
                return;
            }
        }
        var item = new Item(pic,name, price, count);
        cart.push(item);
        saveCart();
    }
    // Set count from item
    obj.setCountForItem = function(pic,name, count) {
        for(var i in cart) {
            if (cart[i].pic === pic) {
                cart[i].name=name;
                cart[i].count = count;
                break;
            }
        }
    };
    // Remove item from cart
    obj.removeItemFromCart = function(pic,name) {
        for(var item in cart) {
            if(cart[item].name === name) {
                cart[item].count --;
                if(cart[item].count === 0) {
                    cart.splice(item, 1);
                }
                break;
            }
        }
        saveCart();
    }

    // Remove all items from cart
    obj.removeItemFromCartAll = function(pic,name) {
        for(var item in cart) {
            if(cart[item].name === name) {
                cart.splice(item, 1);
                break;
            }
        }
        saveCart();
    }

    // Clear cart
    obj.clearCart = function() {
        cart = [];
        saveCart();
    }

    // Count cart
    obj.totalCount = function() {
        var totalCount = 0;
        for(var item in cart) {
            totalCount += cart[item].count;
        }
        return totalCount;
    }

    // Total cart
    obj.totalCart = function() {
        var totalCart = 0;
        for(var item in cart) {
            totalCart += cart[item].price * cart[item].count;
        }
        return Number(totalCart.toFixed(2));
    }

    obj.totalKargo = function() {
        var totalKargo = 0;
        for(var item in cart) {
            totalKargo += cart[item].price * cart[item].count+10;
        }
        return Number(totalKargo.toFixed(2));
    }

    // List cart
    obj.listCart = function() {
        var cartCopy = [];
        for(i in cart) {
            item = cart[i];
            itemCopy = {};
            for(p in item) {
                itemCopy[p] = item[p];

            }
            itemCopy.total = Number(item.price * item.count).toFixed(2);
            cartCopy.push(itemCopy)
        }
        return cartCopy;
    }

    // cart : Array
    // Item : Object/Class
    // addItemToCart : Function
    // removeItemFromCart : Function
    // removeItemFromCartAll : Function
    // clearCart : Function
    // countCart : Function
    // totalCart : Function
    // listCart : Function
    // saveCart : Function
    // loadCart : Function
    return obj;
})();


// *****************************************
// Triggers / Events
// *****************************************
// Add item
$('.add-to-cart').click(function(event) {
    event.preventDefault();
    var pic = $(this).data('pic');
    var name = $(this).data('name');
    var price = Number($(this).data('price'));
    shoppingCart.addItemToCart(pic,name, price, 1);
    displayCart();
});

// Clear items
$('.clear-cart').click(function() {
    shoppingCart.clearCart();
    displayCart();
});


function displayCart() {
    var cartArray = shoppingCart.listCart();
    var output = "";
    for(var i in cartArray) {
        output += "<div class=\"product row border-bottom \">"
            +"<div class=\"row align-items-center col-11\">"
                +"<div class=\"col-2\"><img class=\"img-fluid\" src='/Users/HILAL-PC/Desktop/Django/sokaktabircan_con/static/img/"+cartArray[i].pic+"'></div>"
                
                +"<div class=\"col-4\">"
                    +"<div class=\"row text-muted\">" + cartArray[i].name + "</div>"
                 +"</div>"
                +"<div class=\"col-3\">"
                    + "<button class='minus-item btn-sepet' data-name=" + cartArray[i].name + ">-</button>"
                    +"<a class=\"item-count border\" style=\"padding:0 5px\">"+ cartArray[i].count +"</a>"
                    + "<button class='plus-item btn-sepet ' data-name=" + cartArray[i].name + ">+</button>"
                +"</div>"
                +"<div class=\"col-3\">"
                     +"&#8378; "+cartArray[i].total
                 +"</div>"
            + "</div>"
            +"<div class=\"row align-items-center col-1\">"
                +"<div class=\"col-1 align-content-end\">"
                    + "<span class='delete-item close ' data-name=" + cartArray[i].name + ">&#10005;</span>"
                +  "</div>"
            +  "</div>"
            +  "</div>";
    }

    $('.show-cart').html(output);
    $('.total-cart').html(shoppingCart.totalCart());
    $('.total-kargo').html(shoppingCart.totalKargo());
    $('.total-count').html(shoppingCart.totalCount());
}

// Delete item button

$('.show-cart').on("click", ".delete-item", function(event) {
    var pic = $(this).data('pic')
    var name = $(this).data('name')
    shoppingCart.removeItemFromCartAll(pic,name);
    displayCart();
})


// -1
$('.show-cart').on("click", ".minus-item", function(event) {
    var pic = $(this).data('pic')
    var name = $(this).data('name')
    shoppingCart.removeItemFromCart(pic,name);
    displayCart();
})
// +1
$('.show-cart').on("click", ".plus-item", function(event) {
    var pic = $(this).data('pic')
    var name = $(this).data('name')
    shoppingCart.addItemToCart(pic,name);
    displayCart();
})

// Item count input
$('.show-cart').on("change", ".item-count", function(event) {
    var pic = $(this).data('pic')
    var name = $(this).data('name')
    var count = Number($(this).val());
    shoppingCart.setCountForItem(pic,name, count);
    displayCart();
});

displayCart();
