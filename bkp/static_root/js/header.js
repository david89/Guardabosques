
/*
var bustcachevar=1 ;// bust potential caching of external pages after initial
					// request? (1=yes, 0=no)
var loadedobjects="";
var rootdomain="http://"+window.location.hostname;
var bustcacheparameter="";
var buscar = 0;


var time = 0;
var transparency = 0;
var sizeMain = 48;
var sizeMenu = 48;
//
*/
//document.write("<style type='text/css'>#main {visibility:hidden;}</style>");
//document.write("<style type='text/css'>#menu {visibility:hidden;}</style>");

function submitform()
{
  document.xxx.submit();
}

      $(document).ready(function (){
   
          $("form").submit( function (){  
   
              alert("SUBMIT");
   
              return false; //Si devolvemos false, el formulario ya no se enviará.
   
          });
   
      });


/*

function fadeIn() {
	  //
	  transparency += 10; //
	  transparency = (transparency > 100) ? clearInterval(time) : transparency;
	  //
	  obj = document.getElementById('main');
	  obj.style.visibility = 'visible';
	  obj2 = document.getElementById('menu');
	  obj2.style.visibility = 'visible';

	  if (document.all){
	    // esto es para IE, como siempre hay q programarlo a parte
	    obj.style.filter = 'alpha(opacity='+transparency+')';
	    obj2.style.filter = 'alpha(opacity='+transparency+')';
	  
	  }else{
	    // Safari 1.2, posterior Firefox y Mozilla, CSS3
		obj.style.opacity = transparency /100;
		obj2.style.opacity = transparency /100;
	    // anteriores Mozilla y Firefox
	    obj.style.MozOpacity = transparency /100;
	    obj2.style.MozOpacity = transparency /100;
	    // Safari anterior a 1.2, Konqueror
	    obj.style.KHTMLOpacity = transparency /100;  
	    obj2.style.KHTMLOpacity = transparency /100;
	  } 
	};



function resizeIn() {
  //
  transparency += 10; //
  transparency = (transparency > 100) ? clearInterval(time) : transparency;
  //
  main = document.getElementById('main');
  main.style.visibility = 'visible';
  menu = document.getElementById('menubar');
  menu.style.visibility = 'visible';
//  main.style.width = ""+sizeMain+"%";
 // menu.style.width = ""+sizeMenu+"%";
  
  //sizeMain+=2.5;
  //sizeMenu-=2.5;

  if (document.all){
    // esto es para IE, como siempre hay q programarlo a parte
    main.style.filter = 'alpha(opacity='+transparency+')';
    menu.style.filter = 'alpha(opacity='+transparency+')';
  
  } else {
    // Safari 1.2, posterior Firefox y Mozilla, CSS3
	main.style.opacity = transparency /100;
	menu.style.opacity = transparency /100;
    // anteriores Mozilla y Firefox
    main.style.MozOpacity = transparency /100;
    menu.style.MozOpacity = transparency /100;
    // Safari anterior a 1.2, Konqueror
    main.style.KHTMLOpacity = transparency /100;  
    menu.style.KHTMLOpacity = transparency /100;
  } 
};
//
window.onload = function() {
  time = setInterval('fadeIn()',100);
};

function ajaxresize(url, containerid,form) {
	time = 0;
	transparency = 0;
	sizeMain = 48;
	sizeMenu = 48;
	time = setInterval('resizeIn()',100);
    ajaxpage(url, containerid,form);
};
	
function ajaxfade(url, containerid,form) {
	time = 0; 
	transparency = 0;
	sizeMain = 48;
	sizeMenu = 48;
	time = setInterval('fadeIn()',100);
	ajaxpage(url, containerid,form);
};
	
function ajaxpage(url, containerid,form) {
	var page_request = false;
	
    if (window.XMLHttpRequest) // if Mozilla, Safari etc
        page_request = new XMLHttpRequest();
    else if (window.ActiveXObject){ // if IE
		try {
			page_request = new ActiveXObject("Msxml2.XMLHTTP")
		} catch (e) {
			try {
				page_request = new ActiveXObject("Microsoft.XMLHTTP")
			} catch (e) {
				alert("Your browser does not support AJAX!");
			}
		}
	}
	else
		return false
	
	page_request.onreadystatechange=function(){
		loadpage(page_request, containerid)
	}
	
	if (form != ""){
		var frm = document.forms[form]; // formName needs to be the name of your
										// form
		var pineapple = frm.elements;

		if(frm.method.toLowerCase() === "post") {
			page_request.open('POST', url, true);
			page_request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

			for(var i = 0;i < pineapple.length; i++) 
				page_request.send(pineapple[i].name + "=" + pineapple[i].value);
		} else {
			var query_string = "?";
			for(var ji = 0; ji < pineapple.length; ji++)
				query_string += escape(pineapple[ji].name) + "=" + escape(pineapple[ji].value) + (ji + 1 < pineapple.length ? "&" : "");
			page_request.open('GET', url + query_string, true);
			page_request.send(null);
		}
	} else {
		if (bustcachevar) // if bust caching of external page
			bustcacheparameter=(url.indexOf("?")!=-1)? "&"+new Date().getTime() : "?"+new Date().getTime()
		page_request.open('GET', url+bustcacheparameter, true);
		page_request.send(null);
	}
}


function loadpage(page_request, containerid){
	if (page_request.readyState == 4 && (page_request.status==200 || window.location.href.indexOf("http")==-1))
		document.getElementById(containerid).innerHTML=page_request.responseText;
}

function loadobjs(){
	if (!document.getElementById)
	return
		for (i=0; i<arguments.length; i++){
		var file=arguments[i]
		var fileref=""
		if (loadedobjects.indexOf(file)==-1){ // Check to see if this object
												// has not already been added to
												// page before proceeding
			if (file.indexOf(".js")!=-1){ // If object is a js file
				fileref=document.createElement('script')
				fileref.setAttribute("type","text/javascript");
				fileref.setAttribute("src", file);
			} else if (file.indexOf(".css")!=-1){ // If object is a css file
				fileref=document.createElement("link")
				fileref.setAttribute("rel", "stylesheet");
				fileref.setAttribute("type", "text/css");
				fileref.setAttribute("href", file);
			}
		}
		if (fileref!=""){
			document.getElementsByTagName("head").item(0).appendChild(fileref)
			loadedobjects+=file+" " // Remember this object as being already
									// added to page
		}
	}
}


/* antixss.js.php por Carlos Mesa *//*
function verifica_url(url){
        var host, path_info
        host = 'http://'+location.host;
        path_info = (location.pathname.indexOf('?') != -1) ? location.pathname.substring(0, location.pathname.indexOf('?')) : location.pathname;
        query_string = (location.search) ? ((location.search.indexOf('#') != -1) ? location.search.substring(1, location.search.indexOf('#')) : location.search.substring(1)) : '';
        /* host_and_path_info = document.referrer; */
   /*     largo = host.length+path_info.length+query_string.length;
        /*
		 * alert('Host='+host); alert('Path_info='+path_info);
		 * alert('Query_string='+query_string); alert('Largo='+largo);
		 */
  /*      if ( largo > 92 ) {
                location.href=url;
        }
}

function checkCarnet(){
	var carnet = document.getElementById('username');
	var filter = /^[0-9]{2}-[0-9]{4,6}$/;
	if (filter.test(carnet.value) ){
		document.formcarnet.submit();
	} else {
  		alert("Carnet invalido");
	}
}

function checkEmail(email){
	var filter=/^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i
	return (filter.test(email));
}
function checkCedula(cedula){
	var filter=/^\d+$/;
	return (filter.test(cedula));
}

function checkPersonales() {
	  var ape = document.getElementById('apellidos');
	  var nom = document.getElementById('nombres');
	  var cid = document.getElementById('ci');
	  var tlh = document.getElementById('tlfhab');
	  var tlc = document.getElementById('tlfcel');
	  var ema = document.getElementById('email');
	  // alert('QWERTYFULL');
	  if (	ape.value != "" &&
			nom.value != "" &&
			cid.value != "" &&
			tlh.value != "" &&
			tlc.value != "" &&
			ema.value != "" ){
		  	if (checkEmail(ema.value)){
		  		if (checkCedula(cid.value)){
		  			document.formpersonales.submit();
		  		} else {
			  		alert("Cedula de identidad invalida")
			  	}	
		  	} else {
		  		alert("Direccion email invalida!")
		  	}
	} else {
		alert('Existen Campos Obligatorios en blanco');
	}
}

function checkAcademicas(){
	var indice = document.getElementById('indice');
	  var filter=/^\d+.\d+$/;
	  if (filter.test(indice.value)){
	  		document.formacademicas.submit();
	  	} else {
	  		alert("Indice invalido!");
	  }
}

function checkLaborales() {
/*	  var emp = document.getElementById('empresa');
	  var car = document.getElementById('cargo');
	  var are = document.getElementById('area');
	  // alert('QWERTYFULL');
	  if (	emp.value != "" &&
			car.value != "" &&
			are.value != "" &&){
		  			document.formlaborales.submit();
	   } else {
		   alert('Existen Campos Obligatorios en blanco');
	   }
	   */
	/*	document.formlaborales.submit();
}


function revisar() {
  var cnl = document.getElementById('cn1');
  var cn2 = document.getElementById('cn2');
  var ape = document.getElementById('apellidos');
  var nom = document.getElementById('nombres');
  var cid = document.getElementById('ci');
  var tlh = document.getElementById('tlfhab');
  var tlc = document.getElementById('tlfcel');
  var ema = document.getElementById('email');
  // alert('QWERTYFULL');
  if (	cn1.value != "" && 
		cn2.value != "" &&
		ape.value != "" &&
		nom.value != "" &&
		cid.value != "" &&
		tlh.value != "" &&
		tlc.value != "" &&
		ema.value != "" ){
		document.form_egresados.submit();
   } else {
		      alert('Existen Campos Obligatorios en blanco');
   }
}

function seleccionar(input,output) {

	var ok = document.getElementsByName(output).item(0);	
	var chkdesc = document.getElementsByName(input).item(0);

	var act = chkdesc.checked;
	var check;

	if (act) {
		ok.style.visibility="visible";
	} else {
		ok.style.visibility="hidden";
	}
}

function addIdioma222(numStamps) {
	  var tbl = document.getElementById('idiomas');
	  var lastRow = tbl.rows.length;
	  // if there's no header row in the table, then iteration = lastRow + 1
	  var iteration = lastRow - numStamps;
	  var row = tbl.insertRow(lastRow);
	  var i=0;
	  row.insertCell(0);

	  for (i=0;i<4;i++) {
	      var cellRight = row.insertCell(i);
	      var el = document.createElement('input');
	      el.type = 'text';
	      el.name = 'table' + iteration+""+i;
	      el.id = 'table' + iteration+""+i;
	      el.size = 10;
	      cellRight.appendChild(el);  
	  }
	  
	var s1 = document.getElementsByName("remove").item(0);
	var ok = document.getElementsByName("ok").item(0);
	s1.style.visibility="visible";
	ok.style.visibility="visible";
}

function dropIdioma(ids){ 
	var tbl = document.getElementById('idiomas');
	var lastRow = tbl.rows.length; 
	if (lastRow - ids >1){		
	lastRow--; 
	tbl.deleteRow(lastRow);
	}
};

function addIdioma(numIds) {
	  var tbl = document.getElementById('idiomas');
	  var lastRow = tbl.rows.length;
	  // if there's no header row in the table, then iteration = lastRow + 1
	  var row = tbl.insertRow(lastRow);
	  var i=0;
	  row.insertCell(0);
	  var iteration = lastRow - (numIds + 1);
		  
      var cellRight = row.insertCell(i);
      var el = document.createElement('input');
      el.type = 'text';
      el.name = 'idioma' + iteration;
      el.id   = 'idioma' + iteration;
      el.size = 10;
      cellRight.appendChild(el);  
      for (i = 1; i < 4; i++) {
    	  cellRight = row.insertCell(i);
    	  myselect = document.createElement("select");
    	  myselect.name = 'idioma' + iteration+"-"+i;
    	  myselect.id   = 'idioma' + iteration+"-"+i;
          	
    	  	theOption=document.createElement("OPTION");
			theText=document.createTextNode("Ninguno");
			theOption.appendChild(theText);
			theOption.setAttribute("value","1");
			myselect.appendChild(theOption);
			theOption=document.createElement("OPTION");
	
			theText=document.createTextNode("Poco");
			theOption.appendChild(theText);
			theOption.setAttribute("value","2");
			myselect.appendChild(theOption);
			
			theOption=document.createElement("OPTION");
			theText=document.createTextNode("Regular");
			theOption.appendChild(theText);
			theOption.setAttribute("value","3");
			myselect.appendChild(theOption);
			
			theOption=document.createElement("OPTION");
			theText=document.createTextNode("Bueno");
			theOption.appendChild(theText);
			theOption.setAttribute("value","4");
			myselect.appendChild(theOption);
			
			theOption=document.createElement("OPTION");
			theText=document.createTextNode("Excelente");
			theOption.appendChild(theText);
			theOption.setAttribute("value","5");
		  
		  myselect.appendChild(theOption);
		  cellRight.appendChild(myselect);		
      }		
		
	//	alert('HelloU');
		
		
		
		/*mybutton.onclick=myOnClick;
		mybutton.style.height=20;
		mybutton.style.width=75;
		theText=document.createTextNode("Click Me");
		mybutton.appendChild(theText);
		myform.appendChild(mybutton);
		myselect.setAttribute("bgColor","red");
		myselect.style.color="green";
		myselect.setAttribute("border","10px");
		myselect.style.fontWeight="bold";
		myselect.setAttribute("id","selectID");
		myform.setAttribute("id","formID");
	//	btnDelete=document.getElementById("deleteID");
//		btnDelete.disabled=false;
		btnCreate=document.getElementById("createID");
		btnCreate.disabled=true;*//*
	}

function addAcademica(numIds) {
	  var tbl = document.getElementById('academicas');
	  var lastRow = tbl.rows.length;
	  // if there's no header row in the table, then iteration = lastRow + 1
	  var row = tbl.insertRow(lastRow);
	  
	var iteration = (lastRow )/2 ;
    var cellRight = row.insertCell(0);
// alert(iteration);
    myselect = document.createElement("select");
	myselect.name = 'tipo' + iteration;
	myselect.id   = 'tipo' + iteration;
	
		theOption=document.createElement("OPTION");
		theText=document.createTextNode("Congreso");
		theOption.appendChild(theText);
		theOption.setAttribute("value","Congreso");
		myselect.appendChild(theOption);
		
		theOption=document.createElement("OPTION");
		theText=document.createTextNode("Curso");
		theOption.appendChild(theText);
		theOption.setAttribute("value","Curso");
		myselect.appendChild(theOption);
		
      	theOption=document.createElement("OPTION");
		theText=document.createTextNode("Pasantía Corta");
		theOption.appendChild(theText);
		theOption.setAttribute("value","Pasantía Corta");
		myselect.appendChild(theOption);
  		
		theOption=document.createElement("OPTION");
		theText=document.createTextNode("Pasantía Larga");
		theOption.appendChild(theText);
		theOption.setAttribute("value","Pasantía Larga");
		myselect.appendChild(theOption);
  		
		theOption=document.createElement("OPTION");
		theText=document.createTextNode("Taller");
		theOption.appendChild(theText);
		theOption.setAttribute("value","Taller");
		myselect.appendChild(theOption);
  		
		theOption=document.createElement("OPTION");
		theText=document.createTextNode("Tesis");
		theOption.appendChild(theText);
		theOption.setAttribute("value","Tesis");
		myselect.appendChild(theOption);
		
		theText=document.createTextNode("Tipo");
		bold = document.createElement("b");
		bold.appendChild(theText);
		cellRight.appendChild(bold);
		cellRight.appendChild(document.createElement('br'));
    cellRight.appendChild(myselect);		
    cellRight.rowSpan = 2;		
    
    
    cellRight = row.insertCell(1);
    el = document.createElement('input');
    el.type = 'text';
    el.name = 'titulo' + iteration;
    el.id   = 'titulo' + iteration;

	theText=document.createTextNode("Titulo");
	bold = document.createElement("b");
	bold.appendChild(theText);
	cellRight.appendChild(bold);
	cellRight.appendChild(document.createElement('br'));
    cellRight.appendChild(el);  
    
    myselect = document.createElement("select");
	myselect.name = 'anio' + iteration;
	myselect.id   = 'anio' + iteration;
	cellRight = row.insertCell(2);  
    for (i = 1990; i < 2011; i++) {
  	  	theOption=document.createElement("OPTION");
		theText=document.createTextNode(i);
		theOption.appendChild(theText);
		theOption.setAttribute("value",i);
		myselect.appendChild(theOption);
    }
	theText=document.createTextNode("Año");
	bold = document.createElement("b");
	bold.appendChild(theText);
	cellRight.appendChild(bold);
	cellRight.appendChild(document.createElement('br'));
    cellRight.appendChild(myselect);		
    			 
    cellRight = row.insertCell(3);
    el = document.createElement('input');
    el.type = 'text';
    el.name = 'lugar' + iteration;
    el.id   = 'lugar' + iteration;
    
	theText=document.createTextNode("Lugar");
	bold = document.createElement("b");
	bold.appendChild(theText);
	cellRight.appendChild(bold);
	cellRight.appendChild(document.createElement('br'));
    cellRight.appendChild(el);  

    row = tbl.insertRow(lastRow+1);
    cellRight = row.insertCell(0);
    el = document.createElement('input');
    el.type = 'text';
    el.name = 'descripcion' + iteration;
    el.id   = 'descripcion' + iteration;
    el.size = 45;
	theText=document.createTextNode("Descripcion");
	bold = document.createElement("b");
	bold.appendChild(theText);
	cellRight.appendChild(bold);
	cellRight.appendChild(el);
	cellRight.colSpan = 3;
}


function dropAcademica(ids){ 
	var tbl = document.getElementById('academicas');
	var lastRow = tbl.rows.length; 
	if (lastRow - 2*ids >1){		
		lastRow--; 
		tbl.deleteRow(lastRow);
		lastRow--;
		tbl.deleteRow(lastRow);
	}
};

function addLaboral(numIds) {
	var tbl = document.getElementById('laborales');
	var lastRow = tbl.rows.length;
	  // if there's no header row in the table, then iteration = lastRow + 1
	var row = tbl.insertRow(lastRow);
	var iteration = lastRow/2 ;
	var cellRight = row.insertCell(0);
	//	alert(iteration);
		el = document.createElement('input');
		el.type = 'text';
		el.name = 'empresa' + iteration;
		el.id   = 'empresa' + iteration;
		el.size = 15;
		
		theText=document.createTextNode("Empresa");
		bold = document.createElement("b");
		bold.appendChild(theText);
		cellRight.appendChild(bold);
		cellRight.appendChild(document.createElement('br'));
		cellRight.appendChild(el);		
		cellRight.rowSpan = 2;		
  
	cellRight = row.insertCell(1);
		el = document.createElement('input');
		el.type = 'text';
		el.name = 'cargo' + iteration;
		el.id   = 'cargo' + iteration;

		theText=document.createTextNode("Cargo Ocupado");
		bold = document.createElement("b");
		bold.appendChild(theText);
		cellRight.appendChild(bold);
		cellRight.appendChild(document.createElement('br'));
		cellRight.appendChild(el);  
	
	cellRight = row.insertCell(2);
		myselect = document.createElement("select");
		myselect.name = 'anio' + iteration;
		myselect.id   = 'anio' + iteration;
	  
		for (i = 1990; i < 2011; i++) {
			theOption=document.createElement("OPTION");
			theText=document.createTextNode(i);
			theOption.appendChild(theText);
			theOption.setAttribute("value",i);
			myselect.appendChild(theOption);
		}
		theText=document.createTextNode("Año");
		bold = document.createElement("b");
		bold.appendChild(theText);
		cellRight.appendChild(bold);
		cellRight.appendChild(document.createElement('br'));
		cellRight.appendChild(myselect);		
  			 
	cellRight = row.insertCell(3);
  		el = document.createElement('input');
  		el.type = 'text';
  		el.name = 'area' + iteration;
  		el.id   = 'area' + iteration;
  
  		theText=document.createTextNode("Área");
  		bold = document.createElement("b");
  		bold.appendChild(theText);
  		cellRight.appendChild(bold);
  		cellRight.appendChild(document.createElement('br'));
  		cellRight.appendChild(el);  

  	row = tbl.insertRow(lastRow+1);
  	cellRight = row.insertCell(0);
  		el = document.createElement('input');
  		el.type = 'text';
  		el.name = 'descripcion' + iteration;
  		el.id   = 'descripcion' + iteration;
  		el.size = 43;
  		theText=document.createTextNode("Descripcion");
  		bold = document.createElement("b");
  		bold.appendChild(theText);
  		cellRight.appendChild(bold);
  		cellRight.appendChild(el);
  		cellRight.colSpan = 3;
}


function dropLaboral(ids){ 
	var tbl = document.getElementById('laborales');
	var lastRow = tbl.rows.length; 
	if (lastRow - 2*ids > 1){		
	lastRow--; 
	tbl.deleteRow(lastRow);
	lastRow--;
	tbl.deleteRow(lastRow);
	}
};

////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
//Tigra Calendar v4.0.3 (01/12/2009) American (mm/dd/yyyy)
//http://www.softcomplex.com/products/tigra_calendar/
//Public Domain Software... You're welcome.

//default settins

var A_TCALDEF = {
		'months' : ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
		'weekdays' : ['do', 'lu', 'ma', 'mi', 'ju', 'vi', 'sa'],
		'yearscroll': true,
		'weekstart': 0,
		'centyear'  : 70,
		'imgpath' : 'public/tigra_calendar/img/'
}
//date parsing function
function f_tcalParseDate (s_date) {

	var re_date = /^\s*(\d{1,2})\/(\d{1,2})\/(\d{2,4})\s*$/;
	if (!re_date.exec(s_date))
		return alert ("Invalid date: '" + s_date + "'.\nAccepted format is mm/dd/yyyy.")
	var n_day = Number(RegExp.$2),
		n_month = Number(RegExp.$1),
		n_year = Number(RegExp.$3);
	
	if (n_year < 100)
		n_year += (n_year < this.a_tpl.centyear ? 2000 : 1900);
	if (n_month < 1 || n_month > 12)
		return alert ("Invalid month value: '" + n_month + "'.\nAllowed range is 01-12.");
	var d_numdays = new Date(n_year, n_month, 0);
	if (n_day > d_numdays.getDate())
		return alert("Invalid day of month value: '" + n_day + "'.\nAllowed range for selected month is 01 - " + d_numdays.getDate() + ".");

	return new Date (n_year, n_month - 1, n_day);
}
//date generating function
function f_tcalGenerDate (d_date) {
	return (
		 (d_date.getMonth() < 9 ? '0' : '') + (d_date.getMonth() + 1) + "/"
		+ (d_date.getDate() < 10 ? '0' : '') + d_date.getDate() + "/"
		+ d_date.getFullYear()
	);
}

//implementation
function tcal (a_cfg, a_tpl) {

	// apply default template if not specified
	if (!a_tpl)
		a_tpl = A_TCALDEF;

	// register in global collections
	if (!window.A_TCALS)
		window.A_TCALS = [];
	if (!window.A_TCALSIDX)
		window.A_TCALSIDX = [];
	
	this.s_id = a_cfg.id ? a_cfg.id : A_TCALS.length;
	window.A_TCALS[this.s_id] = this;
	window.A_TCALSIDX[window.A_TCALSIDX.length] = this;
	
	// assign methods
	this.f_show = f_tcalShow;
	this.f_hide = f_tcalHide;
	this.f_toggle = f_tcalToggle;
	this.f_update = f_tcalUpdate;
	this.f_relDate = f_tcalRelDate;
	this.f_parseDate = f_tcalParseDate;
	this.f_generDate = f_tcalGenerDate;
	
	// create calendar icon
	this.s_iconId = 'tcalico_' + this.s_id;
	this.e_icon = f_getElement(this.s_iconId);
	if (!this.e_icon) {
		document.write('<img src="' + a_tpl.imgpath + 'cal.gif" id="' + this.s_iconId + '" onclick="A_TCALS[\'' + this.s_id + '\'].f_toggle()" class="tcalIcon" alt="Open Calendar" />');
		this.e_icon = f_getElement(this.s_iconId);
	}
	// save received parameters
	this.a_cfg = a_cfg;
	this.a_tpl = a_tpl;
}

function f_tcalShow (d_date) {

	// find input field
	if (!this.a_cfg.controlname)
		throw("TC: control name is not specified");
	if (this.a_cfg.formname) {
		var e_form = document.forms[this.a_cfg.formname];
		if (!e_form)
			throw("TC: form '" + this.a_cfg.formname + "' can not be found");
		this.e_input = e_form.elements[this.a_cfg.controlname];
	}
	else
		this.e_input = f_getElement(this.a_cfg.controlname);

	if (!this.e_input || !this.e_input.tagName || this.e_input.tagName != 'INPUT')
		throw("TC: element '" + this.a_cfg.controlname + "' does not exist in "
			+ (this.a_cfg.formname ? "form '" + this.a_cfg.controlname + "'" : 'this document'));

	// dynamically create HTML elements if needed
	this.e_div = f_getElement('tcal');
	if (!this.e_div) {
		this.e_div = document.createElement("DIV");
		this.e_div.id = 'tcal';
		document.body.appendChild(this.e_div);
	}
	this.e_shade = f_getElement('tcalShade');
	if (!this.e_shade) {
		this.e_shade = document.createElement("DIV");
		this.e_shade.id = 'tcalShade';
		document.body.appendChild(this.e_shade);
	}
	this.e_iframe =  f_getElement('tcalIF')
	if (b_ieFix && !this.e_iframe) {
		this.e_iframe = document.createElement("IFRAME");
		this.e_iframe.style.filter = 'alpha(opacity=0)';
		this.e_iframe.id = 'tcalIF';
		this.e_iframe.src = this.a_tpl.imgpath + 'pixel.gif';
		document.body.appendChild(this.e_iframe);
	}
	
	// hide all calendars
	f_tcalHideAll();

	// generate HTML and show calendar
	this.e_icon = f_getElement(this.s_iconId);
	if (!this.f_update())
		return;

	this.e_div.style.visibility = 'visible';
	this.e_shade.style.visibility = 'visible';
	if (this.e_iframe)
		this.e_iframe.style.visibility = 'visible';

	// change icon and status
	this.e_icon.src = this.a_tpl.imgpath + 'no_cal.gif';
	this.e_icon.title = 'Close Calendar';
	this.b_visible = true;
}

function f_tcalHide (n_date) {
	if (n_date)
		this.e_input.value = this.f_generDate(new Date(n_date));

	// no action if not visible
	if (!this.b_visible)
		return;

	// hide elements
	if (this.e_iframe)
		this.e_iframe.style.visibility = 'hidden';
	if (this.e_shade)
		this.e_shade.style.visibility = 'hidden';
	this.e_div.style.visibility = 'hidden';
	
	// change icon and status
	this.e_icon = f_getElement(this.s_iconId);
	this.e_icon.src = this.a_tpl.imgpath + 'cal.gif';
	this.e_icon.title = 'Open Calendar';
	this.b_visible = false;
}

function f_tcalToggle () {
	return this.b_visible ? this.f_hide() : this.f_show();
}

function f_tcalUpdate (d_date) {
	
	var d_today = this.a_cfg.today ? this.f_parseDate(this.a_cfg.today) : f_tcalResetTime(new Date());
	var d_selected = this.e_input.value == ''
		? (this.a_cfg.selected ? this.f_parseDate(this.a_cfg.selected) : d_today)
		: this.f_parseDate(this.e_input.value);

	// figure out date to display
	if (!d_date)
		// selected by default
		d_date = d_selected;
	else if (typeof(d_date) == 'number')
		// get from number
		d_date = f_tcalResetTime(new Date(d_date));
	else if (typeof(d_date) == 'string')
		// parse from string
		this.f_parseDate(d_date);
		
	if (!d_date) return false;

	// first date to display
	var d_firstday = new Date(d_date);
	d_firstday.setDate(1);
	d_firstday.setDate(1 - (7 + d_firstday.getDay() - this.a_tpl.weekstart) % 7);
	
	var a_class, s_html = '<table class="ctrl"><tbody><tr>'
		+ (this.a_tpl.yearscroll ? '<td' + this.f_relDate(d_date, -1, 'y') + ' title="Previous Year"><img src="' + this.a_tpl.imgpath + 'prev_year.gif" /></td>' : '')
		+ '<td' + this.f_relDate(d_date, -1) + ' title="Previous Month"><img src="' + this.a_tpl.imgpath + 'prev_mon.gif" /></td><th>'
		+ this.a_tpl.months[d_date.getMonth()] + ' ' + d_date.getFullYear()
			+ '</th><td' + this.f_relDate(d_date, 1) + ' title="Next Month"><img src="' + this.a_tpl.imgpath + 'next_mon.gif" /></td>'
		+ (this.a_tpl.yearscroll ? '<td' + this.f_relDate(d_date, 1, 'y') + ' title="Next Year"><img src="' + this.a_tpl.imgpath + 'next_year.gif" /></td></td>' : '')
		+ '</tr></tbody></table><table><tbody><tr class="wd">';

	// print weekdays titles
	for (var i = 0; i < 7; i++)
		s_html += '<th>' + this.a_tpl.weekdays[(this.a_tpl.weekstart + i) % 7] + '</th>';
	s_html += '</tr>' ;

	// print calendar table
	var n_date, n_month, d_current = new Date(d_firstday);
	while (d_current.getMonth() == d_date.getMonth() ||
		d_current.getMonth() == d_firstday.getMonth()) {
	
		// print row heder
		s_html +='<tr>';
		for (var n_wday = 0; n_wday < 7; n_wday++) {

			a_class = [];
			n_date  = d_current.getDate();
			n_month = d_current.getMonth();

			// other month
			if (d_current.getMonth() != d_date.getMonth())
				a_class[a_class.length] = 'othermonth';
			// weekend
			if (d_current.getDay() == 0 || d_current.getDay() == 6)
				a_class[a_class.length] = 'weekend';
			// today
			if (d_current.valueOf() == d_today.valueOf())
				a_class[a_class.length] = 'today';
			// selected
			if (d_current.valueOf() == d_selected.valueOf())
				a_class[a_class.length] = 'selected';

			s_html += '<td onclick="A_TCALS[\'' + this.s_id + '\'].f_hide(' + d_current.valueOf() + ')"' + (a_class.length ? ' class="' + a_class.join(' ') + '">' : '>') + n_date + '</td>'

			d_current.setDate(++n_date);
			while (d_current.getDate() != n_date && d_current.getMonth() == n_month) {
				d_current.setHours(d_current.getHours + 1);
				d_current = f_tcalResetTime(d_current);
			}
		}
		// print row footer
		s_html +='</tr>';
	}
	s_html +='</tbody></table>';
	
	// update HTML, positions and sizes
	this.e_div.innerHTML = s_html;

	var n_width  = this.e_div.offsetWidth;
	var n_height = this.e_div.offsetHeight;
	var n_top  = f_getPosition (this.e_icon, 'Top') + this.e_icon.offsetHeight;
	var n_left = f_getPosition (this.e_icon, 'Left') - n_width + this.e_icon.offsetWidth;
	if (n_left < 0) n_left = 0;
	
	this.e_div.style.left = n_left + 'px';
	this.e_div.style.top  = n_top + 'px';

	this.e_shade.style.width = (n_width + 8) + 'px';
	this.e_shade.style.left = (n_left - 1) + 'px';
	this.e_shade.style.top = (n_top - 1) + 'px';
	this.e_shade.innerHTML = b_ieFix
		? '<table><tbody><tr><td rowspan="2" colspan="2" width="6"><img src="' + this.a_tpl.imgpath + 'pixel.gif"></td><td width="7" height="7" style="filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src=\'' + this.a_tpl.imgpath + 'shade_tr.png\', sizingMethod=\'scale\');"><img src="' + this.a_tpl.imgpath + 'pixel.gif"></td></tr><tr><td height="' + (n_height - 7) + '" style="filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src=\'' + this.a_tpl.imgpath + 'shade_mr.png\', sizingMethod=\'scale\');"><img src="' + this.a_tpl.imgpath + 'pixel.gif"></td></tr><tr><td width="7" style="filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src=\'' + this.a_tpl.imgpath + 'shade_bl.png\', sizingMethod=\'scale\');"><img src="' + this.a_tpl.imgpath + 'pixel.gif"></td><td style="filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src=\'' + this.a_tpl.imgpath + 'shade_bm.png\', sizingMethod=\'scale\');" height="7" align="left"><img src="' + this.a_tpl.imgpath + 'pixel.gif"></td><td style="filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src=\'' + this.a_tpl.imgpath + 'shade_br.png\', sizingMethod=\'scale\');"><img src="' + this.a_tpl.imgpath + 'pixel.gif"></td></tr><tbody></table>'
		: '<table><tbody><tr><td rowspan="2" width="6"><img src="' + this.a_tpl.imgpath + 'pixel.gif"></td><td rowspan="2"><img src="' + this.a_tpl.imgpath + 'pixel.gif"></td><td width="7" height="7"><img src="' + this.a_tpl.imgpath + 'shade_tr.png"></td></tr><tr><td background="' + this.a_tpl.imgpath + 'shade_mr.png" height="' + (n_height - 7) + '"><img src="' + this.a_tpl.imgpath + 'pixel.gif"></td></tr><tr><td><img src="' + this.a_tpl.imgpath + 'shade_bl.png"></td><td background="' + this.a_tpl.imgpath + 'shade_bm.png" height="7" align="left"><img src="' + this.a_tpl.imgpath + 'pixel.gif"></td><td><img src="' + this.a_tpl.imgpath + 'shade_br.png"></td></tr><tbody></table>';
	
	if (this.e_iframe) {
		this.e_iframe.style.left = n_left + 'px';
		this.e_iframe.style.top  = n_top + 'px';
		this.e_iframe.style.width = (n_width + 6) + 'px';
		this.e_iframe.style.height = (n_height + 6) +'px';
	}
	return true;
}

function f_getPosition (e_elemRef, s_coord) {
	var n_pos = 0, n_offset,
		e_elem = e_elemRef;

	while (e_elem) {
		n_offset = e_elem["offset" + s_coord];
		n_pos += n_offset;
		e_elem = e_elem.offsetParent;
	}
	// margin correction in some browsers
	if (b_ieMac)
		n_pos += parseInt(document.body[s_coord.toLowerCase() + 'Margin']);
	else if (b_safari)
		n_pos -= n_offset;
	
	e_elem = e_elemRef;
	while (e_elem != document.body) {
		n_offset = e_elem["scroll" + s_coord];
		if (n_offset && e_elem.style.overflow == 'scroll')
			n_pos -= n_offset;
		e_elem = e_elem.parentNode;
	}
	return n_pos;
}

function f_tcalRelDate (d_date, d_diff, s_units) {
	var s_units = (s_units == 'y' ? 'FullYear' : 'Month');
	var d_result = new Date(d_date);
	d_result['set' + s_units](d_date['get' + s_units]() + d_diff);
	if (d_result.getDate() != d_date.getDate())
		d_result.setDate(0);
	return ' onclick="A_TCALS[\'' + this.s_id + '\'].f_update(' + d_result.valueOf() + ')"';
}

function f_tcalHideAll () {
	for (var i = 0; i < window.A_TCALSIDX.length; i++)
		window.A_TCALSIDX[i].f_hide();
}

function f_tcalResetTime (d_date) {
	d_date.setHours(0);
	d_date.setMinutes(0);
	d_date.setSeconds(0);
	d_date.setMilliseconds(0);
	return d_date;
}

f_getElement = document.all ?
	function (s_id) { return document.all[s_id] } :
	function (s_id) { return document.getElementById(s_id) };

if (document.addEventListener)
	window.addEventListener('scroll', f_tcalHideAll, false);
if (window.attachEvent)
	window.attachEvent('onscroll', f_tcalHideAll);
	
//global variables
var s_userAgent = navigator.userAgent.toLowerCase(),
	re_webkit = /WebKit\/(\d+)/i;
var b_mac = s_userAgent.indexOf('mac') != -1,
	b_ie5 = s_userAgent.indexOf('msie 5') != -1,
	b_ie6 = s_userAgent.indexOf('msie 6') != -1 && s_userAgent.indexOf('opera') == -1;
var b_ieFix = b_ie5 || b_ie6,
	b_ieMac  = b_mac && b_ie5,
	b_safari = b_mac && re_webkit.exec(s_userAgent) && Number(RegExp.$1) < 500;






function asd(){
	new tcal ({
		// if referenced by ID then form name is not required
		'controlname': 'myOtherInput'
	}, A_CALTPL);
};

var N_CALNUM = 1;
function f_createContent() {
	var e_div = f_getElement('container');
	e_div.innerHTML +=
		 '<input type="text"  name="testinput' + N_CALNUM + '" value="" />'
		+ '<img title="Open Calendar" class="tcalIcon" onclick="A_TCALS[\'myCalID' + N_CALNUM + '\'].f_toggle()" id="tcalico_myCalID' + N_CALNUM + '" src="img/cal.gif"/><br />';

	new tcal ({
		// form name
		'formname': 'testform',
		// input name
		'controlname': 'testinput' + N_CALNUM,
		// set unique ID to identify the elements
		'id': 'myCalID' + N_CALNUM
	});
	
	N_CALNUM++;
}
function f_removeContent() {
	var e_div = f_getElement('container');
	e_div.innerHTML = '';
	window.A_TCALS = null;
	window.A_TCALSIDX = null;
	N_CALNUM = 1;
}

function crearFechas() {
	N_CALNUM = 1;
	var e_div = f_getElement('container');
	e_div.innerHTML =
		 'Fecha de inicio: <input type="text" readonly="TRUE" name="testinput' + N_CALNUM + '"  />'
		+ '<img title="Open Calendar" class="tcalIcon" onclick="A_TCALS[\'myCalID' + N_CALNUM + '\'].f_toggle()" id="tcalico_myCalID' + N_CALNUM + '" src="public/tigra_calendar/img/cal.gif"/><br />';

	new tcal ({
		// form name
		'formname': 'updactividades',
		// input name
		'controlname': 'testinput' + N_CALNUM,
		// set unique ID to identify the elements
		'id': 'myCalID' + N_CALNUM
	});
	N_CALNUM++;
	e_div.innerHTML +=
		 'Fecha de cierre: <input type="text"  readonly="TRUE" name="testinput' + N_CALNUM + '"  />'
		+ '<img title="Open Calendar" class="tcalIcon" onclick="A_TCALS[\'myCalID' + N_CALNUM + '\'].f_toggle()" id="tcalico_myCalID' + N_CALNUM + '" src="public/tigra_calendar/img/cal.gif"/><br />';
	
	new tcal ({
		// form name
		'formname': 'updactividades',
		// input name
		'controlname': 'testinput' + N_CALNUM,
		// set unique ID to identify the elements
		'id': 'myCalID' + N_CALNUM
	});
	var tbl = document.getElementById('horario');
	tbl.style.visibility="visible";

}

function crearHorario(nbloques) {
	var tbl = document.getElementById('horario');
	var bloques = document.getElementById('bloques').value;
	var size = tbl.rows.length; // if there's no header row in the table, then
	if (bloques < nbloques){
		alert("Numero invalido de bloques");
	} else {
		var i=0; 
		var length = bloques - size;
		var dias = ["lunes", "martes", "miercoles", "jueves", "viernes"];
		var j = 0;
		
		if (bloques<size ){
			for (i=size-1; i>bloques; i--){
				tbl.deleteRow(i);
			}
		} else {
			for ( i = size; i <= bloques; i++){
				var row = tbl.insertRow(i); 
				var cellRight = row.insertCell(0); 
				var theText = document.createTextNode("Bloque "+i);
				bold = document.createElement("b");
				bold.appendChild(theText);
				cellRight.appendChild(bold);
				for (j=0 ;j<5 ;j++) { 
					var cellRight = row.insertCell(j+1); 
					var elem = document.createElement('input'); 
					elem.type = 'text'; 
					elem.name = dias[j]+i;
					elem.size = 8;
					elem.id = dias[j]+i;
					cellRight.appendChild(elem);
				} 
			}
		}	
		
	}	
}

function revisarActividades() {
	  var bloques = document.getElementById('bloques');
	  var sesiones = document.getElementById('sesiones');
	 
	  if (	sesiones.value != "" &&
			bloques.value != "" ){
		   
			document.updactividades.submit();
	   } else {
			      alert('Existen Campos Obligatorios en blanco');
	   }
	   
	}

function estadisticas(pagina,container){
	var a = document.getElementById('anio');
	//var t = document.getElementById('trimestre');
	var t = document.getElementById('trimestre');
	var page = pagina+"?anio="+a.value+"&trimestre="+t.value;
	ajaxfade(page,container,'');
}
/*		

	if (lastRow - numStamps> 0) { 
		var s1 = document.getElementsByName("remove").item(0); 
		var ok =  document.getElementsByName("ok").item(0); 
		ok.style.visibility="visible";
		s1.style.visibility="visible";
	} else if (lastRow + images> numStamps) { 
		var s1 = document.getElementsByName("remove").item(0); 
		var ok = document.getElementsByName("ok").item(0); 
		ok.style.visibility="visible";
		s1.style.visibility="hidden"; 
	} else { var s1 =  document.getElementsByName("remove").item(0); 
		s1.style.visibility="hidden";
		var ok = document.getElementsByName("ok").item(0);
		try { 
			var chkdesc =  document.getElementsByName("chkdesc").item(0); 
			var act = chkdesc.checked; 
			var check; var j = 0;
			while (j+1<numStamps && !act) {
				check = document.getElementsByName("chk"+j).item(0);
				act = check.checked; j++;
			} if (act) { 
				ok.style.visibility="visible";
			} else { 
				ok.style.visibility="hidden";
			} 
		} catch (err){ 
			ok.style.visibility="hidden"; 
		}
	}
	*/


