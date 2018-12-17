$(function(){

    HOST_NODE = 'http://dec454f9.ngrok.io';//'http://localhost';

    setInterval(function(){ execute_consult(); }, 5000)
})

function execute_consult() {
    $.ajax({
      method: 'POST',
      url: HOST_NODE + '/api',
      data: {"hello":"word" },
      dataType: 'text'
    }).done(function( response ) {
        response = $.parseJSON(response);
        $('#show_data').html(JSON.stringify(response.data.reverse()));
    });
}