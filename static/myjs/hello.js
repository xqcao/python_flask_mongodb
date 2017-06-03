$(function() {
  $('.btn').click(function() {
    var mydata = $('form').serialize();
    $.ajax({
      url: '/abc',
      data: $('form').serialize(),
      type: 'POST',
      success: function(res) {
        console.log(res);
        window.location.href = "/cctv";
      },
      error: function(err) {
        console.log('err :', err)
      }
    });
  });
});
