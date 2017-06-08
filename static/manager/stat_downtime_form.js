function Sender_Stat_Downtime() {
         var django = django || {};
         django.jQuery = $;
         function getCookie(name) {
         var cookieValue = null;
         if (document.cookie && document.cookie != '') {
         var cookies = document.cookie.split(';');
         for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
             
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
       }
    }
    return cookieValue;
}
       var csrftoken = getCookie('csrftoken');
       function csrfSafeMethod(method) {
    
          return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
       }
    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
    });
      
       var form_send = $('#form_send_stat_d').serialize();
       var type = $("#type_inventory option:selected").text();
       var model = $("#model option:selected").text();
       var inv_num = $("#inventory option:selected").text();
       
       $.post('/index/view_statistic_downtime/',
       {
	  data: form_send,
          type: type,
          model: model,
          inv: inv_num
	},
        function(data)
	{
          //alert(data);
          arr = data.split("'], ['")
          //alert(arr);
          td = ''
          //alert(arr.length);
          for (var i = 0; i < arr.length; i++) {
          cell = arr[i];
          cell = cell.replace("[['", "");
          cell = cell.replace("']]", "");
          //alert(td);
          if (i != 0) 
          {
          if ((i % 2) == 0) {
          td += '</tr><tr class="tr_click"><td><a href="/index/issue/' + cell + '/" target="_blank">'+cell+'</a></td>';
          } 
          else { td += '<td>' + cell + '</td>'; 
          }
          }
          else { td += '<tr class="tr_click"><td><a href="/index/issue/' + cell + '/" target="_blank">'+cell+'</a></td>';
          }
          }
          //alert(td);
          $('#succes_stat_down').html(td);
          
          
           
	}
);
};
