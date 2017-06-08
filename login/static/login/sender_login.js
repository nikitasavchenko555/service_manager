function Sender_Login() {
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
       var form_send = $('#login').serialize();
       $('#result_login').html();
       $.post('/login/',
       {
	  data: form_send
	},
        function(data)
	{
           //alert(data);
           $('#result_login').html();
           if (data == 'Успешно')
           {
             location = "http://localhost:8000/index/"
           }
           else
           {
           $('#result_login').html(data);
           }
	}

);
};
