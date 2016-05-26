$(document).ready(function(){
    // Initially hide stars in the technical skills
    // No UI to show this off - Only let the curious see my confidence.
    $('.tech').on({
        'mouseenter': function(e){
          var $stars = $(this).find('.stars');
          $stars.addClass('hidden');
        },
        'mouseleave': function(e){
          var leaveInterval = setInterval(function(){
            if (!$stars.hasClass('hidden')){
                $stars.removeClass('hidden');
                clearInterval(leaveInterval);
            }
          }, 100);
        }
    });

  // Easter egg if clicked enough.
  $('.tech').click(function(){
  var random = Math.random() * 1000;
  if (random > 999)
      window.open(''); // Haven't decided where to go yet.
    });

    // These are supposed to be really brief glimpses.
    // There is a link to a resume at the end for a reason.
    $('.experience').click(function(){
       $(this).find('.show-more').toggleClass('hidden');
    });
});
