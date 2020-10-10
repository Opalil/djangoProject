//const { data } = require("jquery");

$(document).ready(function(){
    $("#update").click(function() {
        //alert("Tuote lisätty ostoskoriin!")
        var product_id = $(this).attr('data-id');
        //var product_name = $('#item_name'+product_id.val());

        $.ajax({
            url: '/cart/',
            dataType: 'html',
            type: 'POST',
            data: {productId : product_id},
            success: function(data){
                
                $('#get-data'.html(data))
            }
            
        });
        alert("Tuote lisätty ostoskoriin: " + product_id)
        //$('#table tr:last').after('<tr>{product_id}</tr><tr>{product_name}</tr>');
    });
});

