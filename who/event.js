	$(document).ready(function() {
		
		function changeHeight() {
			if ($(window).height() < 839)
				{
					$("#footer").css("position","relative");
				}
				
				else {
					$("#footer").css("position","absolute");
				}
			};
			
			changeHeight();
				
	$(window).resize(function() {
		changeHeight();

	});
	
	$(window).scroll(function() {
	 if ($(this).scrollTop() < 30) {
		 $("#questionh1").fadeIn();
	 }
	 else{
		 $("#questionh1").fadeOut();
	 }
 });
 	
 	});



