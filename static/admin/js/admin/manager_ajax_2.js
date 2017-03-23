jQuery(document).ready(function ($) {
    $('#name').submit(function(e){
        e.preventDefault();
        var data = $(this).serialize();
        $.ajax({
            type: "POST",
            url: "/change_equipment/",
            data: data,
            cache: false,
            success: function(data){
                if (data == 'ok'){
                   $('#error-name').html(data)
                   location.reload();
                }
                else{
                   $('#error-name').html(data);
                }
            }
       });
    });
});
