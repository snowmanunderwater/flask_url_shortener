$(document).ready(function() {

    $('form').on('submit', function(event) {

        $.ajax({
            data : {
                link_to_shorten  : $('#link_to_shorten').val(),
            },
            type : 'POST',
            url : '/process'
        })
        
        .done(function(data) {

            if (data.error) {
                $('#errorAlert').text(data.error).show();
                $('#successAlert').hide();
            } else {
                $("span[name=ret_msg]").text(data.urll);
                $("a[name=link]").text(data.urll);
                $("a[name=link]").attr("href", data.urll);
            }

        });

        event.preventDefault();

    });

});