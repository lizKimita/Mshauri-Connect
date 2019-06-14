$(function() {
	$('#carousel').carouFredSel({
		direction: 'up',
		items: 1,
		scroll: {
			fx: 'directscroll'
		},
		pagination: {
			container: '#pager',
			anchorBuilder: function( nr ) {
				return '<a href="#" class="thumb' + nr + '"><img src="' + this.src + '" width="50" /></a>';
			}
		}
	});
});
