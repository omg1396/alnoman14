$(function () {
    new WOW().init();
    $('.home_products_slider').owlCarousel({
        loop:true,
        margin:10,
        autoplay:true,
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

$(function() {
    'use strict';
    $('.langs_dropdown').on('click', function() {
        $(this).find('ul').toggle();
    });
    $('body').on('click', '.o_header_affix .langs_dropdown, .o_header_affix .langs_dropdown ul', function() {
        $(this).find('ul').toggle();
    });
    $(document).on('click', function() {
        $('.nav_menu_language').hide();
    });
    $(document).on('click', '.o_header_affix .langs_dropdown .nav_menu_language', function() {
        $(this).hide();
    });
    $('.langs_dropdown').on('click', function(e) {
        e.stopPropagation();
    });
    $('body').on('click', '.o_header_affix .langs_dropdown', function(e) {
        e.stopPropagation();
    });
})