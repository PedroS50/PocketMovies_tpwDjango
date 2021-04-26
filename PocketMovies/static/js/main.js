$(function(){
	$('.form-holder').delegate("input", "focus", function(){
		$('.form-holder').removeClass("active");
		$(this).parent().addClass("active");
	})
})

function toggleNav() {
	var nav = document.getElementById("sidemenu");
	var main = document.getElementById("main-page");
	var button = document.getElementById("sidebarCollapse");

	if ( nav.classList.contains("open") ) {
		nav.style.width = "0";
		main.style.marginLeft = "0";
		nav.classList.remove("open");
		button.classList.add("active");
	} else {
		nav.style.width = "250px";
		main.style.marginLeft = "250px";
		nav.classList.add("open");
		button.classList.remove("active");
	}
}
