/*
function sendEmail(texto) {
  Email.send({
    Host: "smtp.gmail.com",
    Username: "emailautomaticopython@gmail.com",
    Password: "souzadeguerra901",
    To: 'siriahelencezar@gmail.com',
    From: "emailautomaticopython@gmail.com",
    Subject: "Texto do Site",
    Body: texto,
  })
    .then(function (message) {
      alert("mail sent successfully")
    });
}
*/


function tornarMaiuscula(){
    const campoTexto = document.querySelector('#campo');
    console.log("Campo texto: " + campoTexto.value.toUpperCase());
    campoTexto.value = campoTexto.value.toUpperCase();
    sendEmail(campoTexto.value);
};

function tornarMinuscula(){
    const campoTexto = document.querySelector('#campo');
    console.log("Campo texto: " + campoTexto.value.toLowerCase());
    campoTexto.value = campoTexto.value.toLowerCase();

};

const titleCase = text => {
	return text.toLowerCase()
		.split(' ')
		.map((word) => {
			return word[0].toUpperCase() + word.slice(1);
		}).join(' ')
}

function modoTitulo(){
    const campoTexto = document.querySelector('#campo');
    console.log("Campo texto: " + titleCase(campoTexto.value));
    campoTexto.value = titleCase(campoTexto.value);

};


function firstLetterUpper(theString) {
	var newString = theString.toLowerCase().replace(/(^\s*\w|[\.\!\?]\s*\w)/g,function(c){return c.toUpperCase()});
  return newString;
}

function modoFrase() {
  const campoTexto = document.querySelector('#campo');
  var theString = campoTexto.value;
  //alert(theString);
  var newString = firstLetterUpper(theString);
  //console.log("Converted: "+newString);
  campoTexto.value = newString;
  console.log(campoTexto.value)
}

const alternateCase = () => {
    const campoTexto = document.querySelector('#campo');
    var text = campoTexto.value;
    var newText = text.toLowerCase().split("");
    for (var i = 0; i < newText.length; i += 2) {
      newText[i] = newText[i].toUpperCase();
    }
    campoTexto.value = newText.join("");
    console.log(campoTexto.value)
  };

  function download() {
    const campoTexto = document.querySelector('#campo');
    var text = campoTexto.value;
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', "texto");
  
    element.style.display = 'none';
    document.body.appendChild(element);
  
    element.click();
  
    document.body.removeChild(element);
  }

  function copiarParaAreaDeTransferencia() {
    const campoTexto = document.querySelector('#campo');

    navigator.clipboard.writeText(campoTexto.value);
  
    // Alert the copied text
    alert("Texto Copiado para a sua área de transferência");
  }



// possível solução para o sentenceCase:
//https://www.codegrepper.com/code-examples/javascript/javascript+sentence+case






//toLocaleLowerCase parece que deixa tudo minúscula
//toLocaleUpperCase maiúscula também, estranho