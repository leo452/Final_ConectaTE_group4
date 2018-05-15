function ListaEdiciones(id) {
    $.ajax({
        url:'/herramientas/reporte/'+id,
        type: 'GET',
        dataType: 'json',
        success: function(response){
            var data = response.lista_ediciones;
            var modal = $("#tabla_ediciones tbody");
            var html;
            data.forEach(function (element) {
                html +=`<tr>
                    <td>${element.usuarioHerramienta__username}</td>
                    <td>${element.creacion}</td>
                </tr>`;
            });
            modal.html("");
            modal.append(html);
            $('#myModal').modal('show')
        }
    })
}

function ListaTutorial(id) {

}

function ListaEjemplos(id) {

}