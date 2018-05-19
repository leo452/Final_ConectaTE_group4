/**
 * Created by dark on 31/03/18.
 */
/**
 * Created by dark on 31/03/18.
 */
$(function(){
    $('.save-importer').click(function (event) {
        var datos_selecionados = $('.selectpicker').selectpicker('val').map(function(x){ return parseInt(x);});
        var res = [];
        for (var i=0; i< window.data.length ; i++){
            if (parseInt(window.data[i].row) in datos_selecionados){
                res.push(window.data[i]);
            }
        }
        console.log(res);
        $.ajax({
            url:'/herramienta/importer/save/',
            type:'post',
            dataType : 'json',
            data: {rows: $('.selectpicker').selectpicker('val'), file: window.id_file, data:JSON.stringify(res)},
            dataType: 'json',
            success: function (data) {
                if(data.respuesta){
                    location.href = "/herramienta/importer/";
                }
            }
        });
    });
});

/*$(function(){
    $('.save-importer').click(function (event) {
        $.ajax({
            url:'/herramienta/importer/save/',
            type:'post',
            data: {rows: $('.selectpicker').selectpicker('val'), file: window.id_file},
            dataType: 'json',
            success: function (data) {

            }
        });
    });
});*/