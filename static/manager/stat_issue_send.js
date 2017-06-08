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
           alert(data);
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
           if (stat_issue['Назначена'] === undefined)
           {
              stat_issue['Назначена'] = '--';
           };
           if (stat_issue['В работе'] === undefined)
           {
              stat_issue['В работе'] = '--';
           };
           if (stat_issue['Ожидается разрешение'] === undefined)
           {
              stat_issue['Ожидается разрешение'] = '--';
           };
           if (stat_issue['Ожидается поставка'] === undefined)
           {
              stat_issue['Ожидается поставка'] = '--';
           };
           if (stat_issue['Завершено'] === undefined)
           {
              stat_issue['Завершено'] = '--';
           };
           if (stat_issue['Завершено. Авария не подтверждена'] === undefined)
           {
              stat_issue['Завершено. Авария не подтверждена'] = '--';
           };
           if (stat_issue['Завершено. Временное решение'] === undefined)
           {
              stat_issue['Завершено. Временное решение'] = '--';
           };
           if (stat_issue['Закрыто'] === undefined)
           {
              stat_issue['Закрыто'] = '--';
           };
           
           td_issue = '<tr><td>'+stat_issue[5]+'</td><td>'+stat_issue[4]+'</td><td>'+stat_issue[3]+'</td><td>'+stat_issue[2]+'</td><td>'+stat_issue[1]+'</td></tr>';
           //alert(td_issue);
           $('#succes_stat').html(td_issue);
           td_status = '<tr><td>'+stat_issue['Назначена']+'</td><td>'+stat_issue['В работе']+'</td><td>'+stat_issue['Ожидается разрешение']+'</td><td>'+stat_issue['Ожидается поставка']+'</td><td>'+stat_issue['Завершено']+'</td></td>'+'</td><td>'+stat_issue['Завершено. Авария не подтверждена']+'</td></td>'+'</td><td>'+stat_issue['Завершено. Временное решение']+'</td><td>'+stat_issue['Закрыто']+'</td></tr>';
           //alert(td_status);
           $('#succes_status').html(td_status);
	}
);
};

