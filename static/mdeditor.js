$(function(){

  // textareaに行番号を表示
  $('#md-area').linedtextarea();

  // Ctrl + Enterで送信
  $(window).keydown(function (e) {
    if ((e.keyCode == 10 || e.keyCode == 13) && e.ctrlKey) {
        $('#mainform').submit();
        return false;
    }
  });

  // Tabキーでスペース4個入力
  $('#md-area').keydown(function (e) {
    if (e.keyCode == 9) {
        var text = $('#md-area').val();
        $('#md-area').val(text + '\t');
        return false;
    }
  });

  // 送信後はtextareaにフォーカスし、最後の行にキャレットを移動
  if (location.search == '?mode=writing') {
    var text = $('#md-area').val();
    $('#md-area').val('');
    $('#md-area').focus().val(text);
  }

  // 保存ボタンを押すとプルダウンメニューをトグル
  $('#download').click(function(){
    $('#pulldown-menu').toggleClass('active');
  });

  // モーダル用変数
	var open = $('#help'),
  close = $('.modal-close'),
  container = $('.modal-container');

  //開くボタンをクリックしたらモーダルをトグル
  open.on('click',function(){	
    container.toggleClass('active');
    return false;
  });

  //モーダルの外側をクリックしたらモーダルを閉じる
  $(document).on('click',function(e) {
    if(!$(e.target).closest('.modal-body').length) {
      container.removeClass('active');
    }
  });

});  