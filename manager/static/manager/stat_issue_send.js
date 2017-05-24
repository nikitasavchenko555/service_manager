function Sender_Stat() {
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
      
       var form_send = $('#form_send_stat').serialize();
       $.post('/index/view_statistic_issues/',
       {
	  data: form_send
	},
        function(data)
	{
           var stat_issue = JSON.parse(data);
           if (stat_issue[1] === undefined)
           {
              stat_issue[1] = '--';
           };
           if (stat_issue[2] === undefined)
           {
              stat_issue[2] = '--';
           };
           if (stat_issue[3] === undefined)
           {
              stat_issue[3] = '--';
           };
           if (stat_issue[4] === undefined)
           {
              stat_issue[4] = '--';
           };
           if (stat_issue[5] === undefined)
           {
              stat_issue[5] = '--';
           };
           td = '<tr><td>'+stat_issue[5]+'</td><td>'+stat_issue[4]+'</td><td>'+stat_issue[3]+'</td><td>'+stat_issue[2]+'</td><td>'+stat_issue[1]+'</td></tr>';
           $('#succes_stat').html(td);
           
	}
);
};

