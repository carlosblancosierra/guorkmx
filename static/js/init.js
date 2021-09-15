M.AutoInit();

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.slider');
    var instances = M.Slider.init(elems, {'height' : 200, 'indicators' : true});

    var navDropdown = document.querySelectorAll('.dropdown-trigger-main');
    var instances = M.Dropdown.init(navDropdown, ({alignment:'left', 'hover':true, 'constrainWidth':false}));
});