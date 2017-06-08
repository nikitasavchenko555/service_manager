function Sender() {
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
       //var start = $("#start").val();
       //var end = $("#end").text();
       //var format_rep = $("#format option:selected").text();
       //alert(start);
       var form_send = $('#form_send').serialize();
       $.post('/index/reports/',
       {
	  data: form_send
	},
        function(data)
	{
           report_link = '<td>Отчёт успешно создан</td><td><a href="/media/'+data+'" download>Скачать</link></td>'
           $('#succes_report').html(report_link);
           
	}
);
};


