$(document).ready(function() {
$("#sender").click( function(event) {
       
       find_number = document.getElementById('find_number').value;
       alert(find_number);
       $.get('/index/find_issues/', { num: find_number}, function(data){
          var result;
          alert(data);
          $('#sucess').html(data);
        });
       });
});
