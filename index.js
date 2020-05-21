var socket;
socket = io.connect("http://localhost:5000");

function setup() {
  createCanvas(600, 400);
  background(51);
  socket.on("mouse", (data) => {
    // console.log(data);

    noStroke();
    fill(data.color);
    ellipse(data.x, data.y, 36, 36);
  });
}
function mouseDragged() {
//   console.log(mouseX + "," + mouseY);
  var data = {
    x: mouseX,
    y: mouseY,
  };
  socket.emit("mouse", data);
  noStroke();
  fill(255);
  ellipse(mouseX, mouseY, 36, 36);
}

function draw() {}

// window.onload=()=>{
//     var btnSalir = document.getElementById('btnSalir');
//     btnSalir.onclick=()=>{
//         console.log('saliendo');

//         socket.emit('disconnect',()=>{
//             console.log('desconectado');

//         });
//         console.log('salio');

//     }
// }
