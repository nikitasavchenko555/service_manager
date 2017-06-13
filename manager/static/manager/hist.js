$(document).ready(function() {
        //var number_is = $("#number").text();
        //var link = '/index/issue_history/'+number_is+'/';
       $.get('/index/issue_history/', {}, function(message){ 
         if (data == '[]')
	  {
            alert("К сожалению, ничего не найдено. Пожалуйста, уточните данные");
          }
          else
          {
          arr = data.split("'], ['")
          
          td = ''
          
          for (var i = 0; i < arr.length; i++) {
          cell = arr[i];
          cell = cell.replace("[['", "");
          cell = cell.replace("']]", "");
          
          if (i != 0) 
          {
          if ((i % 12) == 0) {
          td += '</tr><tr class="tr_click"><td>' + cell +'</td>';
          } 
          else { td += '<td>' + cell + '</td>'; 
          }
          }
          else { td += '<tr class="tr_click"><td>' + cell + '</td>';
          }
          }
          }
          //alert(td);
          $('#succes_history').html(td);
          
          });
});

