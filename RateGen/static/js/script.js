jQuery(document).ready(function($){
  $('.btn-icon').on('click', function(event){
    event.preventDefault();
    $('.cd-panel-top').addClass('is-visible');
  });
  $('.cd-panel').on('click', function(event){
    if( $(event.target).is('.cd-panel') || $(event.target).is('.cd-panel-close') ) {
      $('.cd-panel').removeClass('is-visible');
      event.preventDefault();
    }
  });
});
