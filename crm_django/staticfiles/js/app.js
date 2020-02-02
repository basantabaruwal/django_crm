document.addEventListener("DOMContentLoaded", function() {
    var sidenav = document.getElementById("sidenav");
    var instances = M.Sidenav.init(sidenav);
    // console.log(sidenav);
    var dropDownTriggers = document.querySelectorAll(".dropdown-trigger");
    M.Dropdown.init(dropDownTriggers);

    var collapsibles = document.querySelectorAll(".collapsible");
    M.Collapsible.init(collapsibles);

    // for rendering the select tags
    var selectElms = document.querySelectorAll("select");
    M.FormSelect.init(selectElms);

    var itemsContainer = document.querySelector("#itemsContainer");
    console.log("Items Container: " + itemsContainer);
});


function addItemMarkup(e) {
    // alert("Iterm adding");
    e.remove();
    console.log(e);

    itemMarkup = `
<div class="section">
                            <label for="id_order_set-0-product">Product:</label><select name="order_set-0-product" id="id_order_set-0-product">
  <option value="" selected="">---------</option>

  <option value="1">Tuna Fish</option>

  <option value="2">Summer T-Shirt</option>

  <option value="3">Banana</option>

</select>
<label for="id_order_set-0-status">Status:</label><select name="order_set-0-status" id="id_order_set-0-status">
  <option value="Pending" selected="">Pending</option>

  <option value="Out for Delivery">Out for Delivery</option>

  <option value="Delivered">Delivered</option>

  <option value="Cancelled">Cancelled</option>

</select>
<label for="id_order_set-0-DELETE">Delete:</label><input type="checkbox" name="order_set-0-DELETE" id="id_order_set-0-DELETE"><input type="hidden" name="order_set-0-id" id="id_order_set-0-id"><input type="hidden" name="order_set-0-customer" value="1" id="id_order_set-0-customer">
                        </div>



                            <button class="btn btn-floating waves-effect waves-light indigo right" id="add-item-markup"
                                onClick="addItemMarkup(this)">
                                <i class="material-icons left">add</i>
                                Add New Item
                            </button>
    `;

    // console.log(itemsContainer);
    itemsContainer.insertAdjacentHTML("beforeend", itemMarkup);
    // for rendering the select tags
    var selectElms = document.querySelectorAll("select");
    M.FormSelect.init(selectElms);
}