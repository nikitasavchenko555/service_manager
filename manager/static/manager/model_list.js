$(document).ready(function() {
$("#my_select").click( function(event) {
       var catid;
       catid = $("#my_select option:selected").text();
       $.get('/index/create_issue/', {name: catid}, function(message){ 
        var mod;
        arr = message.split(',,')
        //alert(arr)
        var options = '<option value="">---------- </option>';
       for (var i = 0; i < arr.length; i++) {
          mod = arr[i].replace(",", "");
          options += '<option>' + mod + '</option>';
          //alert(options)
        }
       $('#model').html(options)
       
   });
});
});
