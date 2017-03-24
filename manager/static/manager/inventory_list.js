$(document).ready(function() {
$("#model").click( function(event) {
       var mode;
       mode = $("#model option:selected").text();
       $.get('/index/create_issue/', {model: mode}, function(message){ 
        var mod;
        arr = message.split(',,')
        //alert(arr)
        var options = '<option value="">---------- </option>';
       for (var i = 0; i < arr.length; i++) {
          mod = arr[i].replace(",", "");
          options += '<option>' + mod + '</option>';
          //alert(options)
        }
       $('#inventory').html(options)
       
   });
});
});
