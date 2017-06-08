$(document).ready(function() {
$("#my_work").click( function(event) {
       var catid;
       spaces = $("#my_work option:selected").text();
       $.get('/index/view_statistic_downtime/', {space: spaces}, function(message){ 
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

$("#type_inventory").click( function(event) {
       var catid;
       catid = $("#type_inventory option:selected").text();
       $.get('/index/view_statistic_downtime/', {name: catid}, function(message){ 
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

$("#model").click( function(event) {
       var mode;
       mode = $("#model option:selected").text();
       $.get('/index/view_statistic_downtime/', {model: mode}, function(message){ 
        var mod;
        arr = message.split(',,')
        //alert(arr)
        var options = '<option value=""></option>';
       for (var i = 0; i < arr.length; i++) {
          mod = arr[i].replace(",", "");
          options += '<option>' + mod + '</option>';
          //alert(options)
        }
       $('#inventory').html(options)
       
   });
});

$("#inventory").click( function(event) {
       var sender;
       sender = $("#inventory option:selected").text();
       $.get('/index/view_statistic_downtime/', {send: sender}, function(message){ 
       $('#succes_equipment').html(message)
       });
       });


});