/*
 * function addImage(numStamps) { //obtener la tabla oculta var tbl =
 * document.getElementById('Images'); var lastRow = tbl.rows.length; // tam�o de
 * la tabla de imagenes var row = tbl.insertRow(lastRow); var nuevaFila =
 * row.insertCell(0); var examinar = document.createElement('input');
 * examinar.type = 'file'; examinar.name = 'Foto' + lastRow; examinar.id =
 * 'Foto' + lastRow; nuevaFila.appendChild(examinar); var s1 =
 * document.getElementsByName("dropImg").item(0); s1.style.visibility="visible";
 * var ok = document.getElementsByName("ok").item(0);
 * ok.style.visibility="visible"; }
 * 
 * function dropImage(numStamps) { var tbl = document.getElementById('Images');
 * var tb2 = document.getElementById('Stamps'); var stamps =
 * tb2.rows.length-numStamps; var lastRow = tbl.rows.length; lastRow--;
 * tbl.deleteRow(lastRow); if (lastRow > 0) { var s1 =
 * document.getElementsByName("dropImg").item(0); var ok =
 * document.getElementsByName("ok").item(0); ok.style.visibility="visible";
 * s1.style.visibility="visible"; } else if (lastRow + stamps> 0) { var s1 =
 * document.getElementsByName("dropImg").item(0); var ok =
 * document.getElementsByName("ok").item(0); ok.style.visibility="visible";
 * s1.style.visibility="hidden"; } else { var s1 =
 * document.getElementsByName("dropImg").item(0); s1.style.visibility="hidden";
 * var ok = document.getElementsByName("ok").item(0); try { var chkdesc =
 * document.getElementsByName("chkdesc").item(0); var act = chkdesc.checked; var
 * check; var j = 0; while (j+1<numStamps && !act) { check =
 * document.getElementsByName("chk"+j).item(0); act = check.checked; j++; } if
 * (act) { ok.style.visibility="visible"; } else { ok.style.visibility="hidden"; } }
 * catch (err){ ok.style.visibility="hidden"; } } }
 * 
 * 
 * 
 * 
 * function addStamp(numStamps) { var tbl = document.getElementById('Stamps');
 * var lastRow = tbl.rows.length; // if there's no header row in the table, then
 * iteration = lastRow + 1 var iteration = lastRow - numStamps; var row =
 * tbl.insertRow(lastRow); var i=0; row.insertCell(0);
 * 
 * for (i=1;i<4;i++) { var cellRight = row.insertCell(i); var el =
 * document.createElement('input'); el.type = 'text'; el.name = 'table' +
 * iteration+""+i; el.id = 'table' + iteration+""+i; el.size = 5;
 * cellRight.appendChild(el); } for (i=4;i<6;i++) { var cellRight =
 * row.insertCell(i); var el = document.createElement('input'); el.type =
 * 'text'; el.name = 'table' + iteration+""+i; el.id = 'table' + iteration+""+i;
 * el.size = 10; cellRight.appendChild(el); } i=6; var cellRight =
 * row.insertCell(i); var el = document.createElement('input'); el.type =
 * 'text'; el.name = 'table' + iteration+""+i; el.id = 'table' + iteration+""+i;
 * el.size = 2; cellRight.appendChild(el); i= 7; var cellRight =
 * row.insertCell(i); var el = document.createElement('input'); el.type =
 * 'text'; el.name = 'table' + iteration+""+i; el.id = 'table' + iteration+""+i;
 * el.size = 40; cellRight.appendChild(el); for (i=8;i<11;i++) { var cellRight =
 * row.insertCell(i); var el = document.createElement('input'); el.type =
 * 'text'; el.name = 'table' + iteration+""+i; el.id = 'table' + iteration+""+i;
 * el.size = 6; cellRight.appendChild(el); }
 * 
 * var s1 = document.getElementsByName("remove").item(0); var ok =
 * document.getElementsByName("ok").item(0); s1.style.visibility="visible";
 * ok.style.visibility="visible"; }
 * 
 * function dropStamp(numStamps) { var tbl = document.getElementById('Stamps');
 * var tb2 = document.getElementById('Images'); var images = tb2.rows.length;
 * var lastRow = tbl.rows.length; lastRow--; tbl.deleteRow(lastRow);
 * 
 * if (lastRow - numStamps> 0) { var s1 =
 * document.getElementsByName("remove").item(0); var ok =
 * document.getElementsByName("ok").item(0); ok.style.visibility="visible";
 * s1.style.visibility="visible"; } else if (lastRow + images> numStamps) { var
 * s1 = document.getElementsByName("remove").item(0); var ok =
 * document.getElementsByName("ok").item(0); ok.style.visibility="visible";
 * s1.style.visibility="hidden"; } else { var s1 =
 * document.getElementsByName("remove").item(0); s1.style.visibility="hidden";
 * var ok = document.getElementsByName("ok").item(0); try { var chkdesc =
 * document.getElementsByName("chkdesc").item(0); var act = chkdesc.checked; var
 * check; var j = 0; while (j+1<numStamps && !act) { check =
 * document.getElementsByName("chk"+j).item(0); act = check.checked; j++; } if
 * (act) { ok.style.visibility="visible"; } else { ok.style.visibility="hidden"; } }
 * catch (err){ ok.style.visibility="hidden"; } } }
 * 
 * function marcardesc( numStamps) { var tbl =
 * document.getElementById('Stamps'); var tb2 =
 * document.getElementById('Images'); var images = tb2.rows.length; var lastRow =
 * tbl.rows.length;
 * 
 * var ok = document.getElementsByName("ok").item(0); var check; var j = 0;
 * 
 * check = document.getElementsByName("chkdesc").item(0); act = check.checked;
 * 
 * if (lastRow + images> numStamps+1 ) { ok.style.visibility="visible"; } else {
 * while (j<numStamps && !act) { check =
 * document.getElementsByName("chk"+j).item(0); act = check.checked; j++; } if
 * (act) { ok.style.visibility="visible"; } else { ok.style.visibility="hidden"; } }
 * var desc = document.getElementsByName("descripcion").item(0);
 * 
 * desc.readOnly = !act ; }
 * 
 * function seleccionar(input,output) {
 * 
 * var ok = document.getElementsByName(output).item(0); var chkdesc =
 * document.getElementsByName(input).item(0);
 * 
 * var act = chkdesc.checked; var check;
 * 
 * if (act) { ok.style.visibility="visible"; } else {
 * ok.style.visibility="hidden"; } }
 * 
 * 
 * 
 * function marcar(i, numStamps) { var tbl = document.getElementById('Stamps');
 * var tb2 = document.getElementById('Images'); var images = tb2.rows.length;
 * var lastRow = tbl.rows.length; var ok =
 * document.getElementsByName("ok").item(0); var chkdesc =
 * document.getElementsByName("chkdesc").item(0); var act = chkdesc.checked; var
 * check; var j = 0;
 * 
 * if (lastRow + images> numStamps+1) { ok.style.visibility="visible"; } else {
 * while (j<numStamps && !act) { check =
 * document.getElementsByName("chk"+j).item(0); act = check.checked; j++; } if
 * (act) { ok.style.visibility="visible"; } else { ok.style.visibility="hidden"; } }
 * 
 * 
 * pmeri = document.getElementsByName("pmeri"+i).item(0); scott =
 * document.getElementsByName("scott"+i).item(0); blanco =
 * document.getElementsByName("blanco"+i).item(0); facial =
 * document.getElementsByName("facial"+i).item(0); descripcion =
 * document.getElementsByName("desc"+i).item(0); color =
 * document.getElementsByName("color"+i).item(0); dentado =
 * document.getElementsByName("dentado"+i).item(0); np =
 * document.getElementsByName("np"+i).item(0); nh =
 * document.getElementsByName("nh"+i).item(0); u =
 * document.getElementsByName("u"+i).item(0);
 * 
 * chk = document.getElementsByName("chk"+i).item(0); var bool =
 * !(pmeri.readOnly);
 * 
 * pmeri.readOnly = bool ; scott.readOnly = bool ; blanco.readOnly = bool ;
 * facial.readOnly = bool ; descripcion.readOnly = bool ; color.readOnly = bool ;
 * dentado.readOnly = bool ; np.readOnly = bool ; nh.readOnly = bool ;
 * u.readOnly = bool ; }
 * 
 * 
 * 
 * function elimImg(salida) { var answer = confirm("Desea eliminar esta
 * Imagen?") if (answer){ window.location = salida; } }
 * 
 * function elimStamp(salida) { var answer = confirm("Desea eliminar la
 * Estampilla Seleccionada?") if (answer){ window.location = salida; } }
 * 
 * function elimSerie(salida) { var answer = confirm("Desea eliminar esta
 * Serie?") if (answer){ window.location = salida; } }
 * 
 * function subir() { var answer = confirm("Desea Subir esta Serie?") if
 * (answer){ document.formulario.submit(); } }
 * 
 * function actualizar() { var answer = confirm("Desea Guardar los cambios a
 * esta Serie?") if (answer){ document.formStamp.submit(); } }
 * 
 * function preliminar() { mywindow = window.open
 * ("modulos/index.php","mywindow","location=1,status=1,scrollbars=1,width=1124,height=600");
 * mywindow.moveTo(0,0); }
 */

