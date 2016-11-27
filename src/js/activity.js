document.addEventListener("DOMContentLoaded", function() {

    //check daily status... emo3 bad, not so good, emo2 middle, emo1 happy  all done)
    var progress = 0.7;
    if(progress>0.5)
        document.getElementById("imgHappy").src="images/emo2.svg";
    else if(progress>0.99)
        document.getElementById("imgHappy").src="images/emo2.svg";
    var el = document.querySelector('#infoHappy');
    el.innerHTML = "Today you have done "+(0.7)*100+"% of tasks!";
    var canvas = document.getElementById('canvas');
    var ctx = canvas.getContext('2d');
    if (canvas.getContext){
        var data = [0.7, 0.2, 0.4, 0.8, 1.0]
        var ctx = canvas.getContext('2d');

        var width = canvas.width;
        var height = canvas.height;
        var l = data.length;

        for (var index = 0; index < data.length; ++index) {
            //console.log(a[index]);
            ctx.fillStyle = "rgba(138, 195,73, 0.8)";
            ctx.fillRect (parseFloat(width/l)*index, height-(height*data[index]), width/l, (height*data[index]));

            ctx.strokeRect(parseFloat(width/l)*index, height-(height*data[index]), width/l, (height*data[index]));
        }
        // fillRect(x, y, width, height)

    } else {
        // canvas-unsupported code here
    }
});

