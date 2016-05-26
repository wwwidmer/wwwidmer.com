$(document).ready(function(){
    // Initially hide stars in the technical skills
    // No UI to show this off - Only let the curious see my confidence.
    $('.tech').on('mouseenter mouseout', function(e){
        var $stars = $(this).find('.stars');
        $stars.toggleClass('hidden');
        setTimeout(function(){
          $stars.fadeOut(400, function(){
              $stars.toggleClass();
          })
        }, 5000)
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
