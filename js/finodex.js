$(document).ready(function(){
	$('.instructions').click(function(){
		$('#instructions-' + this.name).toggle(200);
		$(this).find('.glyphicon').toggleClass('glyphicon-menu-up')
	})

});
