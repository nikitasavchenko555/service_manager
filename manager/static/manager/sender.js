$(document).ready(function() {
$("#inventory").click( function(event) {
       var sender;
       sender = $("#inventory option:selected").text();
       //alert(sender)
       $.get('/index/create_issue/', {send: sender}, function(message){ 
       $('#succes_equipment').html(message)
       });
       });
$("#request_equipment").click( function(event) {
       // using jQuery
         function getCookie(name) {
         var cookieValue = null;
         if (document.cookie && document.cookie != '') {
         var cookies = document.cookie.split(';');
         for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
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
    // these HTTP methods do not require CSRF protection
          return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
       }
    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
    });
       var sender = $("#inventory option:selected").text();
       var catid = $("#type_inventory option:selected").text();
       var mode = $("#model option:selected").text();
       $.post('/index/create_issue/',
       {
	  num: sender,
          cat_id: catid,
          model: mode
	},
        function(data)
	{
	   $('#succes_equipment').html(data)
	});
});
});
