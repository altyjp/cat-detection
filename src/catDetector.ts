declare let cv: any;
declare const utils: any;

export function detectCat(imgDataElm : any, catCascadeFile : any) {

    let detector = new cv.CascadeClassifier();
    detector.load(catCascadeFile);
    let cats = new cv.RectVector();
    let imgData = cv.imread(imgDataElm);
    let msize = new cv.Size(100, 100);
    detector.detectMultiScale(imgData, cats, 1.1, 3, 0, msize, msize);

    for (let i =0; i < cats.size(); i++) {
        let point1 = new cv.Point(cats.get(i).x, cats.get(i).y);
        let point2 = new cv.Point(cats.get(i).x + cats.get(i).width, cats.get(i).y + cats.get(i).height);
        cv.rectangle(imgData, point1, point2, [255, 0, 0, 255]);
    }

    cv.imshow('preview', imgData);
    imgData.delete(); 
    detector.delete();
    cats.delete();

}
