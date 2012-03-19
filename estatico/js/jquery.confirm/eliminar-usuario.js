$(document).ready(function(){
	
	$('a.eliminar2').click(function(evento) {
		evento.preventDefault();
        var url;

        url = $(this).attr('href');

		$.confirm({
			'title'		: 'Eliminar usuario',
			'message'	: '¿Está seguro que desea eliminar este usuario?',
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
