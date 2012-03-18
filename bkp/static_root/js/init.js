$(document).ready(function() {
	// JQGRID
	tableToGrid("#jqgrid", {
		pager : '#pager',
		rowList : [ 6, 12, 24 ],
		width : 700
	});
	jQuery("#jqgrid").setGridParam({
		rowNum : 6
	}).trigger("reloadGrid");

	// VALIDATOR
	$.validator.setDefaults({
		submitHandler : function() {
			alert("submitted!");
		},
		highlight : function(input) {
			$(input).addClass("ui-state-highlight");
		},
		unhighlight : function(input) {
			$(input).removeClass("ui-state-highlight");
		},
		errorClass : 'ui-state-error',
		submitHandler: true,
	});
	$.validator.addMethod('positiveNumber', function(value) {
		return Number(value) > 0;
	}, 'Enter a positive number.');
	

});