window.onload = () => {
  console.log("ok");
  var socket;
  socket = io.connect("http://localhost:5000");
  socket.emit('message','hola s');
  let mensaje = document.getElementById('miMensaje');
  let enviar = document.getElementById('enviar');
  let listaMensajes = document.getElementById('mensajes');
  socket.on('message',(datos)=>{
      console.log('recibido:'+datos);
    listaMensajes.innerHTML+='<li>'+datos+'</li>';
      
  })
  enviar.onclick=()=>{
    //   socket.send(mensaje.value)
      socket.emit('message',mensaje.value);
      mensaje.value="";
      
  }
};
