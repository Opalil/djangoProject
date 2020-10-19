var frm = $('#form')

frm.submit(function(){
    e.preventDefault();
       
    $.ajax({
        url: frm.attr('action'),
        type: 'POST',
        data:  frm.serialize(),            
        success: function(data){
            alert("Onnistui?");
        }
            
    });

});

const user_input = $("#user-input")
const search = $("#search")
const endpoint = ''
const rep_div = $("#replaceable-content")

let query = function(endpoint, request_parameters) {
    $.getJSON(endpoint, request_parameters)
    .done(response => {
        rep_div.fadeTo('slow', 0).promise().then(() => {
            rep_div.html(response['html_from_view'])
            rep_div.fadeTo('slow', 1)
            console.log("WHAT?")
            
        })
    })
}

user_input.on('keyup', function() {
    const request_parameters = {
        q: $(this).val()
    }
})