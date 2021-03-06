$(document).ready(function(){
	jQuery('#camera_wrap').camera({
	loader: false,
	pagination: true ,
	minHeight: '394',
	thumbnails: false,
	height: '40.1875%',
	caption: false,
	navigation: false,
	fx: 'mosaic'
	});
	$().UItoTop({ easingType: 'easeOutQuart' });

})
(function(){
	function init() {
		var speed = 250,
		easing = mina.easeinout;
		[].slice.call ( document.querySelectorAll( '#grid > a' ) ).forEach( function( el ) {
		var s = Snap( el.querySelector( 'svg' ) ), path = s.select( 'path' ),
			pathConfig = {
			from : path.attr( 'd' ),
			to : el.getAttribute( 'data-path-hover' )
			};
		el.addEventListener( 'mouseenter', function() {
			path.animate( { 'path' : pathConfig.to }, speed, easing );
		} );
		el.addEventListener( 'mouseleave', function() {
			path.animate( { 'path' : pathConfig.from }, speed, easing );
		} );
		} );
	}
	init();
})();
$(function(){
  	SyntaxHighlighter.all();
	});
    $(window).load(function(){
      $('.flexslider').flexslider({
        animation: "slide",
        start: function(slider){
          $('body').removeClass('loading');
        }
    });
});
