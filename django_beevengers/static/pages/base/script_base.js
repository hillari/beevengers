
// THIS IS FOR THE MULTI DROPDOWN MENUS
$(function() {

  // ------------------------------------------------------- //
  // Multi Level dropdowns
  // ------------------------------------------------------ //
  $("ul.dropdown-menu [data-toggle='dropdown']").on("click", function(event) {
    event.preventDefault();
    event.stopPropagation();

    $(this).siblings().toggleClass("show");


    if (!$(this).next().hasClass('show')) {
      $(this).parents('.dropdown-menu').first().find('.show').removeClass("show");
    }
    $(this).parents('li.nav-item.dropdown.show').on('hidden.bs.dropdown', function(e) {
      $('.dropdown-submenu .show').removeClass("show");
    });

  });

  $(document).ready( function() {
    pageContent = $("#pageContent").height();
    documentHeight = $(document).height();
    newFooterHeight = documentHeight-pageContent;
    $("#footer").height(newFooterHeight);
  });

});


