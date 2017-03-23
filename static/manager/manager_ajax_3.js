$(document).ready(function() {

    $("#name").click( function(event) {
       var catid;
       catid = $(this).attr("data-catid");
       $.get('/change_equipment_view/', {name: catid}, function(data){
       $('#error-name').html(data); 
       });
});
});


