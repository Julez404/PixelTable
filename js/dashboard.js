
$(document).ready(function () {


    $("#First_Deck").load("/html/Cards/First_Deck.html");
    $("#Second_Deck").load("/html/Cards/Second_Deck.html");
    $("#Third_Deck").load("/html/Cards/Third_Deck.html");

    $("#Navbar_id").load("/html/Navs/Navbar_1.html");
    $("#sidebar").load("/html/Navs/Sidebar_1.html");


});


$('#sidebar-btn').click(function () {
    alert("hello");
   
    });

$("body").click(function (event) {
    $("#log").html("clicked: " + event.target.nodeName);
});