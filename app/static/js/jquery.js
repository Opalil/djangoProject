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

