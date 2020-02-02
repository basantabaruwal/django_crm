document.addEventListener("DOMContentLoaded", function() {
    var sidenav = document.getElementById('sidenav');
    var instances = M.Sidenav.init(sidenav);
    // console.log(sidenav);
    var dropDownTriggers = document.querySelectorAll('.dropdown-trigger');
    M.Dropdown.init(dropDownTriggers);

    var collapsibles = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsibles);

    // for rendering the select tags
    var selectElms = document.querySelectorAll('select');
    M.FormSelect.init(selectElms);
});