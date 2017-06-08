$(document).ready(function() {
$("#my_work").click( function(event) {
       var catid;
       spaces = $("#my_work option:selected").text();
       $.get('/index/create_issue/', {space: spaces}, function(message){ 
        var space;
        //alert(message)
        arr = message.split(',,')
        //alert(arr)
        var options = '<option value=""></option>';
       for (var i = 0; i < arr.length; i++) {
          space = arr[i].replace(",", "");
          //alert(space)
          options += '<option>' + space + '</option>';
          //alert(options)
        }
       $('#type_inventory').html(options)
       
   });
});
});
