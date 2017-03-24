$(function(){             
alert('home.html in BODY!');         
});
data-catid="{{ name }}"

<select id="my_select">
				{% for name in equipment_name %}}
				<option>{{ name }}</option>
				{% endfor %}
				</select></td>


$(document).ready(function() {

    $("#my_select").click( function(event) {
       var catid;
       catid = $("#my_select option:selected").text();
       alert(catid)
       $.get('/index/create_issue/', {name: catid}, function(message){
       $('#error-name').html(message);

function(message){
       for (var i = 0; i < message.length; i++) {
          alert(i)
        }
  
    });
});

<select>
				{% for d in data %}
				<option id="name">{{ data }}</option>
				{% endfor %}
				</select>
});


$(document).ready(function(event) {

    $("#my_select").click( function() {
       var catid;
       catid = $("#my_select option:selected").text();
       alert(catid)
       $.get('/index/create_issue/', {name: catid}, 
       function(message){
       alert(catid)
       $('#id_sub').html(message);
	}
});
});

#работает!!!
$("#my_select").click( function(event) {
       var catid;
       catid = $("#my_select option:selected").text();
       $.get('/index/create_issue/', {name: catid}, function(message){ 
        var mod;
        arr = message.split(',,')
        alert(arr)
        var options = '<option value="">---------- </option>';
       for (var i = 0; i < arr.length; i++) {
          mod = arr[i].replace(",", "");
          options += '<option>' + mod + '</option>';
          //alert(options)
        }
       $('#model').html(options)
       
   });
});
