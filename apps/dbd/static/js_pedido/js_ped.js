$(function () {
    $('.table').DataTable({
        "pageLength": 7,
        "language": {
        "sProcessing": "Procesando...",
        "sLengthMenu": "Mostrar _MENU_ registros",
        "sZeroRecords": "No se encontraron resultados",
        "sEmptyTable": "Ningún dato disponible en esta tabla",
        "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
        "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
        "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
        "sInfoPostFix": "",
        "sSearch": "Buscar:",
        "sUrl": "",
        "sInfoThousands": ",",
        "sLoadingRecords": "Cargando...",
        "oPaginate": {
            "sFirst": "<span class='fa fa-angle-double-left'></span>",
            "sLast": "<span class='fa fa-angle-double-right'></span>",
            "sNext": "<span class='fa fa-angle-right'></span>",
            "sPrevious": "<span class='fa fa-angle-left'></span>"
        },
        "oAria": {
            "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
            "sSortDescending": ": Activar para ordenar la columna de manera descendente"
        }
        },
        responsive:true,
    });

    $('#id_cantidad_detalle,#id_precio_detalle,#id_iva_detalle').change(function(){
        calcular_detalle();
    });
    
    $('#frmPedido').submit(function(e){
        if($('#id_total_detalle').val()==0 || $('#id_id_producto_producto').val()==0){
            e.preventDefault();
            mensaje('No ha agregado Producto, Agrege uno');
        }
    });

    $(document).ready(function() {
        $('.select-clit').select2({
        theme: 'bootstrap4',
    });
});
});

function selectProducto(id_producto,nombre){
    $('#id_cantidad_detalle').val(0);
    $('#id_precio_detalle').val(0);
    $('#id_subtotal_detalle').val(0);
    $('#id_iva_detalle').val(0);
    $('#id_total_detalle').val(0);

    $('#id_id_producto_producto').val(id_producto)
    $('#id_nombre_producto').val(nombre);
    $('#id_cantidad_detalle').focus();
    $('#id_cantidad_detalle').select();

    $('.table').DataTable().search('').draw();

}

function calcular_detalle(){
    var cant,prec,iva,stotal,total;
    cant = $('#id_cantidad_detalle').val();
    cant = cant === "" ? 0 : +cant;
    cant = cant<0 ? 0 : cant;

    prec = $('#id_precio_detalle').val();
    prec = prec === "" ? 0 : +prec;
    prec = prec<0 ? 0 : prec;


    iva = $('#id_iva_detalle').val();
    iva = iva === "" ? 0 : +iva;
    iva = iva<0 ? 0 : iva;

    iva = iva >(cant*prec) ? 0 : iva;

    stotal = cant * prec;
    total = stotal+(stotal * (iva/100))

    $('#id_cantidad_detalle').val(cant);
    $('#id_precio_detalle').val(prec);
    $('#id_iva_detalle').val(iva);
    
    $('#id_subtotal_detalle').val(stotal);
    $('#id_total_detalle').val(total);

}


function clear_detalle(){
    $('#id_cantidad_detalle').val(0);
    $('#id_precio_detalle').val(0);
    $('#id_iva_detalle').val(0);

    $('#id_subtotal_detalle').val(0);
    $('#id_total_detalle').val(0);
    
    $('#id_id_producto_producto').val('');
    $('#id_nombre_producto').val('');

    $('.table').DataTable().search('').draw();

    $("#id_cliente").focus();
}

$("#id_cliente").focus();
