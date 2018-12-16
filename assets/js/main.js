$(document).ready(function(){
  $('a[href*=#]').click(function() {
      var $target = $(this.hash);
        var targetOffset = $target.offset().top;
        $('html').animate({scrollTop: targetOffset}, 1000);
      });
    });
