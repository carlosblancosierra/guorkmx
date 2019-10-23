$(document).ready(function () {

    $('#owl-carousel-testimonials').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        responsive: {
            0: {
                items: 1
            },
        }
    })

    $("#cotizar-btn").click(function () {
        $(this).addClass("disabled");
        $(this).text('Cotizando tu seguro de Auto');
        $(this).append('<div class="progress"><div class="indeterminate"></div></div>');
    });
});

