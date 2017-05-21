$(document).ready(function() {
$("#type_inventory").click( function(event) {
       var catid;
       catid = $("#type_inventory option:selected").text();
       $.get('/index/create_issue/', {name: catid}, function(message){ 
        var mod;
        arr = message.split(',,')
        //alert(arr)
        var options = '<option value=""></option>';
       for (var i = 0; i < arr.length; i++) {
          mod = arr[i].replace(",", "");
          options += '<option>' + mod + '</option>';
          //alert(options)
        }
       $('#model').html(options)
       
   });
});
});
