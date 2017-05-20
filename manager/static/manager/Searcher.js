$(document).ready(function() {
$("#sender").click( function(event) {
       
       find_number = document.getElementById('find_number').value;
       //alert(find_number);
       $.get('/index/find_issues/', { num: find_number}, function(data){
          //var result;
          arr = data.split(',')
          var td;
          for (var i = 0; i < arr.length; i++) {
          cell = arr[i].replace(",", "");
          cell = cell.replace("[(", "");
          cell = cell.replace(")]", ""); 
          link = arr[0].replace(",", "");
          link = link.replace("[(", "");
          td += '<td>' + cell + '</td>';
          $('#sucess').html(td);
          //alert(link);
        }
       $("#sucess").click( function(event){
   		myWin=open('/index/issue/'+link+'/');
        });
        });
       });

$("#sender_2").click( function(event) {
       
       find_number = document.getElementById('find_number').value;
       //alert(find_number);
       $.get('/index/find_content/', { num: find_number}, function(data){
          //var result;
          arr = data.split(',')
          var td;
          for (var i = 0; i < arr.length; i++) {
          cell = arr[i].replace(",", "");
          cell = cell.replace("[(", "");
          cell = cell.replace(")]", ""); 
          link = arr[0].replace(",", "");
          link = link.replace("[(", "");
          td += '<td>' + cell + '</td>';
          $('#sucess').html(td);
          //alert(link);
        }
       $("#sucess").click( function(event){
   		myWin=open('/index/issue/'+link+'/');
        });
        });
       });
});
