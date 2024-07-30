var sketchProc = function (processingInstance) {
    with (processingInstance) {
        size(400, 400);
        frameRate(30);

        // ProgramCodeGoesHere
        
    }
};

var canvas = document.getElementById("mycanvas");
var processingInstance = new Processing(canvas, sketchProc);
canvas.focus();