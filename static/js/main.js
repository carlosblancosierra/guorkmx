$(document).ready(function(){

    if($('#slider-budget').length > 0){

        var slider = document.getElementById('slider-budget');

          noUiSlider.create(slider, {

           start: [125000],
           connect: true,
           step: 10000,
           orientation: 'horizontal', // 'horizontal' or 'vertical'
           range: {
             'min': 10000,
             'max': 250000
           },
            format: wNumb({
                decimals: 3,
                thousand: '.',
            })
         });

        var inputFormat = document.getElementById('quote-budget-text');

        slider.noUiSlider.on('update', function (values, handle) {
            inputFormat.value = values[handle];
        });

        inputFormat.addEventListener('change', function () {
            slider.noUiSlider.set(this.value);
        });

        var sliderQuoteMonth = document.getElementById('slider-month');

          noUiSlider.create(sliderQuoteMonth, {

           start: [6],
           connect: true,
           step: 1,
           orientation: 'horizontal', // 'horizontal' or 'vertical'
           range: {
             'min': 3,
             'max': 12
           },
            format: wNumb({
                decimals: 3,
                thousand: '.',
                suffix: ' (US $)'
            })
         });

        var inputQuoteMonths = document.getElementById('quote-months-text');

        sliderQuoteMonth.noUiSlider.on('update', function (values, handle) {
            inputQuoteMonths.value = values[handle];
        });

        inputQuoteMonths.addEventListener('change', function () {
            sliderQuoteMonth.noUiSlider.set(this.value);
        });
     }

//    $("#carousel-home-partnership").addClass("carousel-home-partnership");

      $("#owl-carousel-partnertship").owlCarousel({
      loop:true,
    margin:10,
    nav:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
    });

    $("#owl-carousel-casos-exito").owlCarousel({
    loop:true,
    nav:true,
    responsive:{
        0:{
            items:1
        }
    }
    });


});