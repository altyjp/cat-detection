const catDetector = require('./catDetector');

// upload and receive id
function sendImage(){
    catDetector.detectCat(document.getElementById("preview"), catCascadeFile);
    return false;
}
  
function canvasDraw() {
    var file = document.getElementById("file_button").files[0];

    //画像ファイルかチェック
    if (file["type"] != "image/jpeg" && file["type"] != "image/png" && file["type"] != "image/gif") {
        alert("画像ファイルを選択してください");
        document.getElementById("file_button").val(''); //選択したファイルをクリア

    } else {
        var fr = new FileReader();

        fr.onload = function() {
            //選択した画像を一旦imgタグに表示
            document.getElementById("preview").src = fr.result;
                        
            //imgタグに表示した画像をimageオブジェクトとして取得
            var image = new Image();
            image.onload = function() { 
                //resize
                var w = 1028;
                var ratio = w / image.width;
                var h = image.height * ratio;

                //canvas
                var canvas = document.getElementById("canvas");
                var ctx = canvas.getContext('2d');
                document.getElementById("canvas").width = w;
                document.getElementById("canvas").height = h;
                ctx.drawImage(image, 0, 0, w, h);
            }
            image.src = document.getElementById("preview").src;
        };

        fr.readAsDataURL(file);
    }
}


// Add event listener
const catCascadeFile = './model/cascade.xml';

window.onload = function() {
    let fileButton = document.getElementById("file_button");
    fileButton.addEventListener('change', canvasDraw);
    let submitButton = document.getElementById("submit_button");
    submitButton.addEventListener('click', sendImage);

    let utils = new Utils('errorMessage');
    utils.loadOpenCv(() => { 
        utils.createFileFromUrl(catCascadeFile, catCascadeFile, () => {
            document.getElementById("result").innerHTML = "Ready."
        });
    });

};