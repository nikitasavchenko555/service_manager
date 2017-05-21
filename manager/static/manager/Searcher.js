$(document).ready(function() {
$("#sender").click( function(event) {
       
       find_number = document.getElementById('find_number').value;
       $.get('/index/find_issues/', { num: find_number}, function(data){
          if (data != "")
          {
          arr = data.split("''")
          var td;
          td = '<tr id="succes" class="tr_click">'
          for (var i = 0; i < arr.length; i++) {
          cell = arr[i];
          cell = cell.replace("'", "");
          link = arr[0].replace("'", "");
          if (i != 0) 
          {
          if ((i % 6) == 0) {
          td +=  '</tr><tr id="succes" class="tr_click"><td>' + cell + '</td>';
          } 
          else { 
          td += '<td>' + cell + '</td>'; 
          }
          }
          else { 
          td += '<td>' + cell + '</td>';
          }
          $('#sucess').html(td);
          }
          }
          else
              {
               alert("К сожалению, ничего не найдено, попробуйте уточнить поиск");
              }
          
          
       $("#sucess").click( function(event){
   		myWin=open('/index/issue/'+link+'/');
        });
        });
       });

$("#sender_2").click( function(event) {
       
       find_number = document.getElementById('find_number').value;
       $.get('/index/find_content/', { num: find_number}, function(data){
          if (data != "")
          {
          arr = data.split("''")
          var td;
          td = '<tr id="succes" class="tr_click">'
          for (var i = 0; i < arr.length; i++) {
          cell = arr[i]
          cell = cell.replace("'", "");
          link = arr[0].replace("'", "");
          if (i != 0) 
          {
          if ((i % 6) == 0) {
          td += '</tr><tr id="succes" class="tr_click"><td>' + cell + '</td>';
          } 
          else { td += '<td>' + cell + '</td>'; 
          }
          }
          else { td += '<td>' + cell + '</td>';
          }
          $('#sucess').html(td);
          }
          }
          else
             {
               alert("К сожалению, ничего не найдено, попробуйте уточнить поиск");
             }
          
          
       $("#sucess").click( function(event){
   		myWin=open('/index/issue/'+link+'/');
        });
        });
       });
});
