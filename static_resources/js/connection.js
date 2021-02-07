// upload and receive id
function sendImage(){
  var formData = new FormData($('#imgForm').get(0));

  //画像処理してformDataに追加
  if ($("#canvas").length) {
      //canvasに描画したデータを取得
      var canvasImage = $("#canvas").get(0);
      //オリジナル容量(画質落としてない場合の容量)を取得
      var originalBinary = canvasImage.toDataURL("image/jpeg"); //画質落とさずバイナリ化
      var originalBlob = base64ToBlob(originalBinary); //オリジナル容量blobデータを取得
      console.log(originalBlob["size"]);
      //オリジナル容量blobデータをアップロード用blobに設定
      var uploadBlob = originalBlob;
      //オリジナル容量が2MB以上かチェック
      if(1000000 <= originalBlob["size"]) {
          //2MB以下に落とす
          var capacityRatio = 1000000 / originalBlob["size"];
          var processingBinary = canvasImage.toDataURL("image/jpeg", capacityRatio); //画質落としてバイナリ化
          uploadBlob = base64ToBlob(processingBinary); //画質落としたblobデータをアップロード用blobに設定
          console.log(capacityRatio);
          console.log(uploadBlob["size"]);
      }
      //アップロード用blobをformDataに追加
      formData.append("file", uploadBlob, 'catimg.jpeg');
  }

  $.ajax($(this).attr('action'), {
    url: '/api/detect_cat/image',
    type: 'post',
    processData: false,
    contentType: false,
    data: formData,
    success: console.log('send!')
  })
  .done(
      function(data){
        var responseJSON = data;
        $("#result").html(
            '<h2>猫の数:'+ responseJSON.cat_number + '匹</h2>' +
            '<img src="'+ responseJSON.encode_prefix + responseJSON.image_base64 +'" alt="" class="resultImage" border="0" />'
          );
        return false;
  })
  .fail(function(jqXHR, textStatus, errorThrown){
      $("#result").html( "<h2>ERROR:Link failed. please retry.</h2>");
      return false;
  });
  return false;
}

function canvasDraw() {
    var file = $("#file_button").prop("files")[0];

    //画像ファイルかチェック
    if (file["type"] != "image/jpeg" && file["type"] != "image/png" && file["type"] != "image/gif") {
        alert("画像ファイルを選択してください");
        $("#file_button").val(''); //選択したファイルをクリア

    } else {
        var fr = new FileReader();

        fr.onload = function() {
            //選択した画像を一旦imgタグに表示
            $("#preview").attr('src', fr.result);
                        
            //imgタグに表示した画像をimageオブジェクトとして取得
            var image = new Image();
            image.onload = function() { 
                //resize
                var w = 1920;
                var ratio = w / image.width;
                var h = image.height * ratio;

                //canvas
                var canvas = $("#canvas");
                var ctx = canvas[0].getContext('2d');
                $("#canvas").attr("width", w);
                $("#canvas").attr("height", h);
                ctx.drawImage(image, 0, 0, w, h);
            }
            image.src = $("#preview").attr('src');
        };

        fr.readAsDataURL(file);
    }
}

// 引数のBase64の文字列をBlob形式にする
function base64ToBlob(base64) {
    var base64Data = base64.split(',')[1], // Data URLからBase64のデータ部分のみを取得
          data = window.atob(base64Data), // base64形式の文字列をデコード
          buff = new ArrayBuffer(data.length),
          arr = new Uint8Array(buff),
          blob,
          i,
          dataLen;
    // blobの生成
    for (i = 0, dataLen = data.length; i < dataLen; i++) {
        arr[i] = data.charCodeAt(i);
    }
    blob = new Blob([arr], {type: 'image/jpeg'});
    return blob;
}