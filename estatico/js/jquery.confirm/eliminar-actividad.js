$(document).ready(function(){
	
	$('a.eliminar2').click(function(evento) {
		evento.preventDefault();
		//var elem = $(this).closest('.item');
        var url = $(this).attr('href');

		$.confirm({
			'title'		: 'Eliminar actividad',
			'message'	: '¿Está seguro que desea eliminar esta actividad?',
			'buttons'	: {
				'Sí'	: {
					'class'	: 'green',
					'action': function(){
                        window.location = url;
					}
				},
				'No'	: {
					'class'	: 'gray',
					'action': function(){}	// Nothing to do in this case. You can as well omit the action property.
				}
			}
		});
		
	});
	
});
