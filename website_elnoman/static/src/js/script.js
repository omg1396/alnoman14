$(function () {
//    new WOW().init();
    $('.home_products_slider').owlCarousel({
        loop:true,
        margin:10,
        center:true,
        dots:true,
        responsive:{
            0: {
                items: 1,
            },
            481: {
                items: 1,
            },
            768: {
                items: 3,
            },
            1024: {
                items:5
            }
        }
    });
});

function directTel(){
    window.open('tel:00218214771882');
}
function directEmail(){
    window.open('mailto:info@elnomangroup.com');
}