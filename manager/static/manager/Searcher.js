$(document).ready(function() {
$("#sender").click( function(event) {
       
       find_number = document.getElementById('find_number').value//$("#find_number").text();
       alert(find_number)
       $.get('/index/find_issues/', { num: find_number}, function(data){ 
       //alert(data)
       //$('#succes_equipment').html(message)
       result = '<td>{{ '+data+'  }}</td>'
       $('#sucess').html(result)
       });
       });
});
