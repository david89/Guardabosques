
function all(){



$(".objetivo2").simpletip({
               content: 'holamundo 2',
               fixed: true, 
               position: 'bottom' 
});

$(".objetivo3").simpletip({
               content: 'holamundo 3',
               fixed: true, 
               position: 'bottom' 
});

$(".objetivo4").simpletip({
               content: 'holamundo 4',
               fixed: true, 
               position: 'bottom' 
});

$(".objetivo5").simpletip({
               content: 'holamundo 5',
               fixed: true, 
               position: 'bottom' 
});

$('#date').datepicker({
    	inline: true
});

$(".timer").change(function(){
   var object = ($(this).attr('id')).split("_");
   var id = parseInt(object[2]);

   var hi = parseInt($("#h_i_"+id).val());
   var hf = parseInt($("#h_f_"+id).val());
   var mi = parseInt($("#m_i_"+id).val());
   var mf = parseInt($("#m_f_"+id).val());
               
   var h = hf - hi;
   var m = mf - mi; 

   if (m < 0){
       $("#total"+id).val((h-1)+"h"+(60+m)+"m");
   } else {
       $("#total"+id).val(h+"h"+m+"m");                
   }
});

}
/*
function addrow(){
}
*/
$(document).ready(function(){
	all();
	//addrow();
});




