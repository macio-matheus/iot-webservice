$(function(){

    HOST_NODE = 'http://localhost';

    setInterval(function(){ execute_consult(); }, 3000)
})

function execute_consult() {
    $.ajax({
      method: 'POST',
      url: HOST_NODE + '/api',
      data: {"hello":"word" },
      dataType: 'text'
    }).done(function( response ) {
        response = $.parseJSON(response);
        console.log(response.data[0])
        $('#show_data').html(JSON.stringify(response.data);
    });
}